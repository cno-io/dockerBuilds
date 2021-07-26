FROM ubuntu:20.04

LABEL MAINTAINER="TTL_0"

RUN apt-get update && apt-get -y install python3 python3-pip
RUN pip3 install roadrecon

RUN sed -i "s#app.run(debug=args.debug)#app.run(debug=args.debug, host='0.0.0.0')#" /usr/local/lib/python3.8/dist-packages/roadtools/roadrecon/server.py

RUN mkdir /shared
VOLUME ["/shared"]

ENTRYPOINT ["/usr/local/bin/roadrecon"]
CMD []
