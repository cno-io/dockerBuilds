FROM ubuntu:16.04

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install python
RUN apt-get update && apt-get -y install python-pip
RUN apt-get update && apt-get -y install python-dev
RUN apt-get update && apt-get -y install build-essential

RUN pip install Flask
RUN pip install lxml

COPY . /app

RUN chmod +x /app/*.py

RUN mv /app/.fog /root/.fog
RUN chmod 777 /root/.fog

RUN mkdir /shared
VOLUME ["/shared"]

EXPOSE 8081

ENTRYPOINT flask run --host=0.0.0.0 --port 8081
CMD []
