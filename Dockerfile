FROM python:2
FROM mohaseeb/raspberrypi3-python-opencv:latest

WORKDIR /app
ADD . /app

RUN pip install --no-cache-dir -r requirements.txt



CMD ["python", "./main.py"]