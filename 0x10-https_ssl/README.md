# HTTPS - SSL

This project focuses on setting up `HTTPS` (Hypertext Transfer Protocol Secure) using `SSL` (Secure Sockets Layer) for a website or web application. It ensures secure communication between the client and the server by encrypting data transmission.

## Requirements

- Web servers (e.g. `Nginx`) and their configuration.
- A domain name or public IP address for *load balancer(HAProxy) server, web servers.*
- A valid SSL certificate issued by a trusted Certificate Authority (CA) - in this context `certbot`.
- Access to the server hosting your website or web application - in this context DotTech Domains `get.tech`.

## Installation

1. Obtain an SSL certificate:
   - Generate a self-signed SSL certificate.
2. Install the SSL certificate on your server:
   - Configure the HAProxy(Load Balancer) web server to use the SSL certificate.
   - Configure the server to listen on the HTTPS port (typically port 443).
   - Enable SSL/redirect scheme https code 301 if !{ ssl_fc } to `HTTPS`.
3. Update your website/application code:
   - Ensure that your website or web application uses secure URLs (https://) for all internal links and external resources (e.g., images, scripts, stylesheets).
4. Test the SSL configuration:
   - Access your website using the HTTPS protocol (https://) and verify that the SSL certificate is valid and the connection is secure.
   
## Usage

Once the SSL configuration is complete, your website or web application will be accessible via the HTTPS protocol. Users can access your site securely by prefixing the URL with `https://`. Ensure that all HTTP requests are automatically redirected to HTTPS for better security.

## Resources

- [OpenSSL](https://www.openssl.org/): A powerful toolkit for SSL/TLS protocols and certificate management.
- [Certbot](https://certbot.eff.org/): A free, open-source tool to automatically obtain and manage SSL certificates.
- [Mozilla SSL Configuration Generator](https://mozilla.github.io/server-side-tls/ssl-config-generator/): Helps generate secure SSL configurations for various web servers.
