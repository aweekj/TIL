# Deploying Django project on ubuntu using nginx and gunicorn

이 글은 Django 프로젝트를 nginx와 gunicorn을 이용하여 ubuntu 서버에 배포하는 과정을 정리한 글이다. 도메인 구매도, vps 서버 구매도 모두 처음이었기 때문에 삽질을 많이 했다.



## 서버 설정

### 1. 서버-도메인 연결[^1]

먼저 서버와 도메인을 구매한다. 서버는 [국내 클라우드 서버호스팅 비교](https://blog.lael.be/post/44) 글 을 참고하여 [ConoHa](https://www.conoha.jp/referral/?token=dKu6u1tdfEn8M0SX91iTgL9SB24ofA6k48Km5Kz.FoesM63ZRo4-5VI)에서 월 900엔짜리 서버를 사고,  도메인은 [PHPS](https://www.phps.kr/)에서 샀다.

서버를 구매할 때 initial root password를 설정하고, ssh 파일도 다운받게 된다(물론 기존의 파일을 사용할 수도 있다). 초기에는 이 비밀번호와 ssh 파일을 통해 서버에 접속하게 되므로 잘 보관해 두는 것이 좋다.

도메인을 사고 나면 도메인과 내 서버의 아이피로 연결되는 과정이 필요한데, 이 역할을 하는 것이 DNS 서버이다. PHPS에서 도메인의 네임서버를 입력하는 칸이 있는데 이 부분에 ConoHa에서 제공하는 네임서버를 입력했다. 그리고 ConoHa의 DNS 설정에서 내 서버의 도메인을 추가한다. 

### 2. 서버 접속

서버를 구매할 때 다운 받았던 (혹은 사용했던) ssh파일을 사용해서 서버에 접속한다. 파일 이름이 `my-ssh-key-file.pem` 이고 구매한 서버의 ip가 `***.**.**.***`이라면,

```bash
$ chmod 400 my-ssh-key-file.pem # 권한 변경. 처음 한번만 하면 됨
$ ssh -i my-ssh-key-file.pem root@***.**.**.*** # root 계정으로 서버 접속
```

서버에 접속하고 나면 `$ date` 를 입력하여 시간이 잘 나오는지 확인해보자. 일본에 있는 서버이기 때문에 별도의 설정은 하지 않아도 된다.

### 3. root 계정 암호 변경

만약을 위해 root 계정의 암호를 변경한다.

```bash
$ passwd
```

### 4. 서버 유저 추가

보안을 위해 서버의 계정을 새로 만들고, 앞으로는 그 계정을 사용하기로 한다. 새 계정의 아이디를 `my-user` 라고 하자.

```bash
$ adduser my-user # 계정 생성
$ adduser my-user sudo # 관리자 권한 부여
$ login my-user # 로그인
```

### 5. SSH 파일 생성 및 서버에 등록[^2]

앞서 ssh 파일로 서버에 접속할 때 root계정으로 로그인 했었다. 이제 `my-user` 계정을 사용하기로 했으므로 접속할 때부터 `my-user`로 로그인하기 위해 새로운 ssh키를 만든다. 

먼저 클라이언트에서 `ssh-keygen` 명령어로 ssh 파일을 생성한다.

```bash
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): new-ssh-key-file.pem # ssh 파일명
Enter passphrase (empty for no passphrase): # 최초 등록 시 사용할 비밀문구
Enter same passphrase again:
Your identification has been saved in new-ssh-key-file.pem.
Your public key has been saved in new-ssh-key-file.pem.pub.
```

`new-ssh-key-file.pem`와 `new-ssh-key-file.pem.pub`이 생성된다. `*.pub`은 공개키인데, `cat`명령으로 공개키의 내용을 출력할 수 있다.

```bash
$ cat new-ssh-key-file.pem.pub # 공개키 출력
```

그리고 서버에 공개키를 등록한다.

```bash
$ mkdir ~/.ssh && cd ~/.ssh 
$ cat >> authorized_keys
# 이 상태에서 클라이언트에서 출력했던 공개키를 복사 후 붙여넣은 다음, 줄을 바꾼후 Ctrl+d를 눌러 저장한다.
```

이렇게 하면 이제 서버에 접속할 때  `my-user`로 바로 로그인이 가능하다.

```bash
$ ssh -i new-ssh-key-file.pem my-user@***.**.**.*** # my-user 계정으로 서버 접속
```

### 6. root 계정 비활성화[^3]

보안을 위해 root 계정으로 로그인하지 못하도록 설정한다.

```bash
$ sudo vim /etc/ssh/sshd_config
```

```bash
# Authentication:
LoginGraceTime 120  
PermitRootLogin no # yes에서 no로 변경
```

해당 위치를 찾을때는 `/PermitRootLogin`를 입력하면 편리하다. 이제 root 계정으로는 서버에 접속할 수 없게 되었다.

변경사항들을 적용하려면 ssh 서비스를 재시작해야 한다.

```bash
$ sudo service ssh restart
```

### 7. 방화벽 설정

우분투의 기본 방화벽인 ufw를 제공한다. 기본적으로 ufw는 disable로 설정되어 있다. 보안을 위해 방화벽을 설정한다.

```bash
$ sudo ufw allow ssh
$ sudo ufw allow http
$ sudo ufw allow https
$ sudo ufw allow ftp
$ sudo ufw enable # 방화벽 설정
$ sudo ufw status # 방화벽 상태 확인
```

그리고 Brute-force에 대비하기 위해 `sshguard`를 설치한다. `sshguard`는 지정된 횟수만큼 접속 시도가 들어오면 방화벽에서 바로 차단한다.

```bash
$ sudo apt-get install sshguard
$ sudo service sshguard start
```

### 8. 언어 설정

다음과 같은 경고를 계속 마주쳤다면, 언어를 설정해주도록 하자.

```bash
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LC_CTYPE = "ko_KR.UTF-8",
	LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale ("en_US.UTF-8").
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
```

```bash
$ vim /etc/default/locale
LANG="en_US.UTF-8"  
LANGUAGE="en_US.UTF-8"  
LC_ALL="en_US.UTF-8"  
```

### 9. 패키지 설치

```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install zsh git
```

zsh와 oh-my-zsh를 사용한다면 다음을 입력하자.

```bash
$ curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh # oh-my-zsh 설치
$ chsh -s $(which zsh) # 기본 셸을 zsh로 변경
```



여기까지 서버 설정이 끝났다. 이제 서버를 재부팅하고 프로젝트 설정으로 넘어간다.

```bash
$ sudo reboot
```





## 프로젝트 설정[^4]

프로젝트 전체 구조는 다음과 같다.

```bash
.
└── projects
    └── myproject
        ├── config
        │   ├── gunicorn.service
        │   ├── myproject_nginx.conf
        │   └── myproject.sock
        ├── env
        ├── log
        │   ├── access.log
        │   └── error.log
        └── myproject
            ├── manage.py
            ├── myproject
            │   ├── __init__.py
            │   ├── settings.py
            │   ├── urls.py
            │   └── wsgi.py
            └── static
```



### 1. 패키지 설치

```bash
$ sudo apt-get install python3-dev python3-pip python3-venv nginx 
$ sudo apt-get install postgresql postgresql-contrib libpq-dev # postgresql 관련 패키지
```

### 2. 가상환경 설정

먼저 프로젝트들은 `~/projects` 폴더를 만들어서 관리할 것이다. 프로젝트 이름이 `myproject`라고 한다면

```bash
$ mkdir projects && cd projects
$ mkdir myproject && cd myproject # 프로젝트 폴더 생성
$ python3 -m venv env # 가상환경 생성
$ source env/bin/activate # 가상환경 활성화
(env) $
```

### 3. nginx 설정

Django 프로젝트를 설정하기 전에 nginx 관련 설정을 먼저 하자.

```bash
(env) $ mkdir log config
(env) $ cd log
(env) $ touch access.log error.log
(env) $ cd ..
(env) $ cd config
(env) $ vim myproject_nginx.conf
```

###### ~/projects/myproject/config/myproject_nginx.conf

```bash
server {
        # the port your site will be served on
        listen 80;
 
        # the domain name it will serve for
        server_name     example.io; # 여기에 도메인 주소를 적는다
        charset         utf-8;
 
        access_log      /home/my-user/projects/myproject/log/access.log;
        error_log       /home/my-user/projects/myproject/log/error.log;
 
        location /static/ { # STATIC_URL
            alias /home/my-user/projects/myproject/myproject/static/; # STATIC_ROOT
            expires 30d;
        }

        location / {
            include proxy_params;
            proxy_pass http://unix:/home/my-user/projects/myproject/config/myproject.sock;
        }
}
```

이제 이 파일을 nginx 경로에 추가한다.

```bash
(env) $ sudo ln -s ~/projects/myproject/config/myproject_nginx.conf /etc/nginx/sites-enabled/
```

그리고 nginx 설정 파일의 문법을 검사하고 서비스를 시작한다.

```bash
(env) $ sudo nginx -t
(env) $ sudo systemctl start nginx
(env) $ sudo ufw allow 8000 # Django의 runserver 기능을 위해 8000번 포트도 열어준다.
```

### 3. 데이터베이스 설정

Django 프로젝트에서 postgresql을 사용한다면 다음과 같은 설정을 거쳐야 한다.

```bash
(env) $ sudo -u postgres psql
postgres=# CREATE DATABASE myproject; # 데이터베이스 생성
postgres=# CREATE USER myprojectuser with PASSWORD 'password'; # 유저 생성
postgres=# GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser; # 권한 할당
postgres=# \q
```

### 4. 프로젝트 생성

실제 프로젝트는 git clone을 통해 가져왔지만 편의상 프로젝트를 새로 생성하는 것으로 글을 쓰겠다.

```bash
(env) $ pip install --upgrade pip
(env) $ pip install django gunicorn psycopg2 whitenoise
(env) $ django-admin startproject myproject
(env) $ cd myproject
(env) $ vim myproject/settings.py
```

###### myproject/settings.py

```python
...
ALLOWED_HOSTS = ['my_domain_name']
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
...
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

###### myproject/wsgi.py

```python
from whitenoise.django import DjangoWhiteNoise
...
application = DjangoWhiteNoise(get_wsgi_application())
...
```

#### 프로젝트 실행

```bash
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py collectstatic
(env) $ python manage.py runserver 0.0.0.0:8000
```

http://my_domain_name:8000/ 으로 접속하여 내용이 잘 출력되는지 확인한다.



### 5. Gunicorn 설정

```bash
(env) $ gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application
```

Gunicorn을 통해 서버를 구동한다. 마찬가지로 http://my_domain_name:8000/ 으로 접속하여 내용이 잘 출력되는지 확인한다. 잘 동작한다면 `deactivate`로 가상환경을 종료하자.

그리고 Gunicorn의 서비스 스크립트를 만든다.

###### ~/projects/myproject/config/gunicorn.service

```bash
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=my-user
Group=www-data
WorkingDirectory=/home/my-user/projects/myproject/myproject
ExecStart=/home/my-user/projects/myproject/env/bin/gunicorn \
        --workers 3 \
        --bind unix:/home/my-user/projects/myproject/config/myproject.sock \
        myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```

이제 이 파일을 서비스에 추가하고 서비스를 실행시킨다.

```bash
$ sudo ln -s ~/projects/myproject/config/gunicorn.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl start gunicorn
$ sudo systemctl enable gunicorn
$ sudo systemctl status gunicorn
```

마지막으로 방화벽을 설정한다.

```bash
$ sudo ufw delete 8000
$ sudo ufw allow 'Nginx Full'
```

http://my_domain_name/ 으로 접속하여 내용이 잘 출력되는지 확인한다.



[^1]: [maxchung님의 블로그](http://www.maxchung.com/2015/11/06/domain-%EA%B5%AC%EC%9E%85%EA%B8%B0-%EB%B0%8F-conoha%EC%97%90-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0/)를 참고했다.
[^2]: [haruair님의 블로그](http://www.haruair.com/blog/2220)를 참고했다.
[^3]: [chann님의 블로그](https://blog.chann.kr/initial-server-setup-with-ubuntu-14-04/)를 참고했다.
[^4]: [quaz님의 블로그](https://blog.qwaz.io/dev-diary/서버-세팅하기-1부)와 [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)을 참고했다.