#image
FROM python:3.8-slim-buster

#what and all Variable we need to define
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory
WORKDIR /code

#install dependices
COPY ./requirments.txt .
RUN pip install -r requirments.txt

#copy project
COPY . .