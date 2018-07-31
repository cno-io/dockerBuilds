FROM ubuntu:16.04

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install python
# RUN apt-get update && apt-get -y install python-pip
# RUN apt-get update && apt-get -y install python-requests
RUN apt-get update && apt-get -y install wget

# RUN pip install netaddr
# RUN pip install setuptools
# RUN pip install pyOpenSSL
# RUN pip install 'requests[security]'

RUN wget --no-check-certificate https://gist.githubusercontent.com/cno-io/0fc1a60a996d256f747f08084df90bd2/raw/944f861166c84109a2e8c287d5a97a21b23eae33/mintyOffline-v0_0_4.py

COPY . /app

RUN chmod +x /app/*.py

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/app/mintyOffline-v0_0_4.py"]
CMD []
