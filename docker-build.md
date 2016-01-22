# Building docker images

## Simple Flask application
First we will learn to run simple Flask application in a container.

```py
#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/hi')
def hello_world():
    return 'Hello World!'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Here are the steps that we need to make to achieve this:
* install python and flask
* get aour script into the container
* acess locally flask application served from inside the container

Assuming the `hello.py` script with our flask app  is in `./app`
directory, we can mount it inside the container with `-v` flag.

```sh
$docker run -v $PWD/app:/app
```

We also need to expose port `5000` from the container to our host.
We can do it with `-p` flag.

```sh
$docker run -p 5000 ubuntu:14.04
```

Let us add this all up:
```sh
$ docker run -it -v $PWD/app:/app/ -p 5000 ubuntu:14.04
root@11e2c4d5b385:/# apt-get update
root@11e2c4d5b385:/# apt-get install -y python python-pip
root@11e2c4d5b385:/# pip install flask
root@11e2c4d5b385:/# cd /app
root@11e2c4d5b385:app/# chmod +x hello.py
root@11e2c4d5b385:app/# ./hello.py
```

We want to see the flask application via a web browser on local machine.
To do that we need to know:
* on what ip adress we can connect to the vm in which the container
  is running?
* which port have been bound to port 5000 on the container

```sh
$ docker-machine ip dev
192.168.99.100
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                     NAMES
11e2c4d5b385        ubuntu:14.04        "/bin/bash"         24 minutes ago      Up 24 minutes       0.0.0.0:32768->5000/tcp   sick_swirles
```

Remember our flask app serves hellos on at `/hi` root, so we should be access
it at
```sh
http://192.168.99.100:32768/hi
```

## Building from with Dockerfile

This is great, but it's a lot of work and bookkeeping. We will learn how to
document and `script` this process. We will also build an image based on
the requirements so that we can quickly start it when ever we need to.

We will create a file called `Dockerfile` in which we tell `docker` how to
build an image for us.

```Dockerfile
FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y python python-pip
RUN pip install flask
ADD $PWD/app /app

WORKDIR /app
EXPOSE 5000
CMD python hello.py
```

Lets explain what is happening:
* `FROM` defines the `base` image we want to use
* `RUN` will run a command in shell inside the container
* `ADD` will copy files from local into the container,
  the first path is relative to Dockerfile location,
  second is relative to root in the container
* `WORKDIR` will set the working directory inside the container
* `EXPOSE` will expose the port in the container to the outside
* `CMD` is the default command when running the container

Now we are going to build this iamge.

```sh
$ docker build -t flask .
```
We are labelling the image `flask` by using `-t` flag.
We tell docker to look for Docker file in current working directory `.` . 

```sh
$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
flask                   latest              86b0a35f9fa6        6 seconds ago       358.4 MB
```

Now we can run it.

```sh
$ docker run -d -P flask
```

We bind the ports with `-P` and run the container as a daemon,
in the background with `-d`.

```sh
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                     NAMES
20f2420ef0f4        flask               "python /app/hello.py"   2 seconds ago       Up 1 seconds        0.0.0.0:32770->5000/tcp   stupefied_yonath
```

We see the flask app can be accessed on port `32770`.
That means we should see it at:
```
http://192.168.99.100:32770/hi
```