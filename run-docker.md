When working with Docker it is important to understand the difference
between image and the container. As described in Docker documentation:

> **Docker images** are the basis of containers. An image is an ordered
> collection of root filesystem changes and the corresponding execution
> parameters for use whithin a container runtime. They are read only.


> **Container** is a runtime instance of a docker image.

We will start with running a container based on `hello-word` image.

```sh
docker run hello-world
```

When we run it 