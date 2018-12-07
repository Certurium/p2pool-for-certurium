FROM alpine:3.8

RUN apk update
RUN apk add python2
RUN apk add python2-dev
RUN apk add musl-dev
RUN apk add libffi-dev
RUN apk add openssl-dev
RUN apk add py2-pip
RUN pip install --upgrade pip
RUN apk add gcc

WORKDIR /p2pool
COPY . /p2pool

RUN cd neoscrypt && python setup.py install

RUN pip install -r requirements.txt

EXPOSE 19327/tcp

ENTRYPOINT ["/usr/bin/python"]
CMD ["run_p2pool.py","--help"]

