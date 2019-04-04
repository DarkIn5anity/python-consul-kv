FROM ubuntu:latest

ENV FILENAME /kv/example.yml


# Copy the Python Script to blink LED
COPY src/ /kv

RUN	chmod +x /kv/bootstrap.sh

RUN     apt-get update -y && apt-get upgrade -y && \
        apt-get install -y libcurl4-openssl-dev libssl-dev libxml2-dev libxslt1-dev python python-pip

#RUN .	/opt/app-root/etc/scl_enable && pip uninstall pycurl	&& \
#	export PYCURL_SSL_LIBRARY=openssl	&& \
#	export LDFLAGS=-L/usr/local/opt/openssl/lib;export CPPFLAGS=-I/usr/local/opt/openssl/include;pip install pycurl --compile --no-cache-dir

RUN pip install -r /kv/requirements.txt


# Trigger Python script
ENTRYPOINT ["/kv/bootstrap.sh"]
