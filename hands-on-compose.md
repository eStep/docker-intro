# Introducing `docker-compose` (former `fig`)
- used for running multi-container applications
- single file is used to define all inner workings of the application

## Lets build simple web app with [Flask](http://flask.pocoo.org/) and [Redis](http://redis.io/)
- Check that docker-compose is [installed](https://docs.docker.com/compose/install/)  

  ```bash
  # host
  docker-compose --version
  ```

- lets create the directory for our application

  ```bash
  # host
  mkdir composetest
  cd composetest
  mkdir code
  ```

- code simple web app in python using [Flask](http://flask.pocoo.org/) in `code/app.py`
  ```py
  # file code/app.py

  from flask import Flask
  from redis import Redis
  from urlparse import urlparse
  import sys, os

  # extract the connection to redis from environment variable
  up = urlparse(os.environ['REDIS_PORT'])
  print >> sys.stderr, 'connecting to redis at %s:%s' % (up.hostname, up.port)

  # connect to redis
  redis = Redis(host=up.hostname, port=up.port)

  # create flask instancw
  app = Flask(__name__)

  # callback to reply to root url
  @app.route('/')
  def hello():
      redis.incr('hits')
      return 'Hi, you are visitor nr %s.' % redis.get('hits')

  # main: run flask
  if __name__ == "__main__":
      app.run(host="0.0.0.0", debug=True)
  ```

- specify the python dependencies for the web app in `code/requirements.txt`

  ```text
  flask
  redis
  ```

- the configuration of the web app container goes in `Dockerfile`

  ```dockerfile
  # Dockerfile
  FROM python:2.7
  ADD ./code /code
  RUN pip install -r /code/requirements.txt
  CMD python /code/app.py
  ```

- define compose configuration that combining elements together

  ```yml
  # docker-compose.yml
  web:
    build: .
    ports:
     - "5000"
    volumes:
     - ./code:/code
    links:
     - redis
    command: python /code/app.py

  redis:
    image: redis
  ```

- now run it all

  ```bash
  # host, in composetest
  docker-compose up
  ```

- in another terminal, get some information about your servers
  ```bash
  # host, in composetest
  docker-compose ps
  ```

- find the external port for the web app
  ```bash
  # host, in composetest
  docker-compose port web 5000
  ```

- direct your browser to the IP address of your host and use the proper port


- or in your terminal
 ```bash
  # host
  curl localhost:[port]
  ```
