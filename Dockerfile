FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y python python-pip

RUN pip install flask

ADD app/hello.py /app/hello.py

EXPOSE 5000
CMD ["python", "/app/hello.py"]