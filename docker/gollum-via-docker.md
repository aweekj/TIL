# Gollum via Docker

## Prerequisite: Docker

Docker가 깔려있지 않다면 Docker 를 설치한다.

* [Docker for Mac](https://docs.docker.com/docker-for-mac/)
* [Docker for Windows](https://docs.docker.com/docker-for-windows/)

또는
* [Docker toolbox](https://www.docker.com/products/docker-toolbox) 설치 후 **Docker Quickstart Terminal**를 실행

## Prerequisite: Git
설명이 필요없다..

## Preparing the Gollum Workspace

```bash
$ cd ~/YOUR_DIRECTORY
$ git init
```

## Creating the Dockerfile
`YOUR_DIRECTORY` 폴더 안에 `Dockerfile` 을 만들 것이다.

```bash
$ touch Dockerfile
$ open Dockerfile
```

Dockerfile에 다음 내용을 복사-붙여넣기 한다.

```
FROM ruby:latest
RUN apt-get -y update && apt-get -y install libicu-dev
RUN gem install gollum
RUN gem install github-markdown org-ruby
VOLUME /wiki
WORKDIR /wiki
CMD ["gollum", "--port", "80"]
EXPOSE 80
```

이 파일은 Docker 에 다음 사항들을 알려준다.

1. [official Ruby repo on Docker Hub](https://hub.docker.com/_/ruby/)의 이미지를 기준으로 함.
2. developer tools, gollum, dipendencies를 설치.
3. Docker container의 작업 디렉토리를 변경하고, container 안의 wiki 폴더에 external symlink 를 제공.
4. port 80에서 gollum engine을 자동으로 시작.
5. container의 port를 노출시켜 접속할 수 있도록 함.

## Building the Docker image
```bash
$ docker build -t gollum .
```
*주의* - 마지막의 . 을 빼먹지 않도록 한다.

## Running the Docker Container

```bash
$ docker run -v `pwd`:/wiki -p 4567:80 gollum
```

*주의* - Windows의 경우 아래와 같이 실행한다.

```bash
$ docker run -v /`pwd`:/wiki -p 4567:80 gollum
```

## Accessing the Gollum GUI
[http://127.0.0.1:4567](http://127.0.0.1:4567)에 접속한다.

(Commit 한 문서만 보인다.)

## 참고링크
* [Gollum via Docker](https://github.com/gollum/gollum/wiki/Gollum-via-Docker)
* [Build your own image - Docker Official Document]( https://docs.docker.com/engine/getstarted/step_four/)
* [Docker for mac 훑어보기](http://nolboo.kim/blog/2016/08/02/docker-for-mac/)
