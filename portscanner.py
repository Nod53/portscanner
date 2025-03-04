import socket
import threading
import sys

# Global list to store open ports
open_ports = []

def validate_ip(ip):
    """Validate that the IP address is in IPv4 dotted decimal format."""
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            num = int(part)
        except ValueError:
            return False
        if num < 0 or num > 255:
            return False
    return True

def parse_ports(ports_str):
    """
    Parse a string of ports and ranges into a list of port numbers.
    Returns None if any part of the input is invalid.
    Valid port numbers are in the range 1-65535.
    """
    ports = []
    parts = ports_str.split(',')
    for part in parts:
        part = part.strip()
        if '-' in part:
            try:
                start_str, end_str = part.split('-')
                start, end = int(start_str), int(end_str)
                if start > end or start < 1 or end > 65535:
                    return None
                ports.extend(range(start, end + 1))
            except ValueError:
                return None
        else:
            try:
                port = int(part)
                if port < 1 or port > 65535:
                    return None
                ports.append(port)
            except ValueError:
                return None
    return ports

def get_valid_ip():
    """Prompt the user for a valid IP address up to 3 times."""
    attempts = 3
    while attempts > 0:
        ip = input("Enter the IP address to scan (IPv4 format, e.g. 192.168.1.1): ").strip()
        if validate_ip(ip):
            return ip
        else:
            print("Invalid IP address. Please ensure it's in the format x.x.x.x with each octet between 0 and 255.")
            attempts -= 1
    print("Exceeded maximum attempts. Exiting.")
    sys.exit(1)

def get_valid_ports():
    """Prompt the user for valid port input up to 3 times."""
    attempts = 3
    while attempts > 0:
        ports_input = input("Enter ports (e.g. '22,80,443', '80-90,443', or type 'common' for common ports): ").strip()
        if ports_input.lower() == 'common':
            # Expanded list of common ports:
            common_ports = [
                20, 21, 22, 23, 25, 53, 80, 110, 123, 137, 138, 139,
                143, 161, 162, 443, 445, 465, 993, 995, 3306, 3389,
                5432, 5900, 8080, 8443
            ]
            return common_ports
        else:
            ports = parse_ports(ports_input)
            if ports is not None and len(ports) > 0:
                return ports
            else:
                print("Invalid port input. Please try again.")
                attempts -= 1
    print("Exceeded maximum attempts. Exiting.")
    sys.exit(1)

def scan_port(host, port):
    """Attempt to connect to the specified host and port, and record if open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open on {host}.")
            open_ports.append(port)
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def main():
    host = get_valid_ip()
    ports = get_valid_ports()

    print(f"Starting scan on host: {host}")

    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Print summary of open ports
    print("\nScan Summary:")
    if open_ports:
        print(f"Open ports ({len(open_ports)}): {sorted(open_ports)}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
