# ALX-SE/Holberton School's Broken Apache HTTP Server Incident Report

<div align="center">
 <img src="./img/404d.jpg" width="640" height="200" />
</div>

> Copyright: [Inzone 404 pages](https://inzonedesign.com/blog/28-cleverly-funny-creative-404-error-pages/)

---
### Background Context:

**ALX Software Engineering/Holberton School** uses some `Apache HTTP Server` to teach it's students on the working of server ifrastructure, web servers, web infrastructure etc. Students are given a full-on functioning Docker container with the requisite resources for learning concepts in real time. In this context I student uses a Docker container running a GNU/Linux Ubuntu Server that hosts an Apache web server, which serves out static content to HTTP requests.


> **Note**  
> The container described above can be run from this base [`image`](https://hub.docker.com/r/holbertonschool/265-0/tags) on [Docker Hub](https://hub.docker.com/):  
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
root@76f44c0da25e:/# echo "I am in $(hostname) Docker container"
I am in 76f44c0da25e Docker container
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK > /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/# #CTRL + D
vagrant@vagrant:~$
```



