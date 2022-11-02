# pull the official docker image
FROM python:3.11.0a1-slim

# set work directory
WORKDIR /

# install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy project
COPY . .