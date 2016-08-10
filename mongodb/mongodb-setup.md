# Install Mongo DB On OS X
[Document](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

```bash
$ brew update
$ brew install mongodb --devel
```

# Run Mongo DB

Set path before run

```bash
$ sudo mkdir -p /data/db
$ whoami
user-name
$ sudo chown user-name /data/db
$ vim ~/.bash_profile

export MONGO_PATH=/usr/local/bin/mongodb
export PATH=$PATH:$MONGO_PATH/bin
```

```bash
## restart terminal
$ mongod

## start another terminal
$ mongo
```
