# pull official base image
FROM python:3.8.6-slim-buster

# set working directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN export PYTHONPATH=/usr/src/app

COPY ./ /app


# run entrypoint.sh

CMD ["/usr/src/app/entrypoint.sh"]

# # Run application
# ENTRYPOINT  ["python","./app/main.py"]
