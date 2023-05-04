## Networking basics #1

> this covers theory for: `localhost/127.0.0.1`, `0.0.0.0`, `/etc/hosts`, `ifconfig/ip`, `nc(netcat)`, `cut` command, `telnet`

### localhost/127.0.0.1
`localhost` is a **hostname** that refers to the `current computer` used to access it. It is also known as a `loopback` address and can be accessed by the IP address `127.0.0.1`.

The **loopback** interface is a virtual network interface that the computer uses to communicate with itself. It is often used by network applications to test the network connection, troubleshoot issues or perform other tasks locally.

### 0.0.0.0
`0.0.0.0` is a special IP address that refers to all available IP addresses on the local machine. It is often used in network programming to indicate that the program should listen on all available network interfaces.

### `/etc/hosts`
`/etc/host`s is a file that contains `mappings` of `IP addresses` to `hostnames`. It is used by the **OS** to resolve hostnames to IP addresses when `DNS` is not available or when DNS is not used.

Entries in the ***/etc/hosts*** file are typically used to map hostnames to IP addresses on the local network. This file is often used to ***override DNS settings*** or to create local domains that are not registered with DNS.

### ifconfig/ip
`ifconfig` is a command-line utility that displays network interface configuration information. It allows you to view the IP address, netmask, and other network configuration settings for each network interface on your machine.

`ip` is a newer command-line utility that performs similar functions as ifconfig. It is designed to replace ifconfig and offers a more modern and flexible interface for managing network interfaces.

### nc (netcat)
`nc` (short for `netcat`) is a command-line utility that is used for `reading` and `writing` data across network connections. It is often used for testing network connectivity, sending and receiving files, and as a basic network troubleshooting tool.

usage:
```bash
$ cat testfile
# client side
hello test
$
```
```bash
# run the server
$ nc -l 2389 > test
$
```
```bash
# run the client
$ cat testfile | nc localhost 2389
$
```
```bash
# print the ‘test’ file at the server end
$ cat test
hello test
$
```


### cut (command)
The `cut` command is a Linux command-line utility that is used to extract sections from a file or input stream. It allows you to select specific columns or fields of text by specifying a delimiter character.
The cut command is often used in conjunction with other Linux utilities to manipulate and format text data.

### telnet
`telnet` is a command-line utility that is used to establish a TCP/IP connection to remote (another) computer or server. It is often used to test network connectivity and troubleshoot network issues.
The telnet command can be used to connect to a specific port on a remote server, allowing you to test the availability of a particular network service or application. It is also commonly used to connect to a remote computer's command-line interface, allowing you to execute commands on the remote machine.