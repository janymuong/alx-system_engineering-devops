# ALX-SE/Holberton School's Broken Apache HTTP Server Incident Report

<div align="center">
 <img src="./img/404d.jpg" width="640" height="240" />
</div>

> Copyright: [Inzone 404 pages](https://inzonedesign.com/blog/28-cleverly-funny-creative-404-error-pages/)


*Posted On: August 11th, 2023*

By the ***On Call Person***: [Jany Muong](https://github.com/janymuong/)


---
### Background Context:

**ALX Software Engineering/Holberton School** uses some `Apache HTTP Server` to teach its students on the working of web servers and web infrastructure etc. Students are given a full-on functioning Docker container with the requisite resources for learning concepts in real time. In this context a student uses a Docker container running a GNU/Linux Ubuntu Server that hosts an Apache web server. However, the "Docker Container" meant to be the vessel of knowledge, holding the Apache web server within its byte-filled heart, which would serve out beautiful static content to HTTP requests; it instead serves "404" messages and the likes :). In this mix of a seeming misconfig, darkness lurked. A server's promise of `'Hello Holberton'` vanished, replaced by a `'Empty reply from server'` chant. It went 'incognito', basically. That is not a very exciting situation, is it?  

<br/>

> **Note**  
> The container described above can be run from this base [`image`](https://hub.docker.com/r/holbertonschool/265-0/tags) from [Docker Hub](https://hub.docker.com/):  
> You can pull the Docker `image` to a local machine/system and you could run a container from it and use it for your practice.  
> See below for reference:  

```bash
vagrant@vagrant:~$ docker run -d -ti holbertonschool/265-0
Unable to find image 'holbertonschool/265-0' locally
265-0: Pulling from holbertonschool/265-0
34667c7e4631: Already exists
d18d76a881a4: Already exists
119c7358fbfc: Already exists
2aaf13f3eff0: Already exists
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for holbertonschool/265-0
76f44c0da25e1fdf6bcd4fbc49f4d7b658aba89684080ea5d6e8a0d832be9ff9
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
76f44c0da25e        holbertonschool/265-0        "/bin/bash"         13 seconds ago      Up 12 seconds                           infallible_bhabha
vagrant@vagrant:~$ docker exec -i 76f44c0da25e hostname
76f44c0da25e
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
root@76f44c0da25e:/# echo "I have an address in RAM in $(hostname) Docker container"
I have an address in RAM in 76f44c0da25e Docker container
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK > /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/# # CTRL + D
vagrant@vagrant:~$
```

<br/><br/>


---
## Issue Summary:

- Time:  
> From **Jun 28, 2023 6:00 AM** to **Jun 28, 2023 12:00 PM (UTC-4)**, students were greeted with an `'Empty reply from server'` text instead of the promised `'Hello Holberton'` served out by practice Docker containers. The impact was - most users encountered the dreaded `404/500` *errors*, with the peak disruption reaching 100% confusion as students could not practice what they know, I mean coming from a place of having learned new information. The elusive ***'Hello Holberton'*** went into hiding, yeah?

- **Root Cause:**   
At first, the team(me) thought it was an invalid configuration of the HTTP server. Ah, the obvious 'go to' heart of all mystery.  

> **Pro Tip:**  
> When servers go silent, check if they've simply embarked on a solo journey to find themselves!
> Okay I am joking, it was not that or a misconfiguration. Apache service was not actually started. Yes, it wasn't.

<br/>


## Timeline:

- **06:00 AM:** Alas, the cries of confused users echo. The curtain of error is raised.
- **06:35 AM:** Our vigilant monitoring system [*PagerDuty*](https://www.pagerduty.com/) blinks an alert, and the debugging knight(me) wields his mind.
- **07:40:** Initial theory: A 'Hello Holberton' overload? Analyzes memory and disk usage.
- **08:00 AM:** Knight grows weary; no improvement...
- **09:10 AM:** The knight veers off-course, blaming the innocent network latency and buffering for crimes not committed.
- **11:30 AM:** Knight takes a day nap... zzzzz
- **12:00 PM:** Knight turns wizard; takes action, `docking` and cleansing the containers, releasing connections so that the ALX-SE 'gremlins' can have peace again.
- **12:30 PM:** `'Hello Holberton'`
<br/><br/>


## Root Cause and Resolution:
The initial assumption was that the web server was running :)
After trying out the usual non-exhaustive debugging flow assumptions e.g. misconfigurations, checking on logs, checking ports, firewalls or memory overload, we came to the grumpling realization that the `Apache` service was not started on container boot to be begin with. The HTTP server was expected to have been up from the jump.
```bash
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
```
Here we can see that after starting my Docker container, I `curl` the *port* `8080` mapped to the ***Docker container port 80***, it does not return a page but an error message `'curl: (52) Empty reply from server'`  

<br/>

So we start it with a script:
```bash
root@76f44c0da25e:/# cat apache-script
#!/usr/bin/env bash
# Bash: debug fix unresponsive apache server
sudo systemctl status apache2
echo "ServerName apacheindocker.com" >> /etc/apache2/apache2.conf
sudo systemctl start apache2
root@76f44c0da25e:/#
```

```bash
vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
```

<br/>

> "My son, you shall tread the path of containers and code, at your discretion!"  
>     - Me assuring one student that the container has been fixed:
<div align="center">
    <img src="./img/stuff.jpg" alt="stuff" width="500" height="300">
</div>
<br/><br/>


## Corrective and Preventative Measures:
This segment lists out suggested corrective measures, and preventative measures.
The scipts with the functionality described below could be wrapped within the application dependencies (as part of the server dependencies for [Apache](https://en.wikipedia.org/wiki/Apache_HTTP_Server)) when creating the docker image.
- Regularly audit and cleanse helper scripts to keep web server up with reboots and preserve settings.
- Monitor connection activities and pool usage.
- Create scripts to automatically thwart any abnormal port 80 connections.
- Add monitoring on server memory to keep other services in check so that Apache has all optimization
