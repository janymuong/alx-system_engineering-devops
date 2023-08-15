# Application Server
> `Nginx`, `Gunicorn`  

This project aims to enhance an existing web infrastructure, which serves web pages via Nginx, by adding an application server - with [AirBnB_clone_v2](https://github.com/janymuong/AirBnB_clone_v2) as the source for the setup. The application server will handle dynamic content and be integrated with Nginx to serve the Airbnb clone project.

## Background

The application server will be deployed as a WSGI server implementation using `Gunicorn` and configuring Nginx to proxy requests.

### What an Appliaction Server IS:
An application server’s fundamental job is to provide its clients with access to business logic, which generates dynamic content; that is, it’s code that transforms data to provide the specialized functionality offered by a business, service, or application in this case the AirBnB clone. Gunicorn has capabilities for processing user requests, interacting with databases, and executing application-specific logic.

> Reference:  
> [DIFF: web server vs. application server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)


## Server Information
Servers likely to be affected by this configuration:

- Servers: `SOME_ID-web-01`, `SOME_ID-web-02`, `SOME_ID-lb-01`
- Username: `ubuntu`
- IP Addresses: `web-01-IP`, `web-02-IP`, `LB-01-IP`
