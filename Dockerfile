FROM python:3.11-slim

RUN pip install luma.led_matrix pillow paho-mqtt

COPY matrix.py /matrix.py

CMD ["python", "/matrix.py"]
