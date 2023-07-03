# Load Balancer

This project focuses on configuring a load balancer using `HAProxy` to distribute traffic between multiple web servers. The load balancer helps improve the performance, scalability, and availability of web applications by evenly distributing incoming requests across the backend servers.

## Project Overview

The project consists of the following components:

- **Load Balancer Server** - `SOME-ID-lb-01`: The server responsible for balancing incoming traffic and distributing it to the backend web servers.
- **Web Servers** - `SOME-ID-web-01`, `SOME-ID-web-02`: Multiple backend servers hosting the web application on `Nginx`.

#### General Info:  
> You could copy files(eg Nginx configuration bash scripts) to the servers like this in CLI:  
>> `$ ./ssh_scp_file some_file.extension server-ip ubuntu ~/.ssh/private_key`

### Server Configuration

1. Configure the first web server (web-01) by executing the provided script. This script installs and configures Nginx as a web server on web-01, sets up the index.html file, and configures redirection and error pages.

2. Configure the second web server (web-02) to be identical to web-01. Use the script to configure Nginx on web-02 and add a custom HTTP response header (`X-Served-By`) to track the server's hostname.

### LB Configuration

1. Connect to the load balancer server (lb-01) using SSH:

   ```bash
   ssh ubuntu@lb-server-ip
   ```

2. Install HAProxy by executing the following commands:

   ```bash
   sudo apt-get update -y
   sudo apt-get install -y haproxy
   ```

3. Configure HAProxy to balance traffic between the web servers. Edit the HAProxy configuration file (/etc/haproxy/haproxy.cfg) and add backend server definitions for web-01 and web-02. Ensure the servers' IP addresses and ports are correctly specified.

4. Restart the HAProxy service to apply the configuration changes:

   ```bash
   sudo service haproxy restart
   ```

## Testing the Load Balancer

Once the setup is complete, you can test the load balancer by sending HTTP requests to the load balancer's IP address. The requests will be distributed among the web servers based on the configured load balancing algorithm.

You can use tools like `curl` or a web browser to send requests and observe the server responses.

> **Note**:  
> The custom HTTP response header (`X-Served-By`) will indicate which web server served the response.

```bash
# using curl
curl -I http://<lb-server-ip>

# output with custom header
HTTP/1.1 200 OK
X-Served-By: web-01
...
```

## Debug

If you encounter any issues during the setup or configuration process, please ensure the following:

- Scripts are executed with the appropriate permissions (e.g., `chmod +x script.sh`).
- IP addresses and hostnames are correctly specified in the configuration files.

## Resources

- [HAProxy Documentation](https://www.haproxy.org/documentation/)
- [Nginx Documentation](https://nginx.org/en/docs/)
