# PASS
## [Deis](http://deis.io/)
Deis (pronounced DAY-iss) is an open source PaaS that makes it easy to deploy and manage applications on your own servers. Deis builds upon Docker and CoreOS to provide a lightweight PaaS with a Heroku-inspired workflow.

## [Dokku](https://github.com/progrium/dokku)
Docker powered mini-Heroku in around 100 lines of Bash.

## [Flynn](https://flynn.io/)
Flynn deploys apps, scales apps, and manages databases.

## [Tsuru](https://tsuru.io/)
Tsuru is an open source PaaS that makes it easy and fast to deploy and manage applications on your own servers.

## [Octohost](http://www.octohost.io/)
Simple web focused Docker based mini-PaaS server. git push to deploy your websites as needed.

## [Panamax](http://panamax.io/)
Panamax is a containerized app creator with an open-source app marketplace hosted in GitHub. Panamax provides a friendly interface for users of Docker, Fleet & CoreOS.

# Service Discovery
Service discovery is used so that containers can find out about the environment they have been introduced to without administrator intervention. They can find connection information for the components they must interact with, and they can register themselves so that other tools know that they are available.

## [etcd](https://coreos.com/etcd/)
Service discovery / globally distributed key-value store by CoreOS. It implements an http API and has a command line client available on each host machine.

## [consul](https://www.consul.io/)
Service discovery / globally distributed key-value store by hashicorp. It has many advanced features that make it stand out including configurable health checks, [ACL functionality](https://www.consul.io/docs/internals/acl.html), [HAProxy configuration](https://hashicorp.com/blog/haproxy-with-consul.html), etc.

## [zookeeper](https://zookeeper.apache.org/)
Service discovery / globally distributed key-value store by Apache Foudation. More mature platform, missing some newer features.

## [crypt](https://xordataexchange.github.io/crypt/)
Crypt allows components to protect the information they write using public key encryption. The components that are meant to read the data can be given the decryption key. All other parties will be unable to read the data.

## [confd](http://www.confd.io/)
Confd is a project aimed at allowing dynamic reconfiguration of arbitrary applications based on changes in the service discovery portal. The system involves a tool to watch relevant endpoints for changes, a templating system to build new configuration files based on the information gathered, and the ability to reload affected applications.

## [marathon](https://github.com/mesosphere/marathon)
While marathon is mainly a scheduler, it also implements a basic ability to reload HAProxy when changes are made to the available services it should be balancing between.

## [vulcand](https://github.com/mailgun/vulcand)
Vulcand serves as a load balancer for groups of components. It is etcd aware and modifies its configuration based on changes detected in the store.

## [synapse](https://github.com/airbnb/synapse)
This project from Airbnb introduces an embedded HAProxy instance that can route traffic to components.

## [nerve](https://github.com/airbnb/nerve)
Nerve, also from Airbnb, is used in conjunction with synapse to provide health checks for individual component instances. If the component becomes unavailable, nerve updates synapse to bring the component out of rotation.

# Networking
## [flannel](https://github.com/coreos/flannel)
Flannel is a virtual network that gives a subnet to each host for use with container runtimes.

## [Weave](https://github.com/weaveworks/weave)
Weave creates a virtual network that connects Docker containers deployed across multiple hosts and enables their automatic discovery.

## [Pipework](https://github.com/jpetazzo/pipework)
Pipework lets you connect together containers in arbitrarily complex scenarios. Pipework uses cgroups and namespace and works with "plain" LXC containers (created with lxc-start), and with the Docker.

# Orchestration (scheduling, cluster management, provisioning)
**Cluster management**: controlling a group of hosts

**Scheduling**: loading services on the host system by hooking into host init system or _cluster-wide_ init system

## [fleet](https://github.com/coreos/fleet https://coreos.com/using-coreos/clustering/)
Fleet is the scheduling and cluster management component of CoreOS. It reads connection info for each host in the cluster from etcd and provides systemd-like service management.

## [marathon](https://github.com/mesosphere/marathon)
Marathon is the scheduling and service management component of a Mesosphere installation. It works with mesos to control long-running services and provides a web UIfor process and container management.

## [swarm](https://docs.docker.com/swarm/)
Swarm is a scheduler by Docker team. It hopes to provide a robust scheduler that can spin up containers on hosts provisioned with Docker, using Docker-native syntax.

## [mesos](https://mesos.apache.org/)
Apache mesos is a tool that abstracts and manages the resources of all hosts in a cluster. It presents a collection of the resources available throughout the entire cluster to the components built on top of it (like marathon). It describes itself as analogous to a "kernel" for a clustered configurations.

## [kubernetes](http://kubernetes.io/)
Google's advanced scheduler, kubernetes allows much more control over the containers running on the infrastructure. Containers can be labeled, grouped, and given their own subnet for communication.

## [compse](https://docs.docker.com/compose/)
Docker's compose project was created to allow group management of containers using declarative configuration files. It uses Docker links to learn about the dependency relationship between containers.

## [Helios](https://github.com/spotify/helios)
Helios is a Docker orchestration platform for deploying and managing containers across an entire fleet of servers, developed by Spotify.

# Monitoring and management
## [Shipyard](http://shipyard-project.com/)
Built on Docker Swarm, Shipyard gives you the ability to manage Docker resources including containers images, private registries and more.

## [Prometheus](http://prometheus.io/)
Prometheus is an open-source systems monitoring and alerting toolkit.

# More
## [Surf](https://www.serfdom.io/)
Surf is a decentralized solution for cluster membership, failure detection and orchestration.

## [logspout](https://github.com/gliderlabs/logspout)
Log routing for Docker container logs.

## [Flocker](https://github.com/ClusterHQ/flocker)
Flocker is an open-source Container Data Volume Manager for Dockerized applications.

Above notes have been in large extent based on [The Docker Ecosystem](https://www.digitalocean.com/community/tutorials/the-docker-ecosystem-an-introduction-to-common-components)  by [Justin Ellingwood](https://twitter.com/jmellingwood) @ [DigitalOcean](https://twitter.com/DigitalOcean).
