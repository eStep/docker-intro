When working with Docker it is important to understand the difference
between image and the container. As described in Docker documentation:

> **Docker images** are the basis of containers. An image is an ordered
> collection of root filesystem changes and the corresponding execution
> parameters for use within a container runtime. They are read only.


> **Container** is a runtime instance of a docker image.

We will start with running a container based on `hello-word` image.

Please run all the following commands in your home directory. Otherwise you
can encounter problems with mounting local volumes.

```sh
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b901d36b6f2f: Pull complete
0a6ba66e537a: Pull complete
Digest: sha256:8be990ef2aeb16dbcb9271ddfe2610fa6658d13f6dfb8bc72074cc1ca36966a7
Status: Downloaded newer image for hello-world:latest

Hello from Docker.
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
 https://docs.docker.com/userguide/
```
When you run this command `Docker` will:
* check if `hello-world` image is available locally
* download the image (from Docker Hub) if needed
* load the image into the container and run it

This container does not do much it outputs the message above and shuts down.
Let us list all running containers.
```sh
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
We don't see any running containers because as we said the container shut down
after it printed out the message. We can list all stopped and running containers.
```sh
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
78970e1f7290        hello-world         "/hello"            3 seconds ago       Exited (0) 2 seconds ago                       admiring_panini
```
We should also be able to see the image that the `admiring_panini` container
has been instantiated from.
```sh
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
hello-world         latest              0a6ba66e537a        3 months ago        960 B
```
Old containers are kept by default, so after a while the list you see when
running `docker ps -a` can get very long. You can remove not used containers
by running
```sh
$ docker rm $(docker ps -a -q)
$ docker ps -a
```
We can tell docker to remove container after it's stopped.
```sh
$ docker run --rm hello-world
$ docker ps -a
```

We will run the container with ubuntu LTS. We can specify the label for the
image we are interested in after `:` in this case `:14.04`.
```sh
$ docker run ubuntu:14.04
Unable to find image 'ubuntu:14.04' locally
14.04: Pulling from library/ubuntu
fcee8bcfe180: Pull complete
4cdc0cbc1936: Pull complete
d9e545b90db8: Pull complete
c4bea91afef3: Pull complete
Digest: sha256:098d121c6a9b39080f835563695f8e05faf765f46c174570e61d08197e82b820
Status: Downloaded newer image for ubuntu:14.04
```
This time the containers shuts down immediately after starting.
```sh
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS                          PORTS               NAMES
de742dcb2503        ubuntu:14.04        "/bin/bash"         About a minute ago   Exited (0) About a minute ago                       fervent_saha
```
We can start the container in interactive mode and attach to its terminal.
```sh
$ docker run -it ubuntu:14.04
root@2f4df153d302:/#
```
We are now inside running docker container.
```sh
root@2f4df153d302:/# lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 14.04.3 LTS
Release:	14.04
Codename:	trusty
```
exit the container with `exit` command.

## Deleting images
All downloaded image may take up space on your computer.
You can remove images with `docker rmi` command. Lets see
what kind of images we have:
```sh
$ docker images
ubuntu                  14.04               c4bea91afef3        2 weeks ago         187.9 MB
```
Now use image hash to remove it:
```sh
$ docker rmi c4bea91afef3
```
You will most probably need to remove a container that is based on this image
before you can remove the image itself.
