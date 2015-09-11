# Doker's powerfull functionalities

---

# runs on your machine -> runs on others
- portable deployment across the machines
- environment needed for your application to run comes with the container
- 'if it works on your machine, it will work on others too'
---

# runs on your machine -> runs in production

---

# application centric
- Docker is optimized for deployment of applications, not machines or systems

---

# automated builds
- use `docker build` do build an image based on `Dockerfile`
- automated building on DockerHub after pushing to git repository

---

# versioning
- docker tracks all changes in successive versions of the container
- it is possible to commit, dif and roll back
- like git, docker uses incremental uploads and downloads, so only diff is send

---

# component re-use
- any image can be used as a base for another image
- you can build one generic image and then multiple specialized versions of that one

---

# sharing
- public registry [Docker Hub](https://hub.docker.com/) with images uploaded by other people
- you can see `Dockerfile` for each container
- _official_ containers maintained by Docker team

---

# tool ecosystem
- deployment: [Dokku](http://progrium.viewdocs.io/dokku/), [Deis](http://deis.io/), [Flynn](https://flynn.io/) ...
- multinode orchestration: [Maestro](https://github.com/toscanini/maestro), [Salt](http://saltstack.com/), [Mesos](https://mesos.apache.org/), [OpenStack Nova](http://docs.openstack.org/developer/nova/) ...
- dashboards: [docker-ui](https://github.com/crosbymichael/dockerui), [Openstack Horizon](http://docs.openstack.org/developer/horizon/), [Shipyard](https://shipyard-project.com/) ...
- configuration managements: [Chef](https://www.chef.io/chef/), [Puppet](https://puppetlabs.com/), [Ansible](http://www.ansible.com/home) ...
- continuous integration: [Jenkins](https://jenkins-ci.org/), [Strider](https://github.com/Strider-CD/strider), [Travis](https://travis-ci.org/) ...

---

# Use cases in Bioinformatics
## making bioinformatics tools/pipelines easy to deploy on any infrastructure
> you start developing a tool on your laptop, then you move it to the cloud (ubuntu) for some more serious analysis, but after a month you want ot put it on the local cluster (CentOS) for production use

---

# making it work for others
> you already use git (and maybe github) for version control and collaboration in your team, you would like to do the same with deployment, to know that if it worked on your machine, when you pushed the changes, it will work on your colleges machine when he pulls them

---

# making it work for people who read you paper
> it's great if you can point in the paper to a git commit relevant to publication, but that does not guarantee that they can install and run it, with docker you can point them to particular commit for the image and be sure they can run it anywhere they need to, you can even make whole paper reproducible

### Example:

Bremges, A., Maus, I., Belmann, P., Eikmeyer, F., Winkler, A., Albersmeier, A., Puhler, A., Schluter, A., Sczyrba, A.: (2015) Deeply sequenced metagenome and metatranscriptome of a biogas-producing microbial community from an agricultural production-scale biogas plant.GigaScience 4:33 doi:10.1186/s13742-015-0073-6 [Docker accessible version of the study](https://registry.hub.docker.com/u/metagenomics/2015-biogas-cebitec/)

---

# don't install anything twice
> if you're installing a new aligner that you want to try, put it in a container, so that when you need it in the cloud or on the cluster you don't have to install it again

- tool in a box
  - [biodocker](https://github.com/BioDocker)
  - [bioboxes](https://github.com/bioboxes)

- analysis environment in a box
  - [Rocker](https://github.com/rocker-org)
  - [docker-bio-linux](https://hub.docker.com/r/gawbul/docker-bio-linux8/)

---

# performance
> Docker containerization has a negligible impact on the execution performance of common genomic pipelines where tasks are generally very time consuming. The minimal performance loss introduced by the Docker engine is offset by the advantages of running an analysis in a self-contained and precisely controlled runtime environment. Docker makes it easy to precisely prototype an environment, maintain all its variations over time and rapidly reproduce any former configuration one may need to re-use. These capacities guarantee consistent results over time and across different computing platforms.

The impact of Docker containers on the performance of genomic pipelines [https://dx.doi.org/10.7287/peerj.preprints.1171v2](https://dx.doi.org/10.7287/peerj.preprints.1171v2)

---

# others on Docker?
- Brad Chapman [Improving reproducibility and installation of genomic analysis pipelines with docker](http://bcb.io/2014/03/06/improving-reproducibility-and-installation-of-genomic-analysis-pipelines-with-docker/)
- Titus Brown [Adventures in replicable scientific papers: Docker](http://ivory.idyll.org/blog//2015-docker-and-replicating-papers.html)
- Heng Li [A few hours with docker](https://lh3.github.io/2015/04/25/a-few-hours-with-docker/)
- Carl Boettiger [An introduction to Docker for reproducible research, with examples from the R environment](http://arxiv.org/abs/1410.0846)

---

# other interesting posts
- [docker-helps-biofuels-research](http://www.software.ac.uk/blog/2015-07-30-docker-helps-biofuels-research)
- [Reproducible research for biofuels and biogas](http://www.eurekalert.org/pub_releases/2015-07/g-rrf072715.php)
- [Docker-based solutions to reproducibility in science](http://blog.sbgenomics.com/docker-based-solutions-to-reproducibility-in-science/)
- [BioDocker and BioBoxes: the containerization of bioinformatics](http://www.acgt.me/blog/2015/8/25/biodocker-and-bioboxes-the-containerization-of-bioinformatics)
- [Using docker for reproducible computational publications](http://melissagymrek.com/science/2014/08/29/docker-reproducible-research.html)
- [Updates on docker and bioinformatics](http://bioinfoblog.it/2015/03/updates-on-docker-and-bioinformatics/)

---

# other intersting Docker based projects:
- [Rabix - Portable Bioinformatics Pipelines from Seven Bridges Genomics](https://www.rabix.org)
- [oswitch](https://github.com/wurmlab/oswitch)
- [nextflow](http://www.nextflow.io/)

---

see this as a slideshow [here](https://gnab.github.io/remark/remarkise?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmkuzak%2Fshipcamel%2Fmaster%2FDocker-use-cases.md#1)
