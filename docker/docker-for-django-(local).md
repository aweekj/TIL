# Docker for django (Local)

## Docker

### 로컬에 도커 설치

* [여기]를 참고하여 설치 (https://docs.docker.com/engine/getstarted/linux_install_help/)

### 우분투 설치

```bash
$ docker pull ubuntu
Using default tag: latest
latest: Pulling from library/ubuntu
b3e1c725a85f: Pull complete 
4daad8bdde31: Pull complete 
63fe8c0068a8: Pull complete 
4a70713c436f: Pull complete 
bd842a2105a8: Pull complete 
Digest: sha256:7a64bc9c8843b0a8c8b8a7e4715b7615e4e1b0d8ca3c7e7a76ec8250899c397a
Status: Downloaded newer image for ubuntu:latest
                                                   
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              104bec311bcd        12 days ago         129 MB
```

### 컨테이너 실행

도커 명령어에 대한 자세한 내용은 [여기](http://pyrasis.com/Docker/Docker-HOWTO#run)를 참고

**run**

```bash
$ docker run -i -t -p 5050:5050 --name django-server ubuntu /bin/bash
```

**ps**

```bash
$ docker ps -a
```

**start**

```bash
$ docker start django-server
```

**attach**

```bash
$ docker attach django-server
```

## Django

```bash
$ apt-get install sudo
$ apt-get update
$ apt-get install git
$ apt-get install python3-pip
$ apt-get install python3-venv

```