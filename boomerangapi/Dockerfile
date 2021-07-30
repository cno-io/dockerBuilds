FROM ubuntu:18.04

MAINTAINER TweekFawkes

RUN mkdir /app
WORKDIR /app

#RUN apt-get update && apt-get -y install python

#RUN apt-get update && apt-get -y install software-properties-common
#RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get -y install python3
RUN apt-get update && apt-get -y install python3-pip

#RUN apt-get update && apt-get -y install python-pip
#RUN apt-get update && apt-get -y install python-requests
#RUN apt-get update && apt-get -y install wget
#RUN apt-get update && apt-get -y install git
#RUN apt-get update && apt-get -y install graphviz
#RUN apt-get update && apt-get -y install git
#RUN apt-get update && apt-get -y install python-tk

#RUN apt-get update && apt-get -y install libsqlite3-dev

#RUN apt-get update && apt-get -y install libssl-dev
#RUN apt-get update && apt-get -y install build-essential
#RUN apt-get update && apt-get -y install python3-dev
#RUN apt-get update && apt-get -y install libffi-dev
#RUN apt-get update && apt-get -y install zlib1g-dev
#RUN apt-get update && apt-get -y install libxml2
#RUN apt-get update && apt-get -y install libxml2-dev
#RUN apt-get update && apt-get -y install libxslt1-dev

#RUN pip install pydot
# RUN pip install setuptools
# RUN pip install pyOpenSSL
# RUN pip install 'requests[security]'

RUN pip3 install boto3

# RUN wget --no-check-certificate https://gist.githubusercontent.com/cno-io/3182fbbab77bbd87fe656666e8166bfc/raw/a44105300a33b1f26989896b8bb4c62af6503d19/nimbusland-v0_0_7.py

COPY . /app

# RUN git clone https://github.com/cno-io/aws-inventory.git
#WORKDIR /app/voodoo-ce
#RUN pip3 install -r requirements.txt
# RUN pip3 install -r requirements.txt
RUN chmod +x /app/*.py
# RUN python3 create_dbs.py

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/usr/bin/python3", "/app/boomerangApi-v0_3.py"]
CMD []