FROM ubuntu:16.04

LABEL MAINTAINER="TTL_0"

RUN apt-get update && apt-get -y install python python-requests
ADD https://raw.githubusercontent.com/anthonyhendricksS2/o365creeper/master/o365creeper.py /o365creeper.py

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/usr/bin/python", "o365creeper.py"]
CMD []