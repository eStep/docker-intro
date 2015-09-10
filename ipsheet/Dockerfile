FROM python:2.7
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
WORKDIR /ipsheet
ENTRYPOINT ["python", "/ipsheet/ipsheet.py"]
