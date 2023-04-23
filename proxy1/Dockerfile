# Use the official Python image as the base image
FROM handsonsecurity/seed-ubuntu:large

RUN apt-get update

WORKDIR /app

COPY . /app

CMD ["python3", "proxy1.py"]

