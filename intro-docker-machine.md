`Docker-machine` allows you to provision Docker running on virtual machine
on your local system or remote cloud. We will use `docker-machine` to create
vm and run docker containers inside it as it would run on our local machine.

# Creating a machine in VirtualBox
We can access information about available on our system machines

```sh
$ docker-machine ls
NAME   ACTIVE   URL          STATE     URL   SWARM   DOCKER    ERRORS
```

We see that we don't have any machines at the beginning. We have to create
one.

```sh
$ docker-machine create --drive virtualbox dev
Running pre-create checks...
Creating machine...
(default) Copying 
(default) Creating VirtualBox VM...
(default) Creating SSH key...
(default) Starting the VM...
(default) Waiting for an IP...
Waiting for machine to be running, this may take a few minutes...
Machine is running, waiting for SSH to be available...
Detecting operating system of created instance...
Detecting the provisioner...
Provisioning with boot2docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
To see how to connect Docker to this machine, run: docker-machine env dev
```

That way we've created a machine from boot2docker iso, named dev running in
our VirualBox installation.

```sh
$ docker-machine ls
NAME      ACTIVE   URL          STATE     URL                         SWARM   DOCKER    ERRORS
dev       -        virtualbox   Running   tcp://192.168.99.100:2376           v1.9.1
```

To be able to connect ot this machine we have to export some environmental
variables.

```sh
$ eval "$(docker-machine env dev)"
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
$ docker-machine env dev
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/<user>/.docker/machine/machines/dev"
export DOCKER_MACHINE_NAME="dev"
# Run this command to configure your shell:
# eval $(docker-machine env dev)
```
Now we can run docker containers in VirtualBox like we would locally.
We will learn about running containers in [next lesson](running-docker-containers.md)  