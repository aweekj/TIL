## How to install and use PostgreSQLon Ubuntu

### Installation

우분투에서 PostgreSQL을 설치하려면

```bash
$ sudo apt-get update
$ sudo apt-get install postgresql postgresql-contrib
```

### Using PostgreSQL roles and databases

PostgreSQL 은 user와 group의 역할을 구별하지 않는 대신 좀더 유연한 용어인 `롤(role)`을 사용한다. PostgreSQL을 설치하면 `postgres` 라는 유저가 생성되는데, 이것은 Postgres 의 default  role 과 관련있다. 계정에 로그인 하려면

```bash
$ sudo -i -u postgres
```

그 후, Postgres prompt 로 들어가려면 

```
$ psql
```

prompt에서 나오려면

```
# \q
```

### Create a new role

새로운 롤을 생성하려면

```
$ createuser --interactive
```

이 명령어는 롤의 이름과 슈퍼유저인지 아닌지의 여부를 묻는다. 추가로 옵션을 지정할 수도 있는데, ` man createuser` 를 입력하면 옵션들의 명령어를 볼 수 있다.

### Create a new database

`test1` 이라는 유저가 있다면,  그 롤은 기본적으로 `test1`이라는 데이터베이스에 접속하려고 시도한다. `postgres` 로 로그인 한 상태에서 `test1`이라는 데이터베이스를 생성하려면

```bash
$ createdb test1
```

### Connect to Postgres with the new user

리눅스에서 `test1` 이라는 시스템 계정을 사용하고 있고(`adduser test1`으로 생성할 수 있다), `test1`이라는 Postgres  유저와 데이터베이스를 만들었다고 하자.

시스템 계정을 바꾸는 방법은

```
$ sudo -i -u test1
```

데이터베이스 `test1` 에 `test` 이라는 Postgres 유저로 접속하려면

```
$ psql
```

다른 데이터베이스에 접속하려면

```
$ psql -d postgres
```

prompt 에서 접속에 대한 정보를 보려면

```
# \conninfo
```



---

### Refer to

- [How To Install and Use PostgreSQL on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04)

  ​