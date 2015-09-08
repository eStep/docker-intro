# Introducing `docker-compose` (former `fig`)
- used for running multi-container applications
- single file is used to define all inner workings of the application

## Lets build simple web app with [Flask](http://flask.pocoo.org/) and [Redis](http://redis.io/)
- lets crete the directory for our application

  ```bash
  # host
  mkdir composetest
  cd composetest
  ```

- simple web app in python using [Flask](http://flask.pocoo.org/)

  ```py
  # app.py
  from flask import Flask
  from redis import Redis
  
  app = Flask(__name__)
  redis = Redis(host='redis', port=6379)
  
  @app.route('/')
  def hello():
      redis.incr('hits')
      return 'Hello World! I have been seen %s times' % redis.get('hits')
  
  if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
  ```

- now we need to specify our python dependencies in `requirements.txt`

  ```text
  flask
  redis
  ```

- and the configuration of our container that the app will run in

  ```dockerfile
  # Dockerfile
  FROM python:2.7
  ADD . /code
  WORKDIR /code
  RUN pip install -r requirements.txt
  CMD python app.py
  ```

- try to build it

  ```bash
  docker build -t web .
  ```

- define compose configuration that combining elements together

  ```yml
  # docker-compose.yml
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

- now run it all

  ```bash
  docker-compose up
  ```
