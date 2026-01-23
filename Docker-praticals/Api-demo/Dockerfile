FROM python:slim

WORKDIR /pyapp

COPY ./api_demo.py .

RUN pip install requests

CMD ["python","api_demo.py"]