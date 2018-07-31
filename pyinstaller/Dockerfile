FROM ubuntu:16.04

MAINTAINER TweekFawkes

# RUN mkdir /app
# WORKDIR /app

RUN apt-get update && apt-get -y install python
RUN apt-get update && apt-get -y install python-pip
RUN apt-get update && apt-get -y install python-requests
# RUN apt-get update && apt-get -y install wget

RUN pip install pyinstaller

# COPY . /app

# RUN chmod +x /app/*.py

RUN mkdir /shared
WORKDIR /shared
VOLUME ["/shared"]

ENTRYPOINT ["/usr/local/bin/pyinstaller"]
CMD []
