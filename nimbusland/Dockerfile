FROM ubuntu:16.04

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install python
RUN apt-get update && apt-get -y install python-pip
RUN apt-get update && apt-get -y install python-requests
RUN apt-get update && apt-get -y install wget

RUN pip install netaddr
RUN pip install setuptools
RUN pip install pyOpenSSL
RUN pip install 'requests[security]'

RUN wget --no-check-certificate https://gist.githubusercontent.com/cno-io/3182fbbab77bbd87fe656666e8166bfc/raw/a44105300a33b1f26989896b8bb4c62af6503d19/nimbusland-v0_0_7.py

COPY . /app

RUN chmod +x /app/*.py

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/app/nimbusland-v0_0_7.py"]
CMD []
