# Multi-container Applications with Compose

`docker-compose` is a tool used for defining and running multi-container
applications.
To use `compose` we have to:
* create Dockerfile with description for each service 
* create `docker-compose.yml` file with description of how different services
  come together
* run `docker-compose up` to start the whole application

We're going to modify our flask app so that it keeps all visits to the
website. We will store number of visits in redis store.

```python
#!/usr/bin/env python

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times' % redis.get('hits')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

We will define python dependencies in `requirements.txt`
```txt
flask
redis
```

Description of flask image goues into new Dckerfile
```Dockerfile
FROM python:2.7
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "hello-counter.py"]
```

This time our starting image is `ptyhon:2.7` intstead of `ubuntu`, this way
we avoid installing python and can move immediately to installing python modules.

We're now going to build the image like we did before
```sh
$ docker build -t web ./compose-flask
$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
web                     latest              1b11b4e28507        6 seconds ago       682.7 MB
```

We will use `docker-compose.yml` to define our microservices:
```yml
web:
  build: .
  ports:
   - "5000:5000"
  volumes:
   - .:/code
  links:
   - redis
redis:
  image: redis
```

It defines `web` container which:
* is built from `Docerfile` in same directory
* binds `port 5000` in the container to `port 5000` on the host
* mounts `cwd` as `/code` inside the container
* links to other container called `redis`

It also defines `redis` container that will be buld from `redis` official
image.

```sh
$ docker-compose up
$ docker-compose ps
        Name                      Command               State           Ports
--------------------------------------------------------------------------------------
composeflask_redis_1   /entrypoint.sh redis-server      Up      6379/tcp
composeflask_web_1     /bin/sh -c python hello-co ...   Up      0.0.0.0:5000->5000/tcp
    
```