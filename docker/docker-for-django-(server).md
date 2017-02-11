# Docker for django (Server)

## AWS EC2

1. 인스턴스 생성
* EC2 - Launch Instance - Ubuntu Server 16.04 LTS - t2.micro - Review and Launch - Launch
* Key pair 생성 후 선택

2. 인스턴스 보안 설정
* EC2 - Security Groups - Create Security Group - Inbound Edit
* Add Rule(SSH / TCP / 22 / My Ip)
* Add Rule(Custom TCP Rule / TCP / 8000 / Anywhere)

3. 접속
* 인스턴스 목록에서 우클릭 - Connect - 시키는 대로 할 것
* `cd .ssh`

## Docker

### 서버에 도커 설치

* [여기]를 참고하여 설치 (https://docs.docker.com/engine/getstarted/linux_install_help/)

* 설치 확인

```bash
$ docker --version
Docker version 1.12.1, build 23cf638

$ [sudo] docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c04b14da8d14: Pull complete 
Digest: sha256:0256e8a36e2070f7bf2d0b0763dbabdd67798512411de4cdcf9431a1feb60fd9
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker Hub account:
 https://hub.docker.com

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/

$ [sudo] docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              c54a2cc56cbb        5 months ago        1.848 kB

```

## Git and django

1. 설치

```bash
sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
```

2. Git clone
3. Runserver

## Connect

브라우저에서 EC2 - Running instances - Public DNS뒤에 :8000붙인 주소로 접속

---
## 더 읽어볼 것
- [Docker - Quickstart : Compose and Django](https://docs.docker.com/compose/django/)
- [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 16.04
  ](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)
- [Dockerizing a Python Django Web Application](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)
- [Packaging Django applications into Docker container images](http://michal.karzynski.pl/blog/2015/04/19/packaging-django-applications-as-docker-container-images/)
