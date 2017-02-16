# AWS EC2, Django, Postgresql

## AWS EC2

### 1. 인스턴스 생성

- EC2 - Launch Instance - Ubuntu Server 16.04 LTS - t2.micro - Review and Launch - Launch

#### 1-1. 인스턴스 보안 설정

- Add Rule(SSH / TCP / 22 / My Ip)
- Add Rule(Custom TCP Rule / TCP / 8000 / Anywhere)

#### 1-2. Key Pair 생성

- Create new key pair - Download
- 다운받은 파일을 .ssh 폴더로 이동 `$ mv <key-pair-name>.pem ~/.ssh`

### 2. 인스턴스 접속

- 인스턴스 목록에서 우클릭 - Connect - 시키는 대로 할 것
- `$ cd .ssh`



## Set up

### Install packages

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-venv libpq-dev postgresql
```

### Set up postgresql

#### Create user to the system

```bash
$ sudo adduser <username>			# 유저 등록
$ sudo gpasswd -a <username> sudo	 # sudo 그룹에 넣음
$ sudo -i -u <username>
<username>@:~$
```

#### Create new role

```bash
<username>@:~$ sudo -i -u postgres				# postgres default account로 로그인
postgres@:~$ createuser --interactive
Enter name of role to add: <role-name>
Shall the new role be a superuser? (y/n) y
postgres@:~$ createdb <db-name>
postgres@:~$ exit
logout
<username>@:~$ psql
psql (9.5.5)
<role-name>=# \conninfo
<role-name>=# ALTER USER "role-name" WITH PASSWORD 'db-password';
ALTER ROLE
<role-name>=# \q
<username>@:~$
```



### Clone your django project from github

```bash
<username>@:~$ git clone https://github.com/<github-name>/<project>.git
<username>@:~$ cd <project>
<username>@:~/<project>$ python3 -m venv env
<username>@:~/<project>$ source env/bin/activate
(env) <username>@:~/<project>$ 
```



**[NOTE]** If warning occurs like this, :

```bash
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LC_CTYPE = "ko_KR.UTF-8",
	LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale ("en_US.UTF-8").
```

type like this:

```bash
$ export LC_ALL="en_US.UTF-8"
$ export LC_CTYPE="en_US.UTF-8"
```



### Run your django project

```bash
(env) $ pip install --upgrade pip
(env) $ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8000
```

And open http://<your-public-DNS>:8000 in browser.