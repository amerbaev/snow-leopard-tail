FROM python:3.5.2

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN mkdir /usr/snow-leopard-tail

COPY . /usr/snow-leopard-tail

WORKDIR /usr/snow-leopard-tail

EXPOSE 8080

CMD gunicorn --bind 0.0.0.0:8080 snow_leopard_tail:app