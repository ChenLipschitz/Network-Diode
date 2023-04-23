# Use the official Python image as the base image
FROM handsonsecurity/seed-ubuntu:large

WORKDIR /app

COPY . /app

RUN pip3 install tqdm 

CMD ["python3", "user.py"]



