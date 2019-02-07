FROM ubuntu:16.04

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install python
RUN apt-get update && apt-get -y install python-pip
RUN apt-get update && apt-get -y install python-dev
RUN apt-get update && apt-get -y install build-essential

RUN pip install Flask

COPY . /app

RUN chmod +x /app/*.py

RUN mv /app/.s3cfg /root/.s3cfg
RUN chmod 777 /root/.s3cfg

RUN mkdir /shared
VOLUME ["/shared"]

EXPOSE 8000

ENTRYPOINT flask run --host=0.0.0.0 --port 8000
CMD []
