This hands on is based on [Materials for Analyzing Next-Generation Sequencing (ANGUS) course.](https://github.com/ngs-docs/angus)

# Run Docker
- run simple ubuntu based container

```bash
# host
docker run ubuntu:14.04
```

- list docker containers

```bash
# host
docker ps
docker ps -a
```

- the container has been created, but had nothing to do, so it shut down
- we can attach to the container (like ssh to the remote)

  -i keep STDIN open

  -t allocate pseudo-tty

```bash
# host
docker run -it ubuntu:14.04
```

- use second terminal window to list containers

```bash
# host
docker ps -a
```

- exit with `exit`
- if you run same command again, new ubuntu base container will be created
- you have to delete containers by hand, they will stack up very quickly,
- you can `docker run` with `-rm` flag to delete the container once it exits

```bash
# host
docker run --rm ubuntu:14.04
```

# Building Docker images
- we will build a Docker image for the MEGAHIT short read assembler ([http://angus.readthedocs.org/en/2015/assembling-ecoli.html%3E](http://angus.readthedocs.org/en/2015/assembling-ecoli.html%3E))
- start new container

```bash
# host
docker run -it ubuntu:14.04
```

- install necessary dependencies (remember, you're already root)

```bash
# in the container
apt-get update && apt-get install -y g++ make git zlib1g-dev python
```

- checkout and install megahit

```bash
# in the container
git clone https://github.com/voutcn/megahit.git /home/megahit
cd /home/megahit && make
```

- we don't want to do it again, we want to keep this image for use

```bash
# host
docker commit -m "build megahit" e82c6007f7a4 megahit
docker images
```

- we can now run it and use megahit

```bash
# host
docker run -it megahit

# in the container
/home/megahit/megahit
```

- later we'll put it in dockerhub so that no one ever has to do it again
- how do we get the data for analysis to the container?

# getting data to the container
- get data locally

```bash
# host
mkdir $HOME/data
cd $HOME/data
curl -O http://public.ged.msu.edu.s3.amazonaws.com/ecoli_ref-5m-trim.se.fq.gz
curl -O http://public.ged.msu.edu.s3.amazonaws.com/ecoli_ref-5m-trim.pe.fq.gz
```

- run container and connect to local data directory

```bash
# host
docker run -v $HOME/data:/data -it megahit

# in the container
ls /data
```

- lets run the assembly

```bash
# in the container
/home/megahit/megahit --12 /data/*.pe.fq.gz \
                      -r /data/*.se.fq.gz \
                      -o /data/ecoli -t 4
```

- exit and look at analysis data

```bash
# in the container
exit

# host
ls $HOME/data
ls $HOME/data/ecoli
```

- we can run megahit command without entering the container like this

```bash
# host
docker run -v $HOME/data:/data \
   -it megahit \
   sh -c '/home/megahit/megahit --12 /data/*.pe.fq.gz
                     -r /data/*.se.fq.gz
                     -o /data/ecoli -t 4'
```

- we could also put the command in the script and run the script `do-assemble.sh`

```
#! /bin/bash
rm -fr /data/ecoli
/home/megahit/megahit --12 /data/*.pe.fq.gz \
                      -r /data/*.se.fq.gz  \
                      -o /data/ecoli -t 4
```

```bash
# host
chmod +x do-assemble.sh
```

# building with Dockerfile

```
FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y g++ make git zlib1g-dev python
RUN git clone https://github.com/voutcn/megahit.git /home/megahit
RUN cd /home/megahit && make
CMD /data/do-assemble.sh
```

- we will now build and image based on the Dockerfile

```bash
# host
docker build -t magahit .
```

- and run a container

```bash
# host
docker run -v $HOME/data/:/data -it megahit
```
