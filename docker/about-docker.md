# About Docker

참고로 Docker(이하 도커) 초보임. 서버 셋팅용 스크립트를 짜다가, 귀찮음을 깨닫고 도커에 대해 알아본 것을 정리함. 도커는 프로그램+실행환경을 하나의 컨테이너로 추상화하여 어느 환경에서나 실행 가능하도록 함. 따라서 로컬에 개발 환경을 구축하는 대신, 도커 컨테이너를 개발 환경으로 사용 가능.



### 1. What is Docker?

도커에는 이미지와 컨테이너라는 개념이 있다. 

##### 이미지

- 실행에 필요한 파일과 설정값들을 포함하고 있는 것. 
- 레이어 개념을 사용한다. ubuntu 이미지가 `A` + `B` + `C`의 집합이라면, ubuntu 이미지를 베이스로 만든 nginx 이미지는 `A` + `B` + `C` + `nginx`. webapp 이미지를 nginx 이미지 기반으로 만들었다면 예상대로 `A` + `B` + `C` + `nginx` + `source` 레이어로 구성. webapp 소스를 수정하면 `A`, `B`, `C`, `nginx` 레이어를 제외한 새로운 `source(v2)` 레이어만 다운받으면 되기 때문에 굉장히 효율적으로 이미지를 관리할 수 있다.
- `Dockerfile` 에 이미지 생성과정을 적는다.
- 도커에도 깃허브 같은 도커허브가 있어서 이미지를 `push/pull` 할 수 있다.

##### 컨테이너

이미지를 실행한 상태



### 2. Installation

#### Linux

```bash
curl -s https://get.docker.com/ | sudo sh

sudo usermod -aG docker $USER # 현재 접속중인 사용자에게 권한주기
sudo usermod -aG docker your-user # your-user 사용자에게 권한주기
```

#### Mac OS

[Link](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac)

#### Windows

[Link](https://docs.docker.com/docker-for-windows/install/)



### 3. Run Docker

```bash
$ docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG ...]
```

`run` 실행 시 이미지가 없으면 `pull` -> `create` -> `start` 한다.

##### 실행 옵션

| OPTION | DESCRIPTION                       |
| ------ | --------------------------------- |
| -d     | detached mode 흔히 말하는 백그라운드 모드     |
| -p     | 호스트와 컨테이너의 포트를 연결 (포워딩)           |
| -v     | 호스트와 컨테이너의 디렉토리를 연결 (마운트)         |
| -e     | 컨테이너 내에서 사용할 환경변수 설정              |
| -name  | 컨테이너 이름 설정                        |
| --rm   | 프로세스 종료시 컨테이너 자동 제거               |
| -it    | -i와 -t를 동시에 사용한 것으로 터미널 입력을 위한 옵션 |
| -link  | 컨테이너 연결 [컨테이너명:별칭]                |



#### Example: ubuntu

```bash
$ docker run --rm -it ubuntu:16.04 /bin/bash
$ cat /etc/issue
Ubuntu 16.04.2 LTS \n \l
$ ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
$ exit
```



#### Example: tensorflow

```bash
$ docker run -d -p 8888:8888 -p 6006:6006 teamlab/pydata-tensorflow:0.1
```



### 4. Basic Commands

#### 컨테이너 목록 확인: ps

```bash
$ docker ps # 실행중인 컨테이너 목록
$ docker ps -a # 종료된 컨테이너까지 포함된 목록
```



#### 컨테이너 중지: stop

실행중인 컨테이너를 중지. `docker ps`로 컨테이너의 이름 또는 ID를 확인. ID는 앞부분만 입력해도 됨.

```bash
$ docker stop CONTAINER1 CONTAINER2 [CONTAINER...]
```



#### 컨테이너 제거: rm

종료된 컨테이너를 완전히 제거

```bash
$ docker rm CONTAINER1 CONTAINER2 [CONTAINER...]
$ docker rm -v $(docker ps -a -q -f status=exited) # 중지된 컨테이너를 모두 삭제
```



#### 이미지 목록 확인: images

```bash
$ docker images
```



#### 이미지 다운로드: pull

이미지를 최신 버전으로 다운로드

```bash
$ docker pull IMAGE
```



#### 이미지 삭제: rmi

사용하지 않는 이미지 용량을 차지하므로 지우는 것이 좋음. 실행중인 이미지는 삭제되지 않는다.

```bash
$ docker rmi IMAGE [IMAGE...]
```



#### 컨테이너 로그 보기: logs

```bash
$ docker logs CONTAINER # 전체 로그 출력
$ docker logs --tail 10 CONTAINER # 마지막 10개의 로그 출력
$ docker logs -f CONTAINER # 실시간으로 확인
```



#### 컨테이너 명령어 실행: exec

실행중인 컨테이너에 들어가거나 컨테이너의 파일을 실행할 때 사용

```bash
$ docker run -d -it ubuntu:16.10 /bin/bash # 예: 우분투 실행
$ docker ps # 컨테이너 아이디 6adf
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
6adf34959e8e        ubuntu:16.10        "/bin/bash"         51 seconds ago      Up 50 seconds                           quirky_kowalevski
$ docker exec -it 6adf /bin/bash # 우분투 접속
```



### 5. Docker Compose

이미지 다운, 컨테이너 실행 등을 `docker-compose.yml` 이라는 파일을 통해 한번에 해결.

리눅스는 docker-compose를 설치해야 한다.

```bash
$ curl -L "https://github.com/docker/compose/releases/download/1.9.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ chmod +x /usr/local/bin/docker-compose
```



#### Example: wordpress

디렉토리를 하나 만들고 그 안에 `docker-compose.yml`을 만든다

###### docker-compose.yml

```yaml
version: '2'

services:
   db:
     image: mysql:5.7
     volumes:
       - db_data:/var/lib/mysql
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: wordpress
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress

   wordpress:
     depends_on:
       - db
     image: wordpress:latest
     volumes:
       - wp_data:/var/www/html
     ports:
       - "8000:80"
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_PASSWORD: wordpress
volumes:
    db_data:
    wp_data:
```

그리고 

```bash
$ docker-compose up
```

이라고 하면 실행 됨





### Refer to

- [초보를 위한 도커 안내서](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html) : 이 시리즈에서 많이 배웠다. 차근차근 잘 설명되어있다.