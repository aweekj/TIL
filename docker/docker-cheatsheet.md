# Docker Cheatsheet

#### Get the list of all images
```bash
$ docker images
```


#### Remove single images

```bash
$ docker rmi IMAGE_NAME
```
You can use first three digits of Image ID instead of Image Name. For example, if Image ID is `7b66156f376c`,

```bash
$ docker rmi 7b6
```

#### Stop all containers

```bash
$ docker stop $(docker ps -a -q)
```

#### Remove all containers

```bash
$ docker rm $(docker ps -a -q)
```

#### Remove all images

```bash
$ docker rmi $(docker images -qf "dangling=true")
```

#### Remove all images except some images
Remove all images except `ubuntu` and `my-image`
```bash
$ docker rmi $(docker images | grep -v 'ubuntu\|my-image' | awk {'print $3'})
```
