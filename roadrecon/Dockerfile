FROM ubuntu:20.04

LABEL MAINTAINER="TTL_0"

RUN apt-get update && apt-get -y install python3 python3-pip
RUN pip3 install roadrecon

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/usr/local/bin/roadrecon"]
CMD []