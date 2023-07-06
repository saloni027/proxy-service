FROM python:3.8.3
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# CMD python proxy_server.py