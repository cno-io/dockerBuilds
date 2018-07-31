FROM ubuntu:16.04

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install software-properties-common python-software-properties
RUN apt-get update && add-apt-repository -y ppa:gophers/archive
RUN apt-get update && apt-get -y install golang-1.10-go
RUN apt-get update && apt-get -y install git

RUN /usr/lib/go-1.10/bin/go get -u github.com/cno-io/gobuster

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/root/go/bin/gobuster"]
CMD []
