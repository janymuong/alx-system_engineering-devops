# SSH

This project focuses on `Secure Shell (SSH)`, a network protocol used for secure remote communication between systems. The project includes a set of Bash scripts that demonstrate various SSH operations.

## Prerequisites
> environment:  
>> - Ubuntu 20.04 LTS  
>> - Bash shell  
>> - Editors: vi, vim, emacs  


## Project Structure

The project contains the following files:

- `0-use_a_private_key`: a bash script that uses ssh to connect to your server using a private key to connect to a remote shell w/ username `ubuntu`  
- `1-create_ssh_key_pair`: a Bash script that creates an RSA key pair.  
- `2-ssh_config`:  Client configuration file.  
- `100-puppet_ssh_config.pp`:  Client configuration file (but w/ Puppet).  


## Usage
Sample usage

   ```
   ./0-use_a_private_key
   ```
