FROM node:8

MAINTAINER TweekFawkes

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

RUN mkdir /shared
VOLUME ["/shared"]

EXPOSE 8080
CMD nodejs /usr/src/app/index.js -s
