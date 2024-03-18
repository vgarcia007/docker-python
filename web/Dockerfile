FROM python:alpine3.19
ADD . /web
WORKDIR /web
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/bash", "/web/AppStart.sh"]
