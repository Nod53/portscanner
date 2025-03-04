# Python Port Scanner

## Overview

This is a lightweight Python tool that scans an IPv4 address for open ports. The script includes input validation and error handling for both the IP address and port inputs. It supports scanning:
- Individual ports (e.g., `22,80,443`)
- Ranges of ports (e.g., `80-90`)
- A combination of both (e.g., `22,80-85,443`)
- A predefined set of common ports by typing `common`

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
