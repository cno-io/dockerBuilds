FROM ubuntu:16.04

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install python3
RUN apt-get update && apt-get -y install python3-pip
RUN apt-get update && apt-get -y install python-requests
RUN pip3 install google-api-python-client

COPY . /app

RUN chmod +x /app/*.py

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/app/iamServiceAccountsGetAccessToken.py"]
CMD []
