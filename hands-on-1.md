This hands on is based on [Materials for Analyzing Next-Generation Sequencing (ANGUS) course.](https://github.com/ngs-docs/angus)

# Run Docker
- run simple ubuntu based container

```
docker run ubuntu:14.04
```

- the container has been created, but had nothing to do, so it shut down we can attach to running

  -i keep STDIN open

  -t allocate pseudo-tty

```
docker run -it ubuntu:14.04
```

- exit with `exit`
- if you run same command again, new ubuntu base container will be created

# Building Docker images
- we will build a Docker image for the MEGAHIT short read assembler ([http://angus.readthedocs.org/en/2015/assembling-ecoli.html%3E](http://angus.readthedocs.org/en/2015/assembling-ecoli.html%3E))
- start new container

```
docker run -it ubuntu:14.04
```

- install necessary dependencies (remember, you're already root)

```
apt-get update && apt-get install -y g++ make git zlib1g-dev python
```

- checkout and install megahit

```
git clone https://github.com/voutcn/megahit.git /home/megahit
cd /home/megahit && make
```

- we don't want to do it again, we want to keep this image for use

```
docker commit -m "build megahit" e82c6007f7a4 megahit
docker images
```

- we can now run it and use megahit

```
docker run -it megahit
/home/megahit/megahit
```

- later we'll put it in dockerhub so that no one ever has to do it again
- how do we get the data for analysis to the container?

# getting data to the container
- get data locally

```
mkdir data
cd data
wget http://public.ged.msu.edu.s3.amazonaws.com/ecoli_ref-5m-trim.se.fq.gz
wget http://public.ged.msu.edu.s3.amazonaws.com/ecoli_ref-5m-trim.pe.fq.gz
```

- run container and connect to local data directory

```
docker run -v ./data:/data -it megahit
ls /data
```

- lets run the assembly

```
/home/megahit/megahit --12 /data/*.pe.fq.gz \
                      -r /data/*.se.fq.gz \
                      -o /data/ecoli -t 4
```

- exit and look at analysis data

```
exit
ls data
ls data/ecoli
```

- we can run megahit command without entering the container like this

```
docker run -v ./data:/data \
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

```
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

```
docker build -t magahit .
```

- and run a container

```
docker run -v ./data/:/data -it megahit
```
