FROM python:2
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM mohaseeb/raspberrypi3-python-opencv:latest


CMD ["python", "./main.py"]