import socket
import threading
import argparse

def scan_port(host, port):
    # Attempt to connect to specified host and port.
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sets a timeout so the script doesn't hang on closed ports
        sock.settimeout(1)
        result = socket.connect_ex((host, port))
        if result == 0:
            print(f"port {port} is open on {host}.")
        sock.close()
    except Exception as e:
        # will add error handling here
        pass

def main():
    
