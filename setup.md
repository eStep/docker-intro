# Software Setup

The goal of this workshop is to understand the basics of `docker`. In order to
do it we need to setup few `docker` tools. This tutorial expects that you are
working with linux operating system, either one running directly on your computer
a linux vm inside VirtualBox or other virtualisation software.

For *Multi Container Applications* lesson you will need to install `docker-compose`.

Advanced users can learn from last lesson, *Introduction to `docker-machine`*, how to
execute docker command on remote machines.

Before installing it's worth checking your linux distribution and architecture.
Keep in mind that you cannot install `docker engine` on 32 bit operating system.

```sh
# to learn about the distribution
$ lsb_release -dc
# to learn about architecture
$ arch
```

## docker engine
Please follow instructions relevant for your linux distribution on
[Docker documentation page](https://docs.docker.com/engine/installation/).

## `docker-compose`
Install by following instructions on
[Docker documentation page ](https://docs.docker.com/compose/install/).

## `docker-machine`
Install by following instructions on
[Docker documentation page](https://docs.docker.com/machine/install-machine/).