The goal of this workshop is to understand the basics of `docker`. In order to
do it we need to setup few `docker` tools. 

For the entire workshop, independent of the operating system, we will be using
`docker-machine`. It will let us setup host (in our case vm in virualbox)
and configure docker client to talk to it. You will learn more about
`docker-machine` during the workshop. There is no need for creating new virtual machine
inside VirtualBox before start of the workshop.

Last lesson shows how to define and run multi-container applications with `docker-compose`.

Following are the instructions to setup `docker-machine` on your computer.


## Windows
On Windows, the simplest way to setup `Docker`, `docker-machine` and `docker-compose` is
is to use [Docker Toolbox](https://www.docker.com/docker-toolbox).

* Download an installer from
[Docker Toolbox page](https://www.docker.com/docker-toolbox)

* Follow
[installation instructions for windows](https://docs.docker.com/windows/step_one/)

## Mac OS X
On Mac, the sipmlest way to setup `Docker`, `docker-machine` and `docker-compose`
is to use [Docker Toolbox](https://www.docker.com/docker-toolbox).

* Download an installer from
[Docker Toolbox page](https://www.docker.com/docker-toolbox)

* Follow
[installation instructions for windows](https://docs.docker.com/mac/step_one/)

## Linux
Make sure you have 64 bit linux version. You cannot run `docker-engine` on
32 bit linux. If you are not sure which version of Linux you have available
on your computer you can check it with following commands
```sh
# to learn about the distribution
$ lsb_release -dc
# to learn about architecture
$ arch
```

Even though docker can be installed in most linux distributions with a package
manager, we recommend using VirtualBox and `docker-machine`.

* VirtualBox
    
    Our docker host will be running in the virtualbox and all docker contaiers
    will be running on this host. `docker-machine` will help us with the setup
    and talking to this host.
    
    Even if you have VirtualBox installed try to install the latest version.
    There have been a lot of changes to VB recently that make it play better
    with docker. Latest VirtualBox version at the time of writing this tutorial
    is `5.0.14`

    Download and install VirtualBox from
    [Oracle website](https://www.virtualbox.org/wiki/Linux_Downloads)
    
* `docker-engine`

    Install by following instructions on
    [Docker documentation](https://docs.docker.com/engine/installation/).
    
* `docker-machine`
   
    Install by following instructions on
    [Docker documentation](https://docs.docker.com/machine/install-machine/).
    
* `docker-compose`

    Install by following instructions on
    [Docker documentation](https://docs.docker.com/compose/install/).
    
Check if all docker tools are installed on your computer.
```sh
$ docker-machine --version
docker-machine version 0.5.6, build 61388e9
$ docker-compose --version
docker-compose version: 1.5.0
```
