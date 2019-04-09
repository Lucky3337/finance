FROM python:3
MAINTAINER Vladislav Bobrov <bobrov.v1ad3@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/