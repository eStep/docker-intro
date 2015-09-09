FROM python:2.7
ADD . /ipsheet
WORKDIR /ipsheet
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "/ipsheet/ipsheet.py"]
