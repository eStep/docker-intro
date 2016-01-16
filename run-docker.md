When working with Docker it is important to understand the difference
between image and the container. As described in Docker documentation:

> **Docker images** are the basis of containers. An image is an ordered
> collection of root filesystem changes and the corresponding execution
> parameters for use whithin a container runtime. They are read only.


> **Container** is a runtime instance of a docker image.

We will start with running a container based on `hello-word` image.

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
* check to `hello-world` image is available locally
* download the image (from Docker Hub) if needed
* load the image into the container and run it

This container does not do much it outputs the message you see and shuts down.
Lets list all running containers.
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
has been instantiated based on.
```sh
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
hello-world         latest              0a6ba66e537a        3 months ago        960 B
```