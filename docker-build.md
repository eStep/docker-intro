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

Assuming the `hello.py` script with our flask app  is in `./code`
directory, we can mount it inside the container with `-v` flag.

```sh
$docker run -v $PWD/code:/code
```

We also need to expose port `5000` from the container to our host.
We can do it with `-p` flag.

```sh
$docker run -p 5000 ubuntu:14.04
```

Let us add this all up:
```sh
$ docker run -it -v $PWD/code:/code/ -p 5000 ubuntu:14.04
root@11e2c4d5b385:/# apt-get update
root@11e2c4d5b385:/# apt-get install -y python python-pip
root@11e2c4d5b385:/# pip install flask
root@11e2c4d5b385:/# cd /code
root@11e2c4d5b385:code/# chmod +x hello.py
root@11e2c4d5b385:code/# ./hello.py
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

Remember our flask app serves hellos on at `/hi` root, so we shold be access
it at
```sh
http://192.168.99.100:32768/hi
```