FROM python:3.8-alpine as compile

LABEL MAINTAINER="TTL_0"

WORKDIR /opt

RUN apk add --no-cache git gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN python3 -m pip install virtualenv
RUN virtualenv -p python venv
ENV PATH="/opt/venv/bin:$PATH"
RUN git clone --depth 1 https://github.com/anthonyhendricksS2/impacket.git
RUN python3 -m pip install impacket/

FROM python:3.8-alpine
COPY --from=compile /opt/venv /opt/venv

RUN mkdir /shared
VOLUME ["/shared"]

ENV PATH="/opt/venv/bin:$PATH"
ENTRYPOINT ["/bin/sh"]
CMD []