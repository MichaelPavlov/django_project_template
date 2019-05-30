FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
ADD config/requirements.txt /app/requirements.txt
WORKDIR /app/
RUN pip install -r requirements.txt
RUN adduser --disabled-password --gecos '' user
USER user