FROM node:6
# FROM node:6
# FROM node:8

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

#RUN apt-get update && apt-get -y install apt-transport-https
#RUN apt-get update && apt-get -y install build-essential
#RUN apt-get update && apt-get -y install curl
#RUN apt-get update && apt-get -y install ca-certificates
#RUN apt-get update && apt-get -y install git
#RUN apt-get update && apt-get -y install lsb-release
#RUN apt-get update && apt-get -y install python-all
#RUN apt-get update && apt-get -y install rlwrap
#RUN apt-get update && apt-get -y install vim
#RUN apt-get update && apt-get -y install nano
#RUN apt-get update && apt-get -y install jq

RUN npm install --global azure-cli@0.10.17

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN azure config mode arm
ENV EDITOR vim

RUN mkdir /shared
VOLUME ["/shared"]
