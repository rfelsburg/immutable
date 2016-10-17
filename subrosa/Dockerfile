FROM python:2.7
EXPOSE 8000

COPY app /usr/src/app
COPY entrypoint.sh /entrypoint.sh

WORKDIR /usr/src/app

RUN pip install -r requirements.txt
RUN ./install
