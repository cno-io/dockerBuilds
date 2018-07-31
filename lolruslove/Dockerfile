FROM ubuntu:16.04

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install python
RUN apt-get update && apt-get -y install python-pip
RUN apt-get update && apt-get -y install python-requests
RUN apt-get update && apt-get -y install wget
RUN apt-get update && apt-get -y install libssl-dev

RUN pip install netaddr
RUN pip install setuptools
RUN pip install pyOpenSSL
RUN pip install 'requests[security]'
RUN pip install scrapy
RUN pip install enum34
RUN pip install cryptography
RUN pip install dnspython
RUN pip install pyopenssl --upgrade

RUN wget --no-check-certificate https://gist.githubusercontent.com/cno-io/01462d2f5c7d810dd4ddd3b0099d1948/raw/4277c11c9a43e4d905c4a8fbd9a4e2b7141c320d/lolruslove-v0_0_7.py

COPY . /app

RUN chmod +x /app/*.py

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/app/lolruslove-v0_0_7.py"]
CMD []
