# Docker for Jekyll

### Create Dockerfile

```bash
$ touch Dockerfile
```

#### Dockerfile
```
FROM ruby:latest
WORKDIR /root
RUN ruby -S gem install jekyll
EXPOSE 4000
```

### Build Image
Insert `IMAGE_NAME` whatever you want.
```bash
$ docker build -t IMAGE_NAME .
```

### Create new jekyll blog
*NOTE* - Skip this if you already has jekyll blog.

```bash
$ docker run -it -v `pwd`:/root IMAGE_NAME ruby -S jekyll new . --force
```

### Run jekyll server

```bash
$ docker run -it -v $(pwd):/root -p 4000:4000 IMAGE_NAME \
	ruby -S jekyll serve --host=0.0.0.0 --watch --force_polling
```

* Run a interactive TTY from docker (`--it`)
* Mounts current directory inside container at /root (`-v $(pwd):/root`)
* Expose port 4000 from container to host (`-p 4000:4000`)
* Uses `IMAGE_NAME` image to run container
* Ups Jekyll server using `ruby -S jekyll serve`
* Sets Jekyll host to 0.0.0.0 (`--host=0.0.0.0`)
* Forces Jekyll to watch modifications inside blog skeleton (`--watch`)
* Forces Jekyll to polling periodically in order to detect changes (`--force_polling`)





## Refer to
[Creating a GitHub Jekyll Blog using Docker](http://salizzar.net/2014/11/06/creating-a-github-jekyll-blog-using-docker/)
