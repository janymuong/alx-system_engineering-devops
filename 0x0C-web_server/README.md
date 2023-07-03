# Web Server

This project focuses on setting up and managing web servers. It covers various aspects of web server configuration and administration, providing a foundation for serving web content.

## Requirements

> - Operating System: Ubuntu 16.04 LTS/Ubuntu 20.04 LTS  
> - Bash scripting  
> - Familiarity with Ubuntu server administration  
> - Understanding of web server concepts and protocols (HTTP, DNS, etc.)  
> - Basic knowledge of domain management (DNS record types)  


## Project Structure

The project includes various components and concepts related to web servers. Here's an overview of the key aspects:

1. Web Server Basics:
   - Understanding the role and functionality of web servers.
   - Configuring and managing web server software (e.g., Apache, Nginx - focus on Nginx).

2. File Transfer:
   - Transferring files to a server using `SSH` and `scp`.
   - Automating file transfer using Bash scripts.

3. Domain Management:
   - Working with DNS (Domain Name System) records.
   - Understanding DNS record types (A, CNAME, TXT, MX) and their usage.

5. Miscellaneous:
   - Monitoring server performance and resource usage.
   - Managing server logs and troubleshooting common issues.

## Usage

This project provides a set of scripts and guidelines to configure and manage web servers. Each component or concept may have its own dedicated script or documentation.

Example usage:
```bash
$ ./0-transfer_file some_file.html 8.8.8.8 ubuntu ~/.ssh/private_key
```
