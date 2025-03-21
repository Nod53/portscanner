# Python Port Scanner

## Overview

This is a lightweight Python tool that scans an IPv4 address for open ports. The script includes input validation and error handling for both the IP address and port inputs. It supports scanning:
- Individual ports (e.g., `22,80,443`)
- Ranges of ports (e.g., `80-90`)
- A combination of both (e.g., `22,80-85,443`)
- A predefined set of common ports by typing `common`

### Common Ports

20: FTP Data  
21: FTP Control  
22: SSH  
23: Telnet  
25: SMTP  
53: DNS  
80: HTTP  
110: POP3  
123: NTP  
137: NetBIOS Name Service  
138: NetBIOS Datagram Service  
139: NetBIOS Session Service  
143: IMAP  
161: SNMP  
162: SNMP Trap  
443: HTTPS  
445: SMB  
465: SMTPS  
993: IMAPS  
995: POP3S  
3306: MySQL  
3389: RDP  
5432: PostgreSQL  
5900: VNC  
8080: Alternate HTTP  
8443: Alternate HTTPS  

## Features

- **IP Address Validation:**  
  Checks that the entered IP address is in proper IPv4 format (four octets separated by dots, each between 0 and 255).

- **Port Input Parsing:**  
  Accepts comma-separated values, ranges (e.g., `80-90`), or a mixture of both. It also offers a list of common ports if the user types `common`.

- **Error Handling:**  
  Provides up to 3 attempts for both IP address and port inputs before exiting if invalid inputs are detected.

- **Concurrent Scanning:**  
  Uses Python's threading to scan multiple ports simultaneously.

- **Output:**  
  Only announces ports that are open, then displays a summary of all open ports at the end of the scan.

## Disclaimer

**Important:** Use this tool only on systems that you have explicit permission to scan. Unauthorised port scanning may be illegal and unethical.

## Requirements

- Python 3.x
