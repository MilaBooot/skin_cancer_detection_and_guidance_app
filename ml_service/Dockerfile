FROM python:3.6.8

RUN mkdir -p /usr/src/ml_api/
COPY requirements.txt /usr/src/ml_api/

WORKDIR /usr/src/ml_api/
RUN pip install -r requirements.txt

COPY . /usr/src/ml_api

ENTRYPOINT ["python", "application.py"]
EXPOSE 5001
