FROM ubuntu:16.04

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install python
RUN apt-get update && apt-get -y install python-pip
RUN apt-get update && apt-get -y install python-dev
RUN apt-get update && apt-get -y install build-essential
RUN apt-get update && apt-get -y install net-tools
RUN apt-get update && apt-get -y install iputils-ping

RUN pip install Flask

COPY . /app

RUN chmod +x /app/*.py

RUN mkdir /shared
VOLUME ["/shared"]

EXPOSE 5001

ENTRYPOINT flask run --host=0.0.0.0 --port 5001
CMD []
