# ALX-SE/Holberton School's Broken Apache HTTP Server Incident Report

<div align="center">
 <img src="./img/404d.jpg" width="640" height="200" />
</div>

> Copyright: [Inzone 404 pages](https://inzonedesign.com/blog/28-cleverly-funny-creative-404-error-pages/)


*Posted On: 11th Auguts, 2023*

By the On Call Person: Jany Muong


---
### Background Context:

**ALX Software Engineering/Holberton School** uses some `Apache HTTP Server` to teach its students on the working of server and web infrastructure etc. Students are given a full-on functioning Docker container with the requisite resources for learning concepts in real time. In this context a student uses a Docker container running a GNU/Linux Ubuntu Server that hosts an Apache web server. The "Docker Container" meant to be the vessel of knowledge, holding the Apache web server within its byte-filled heart, which would serve out beautiful static content to HTTP requests; it instead serves "404" messages and the likes :). In this tale of a seeming misconfig, darkness lurked. A server's promise of "`Hello Holberton`" vanished, replaced by a "`Empty reply from server`" chant - it went 'incognito'. That is not a very exciting situation, is it?


> **Note**  
> The container described above can be run from this base [`image`](https://hub.docker.com/r/holbertonschool/265-0/tags) from [Docker Hub](https://hub.docker.com/):  
> You can pull the Docker `image` above to a local machine/system and you could run a container from it and use it for your practice. See below for reference:  

```bash
vagrant@vagrant:~$ docker run -d -ti holbertonschool/265-0
Unable to find image 'holbertonschool/265-0' locally
14.04: Pulling from library/ubuntu
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


---
### Issue Summary:

- Time:  
> From **Jun 26, 2023 6:00 AM**  to **Jun 28, 2023 6:00 AM (UTC-4)**, students were greeted with `Empty reply from server` instead of the promised `Hello Holberton`by practice Docker containers. The impact was - most users encountered the dreaded 500 errors, with the peak disruption reaching 100% confusion as students could not practice what they know, I mean coming from a place of having learned new information. The elusive "Hello Holberton" went into hiding, yeah?


- **Root Cause:**   
At first, the team(me) thought it was an invalid configuration of the HTTP server. Ah, the obvious 'go to' heart of all mystery.  

> **Pro Tip:** When servers go silent, check if they've simply embarked on a solo journey to find themselves!
> Okay I am joking, it was not that or a misconfiguration. Apache service was not actually started. Yes, it wasn't.


### Timeline:

- **06:00 AM:** Alas, the cries of confused users echoe. The curtain of error is raised.
- **06:35 AM:** Our vigilant monitoring system PagerDuty blinks an alert, and the debugging knight comes wields his mind.
- **14:40:** Initial theory: A "Hello Holberton" overload? Attempted increased server capacity spell.
- **16:50:** Knight grows weary; no improvement...
- **23:10:** The knight veers off-course, blaming the innocent network latency and buffering for crimes not committed.
- **00:30 AM:** Knight sleeps ... zzzzz
- **05:00 AM:** Knight turns wizard; takes action, `docking` and cleansing the containers, releasing connections so that the ALX-SE 'gremlins' can have peace again.
- **06:00 AM:** '`Hello Holberton`'


### Root Cause and Resolution:

> will fill here

<div style="display: flex;">
  <div style="flex: 1; margin-right: 20px;">
    <img src="./img/stuff.jpg" alt="stuff" width="300" height="auto">
  </div>
  <div style="flex: 2;">
    <blockquote>
      <p>My son, you shall tread the path of containers and code, at your discretion!</p>
    </blockquote>
  </div>
</div>


### Corrective and Preventative Measures:
This segment lists out suggested corrective measures, and preventative measures.

- Regularly audit and cleanse helper scripts to keep web server up with reboots and preserve settings.
- Monitor connection activities and pool usage.
- Create scripts to automatically thwart any abnormal port 80 connections.
- Add monitoring on server memory to provide keep other services in check so that Apache has all optimization
