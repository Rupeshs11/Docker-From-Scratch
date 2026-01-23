FROM python:slim

WORKDIR /pyapp

COPY ./myapp.py .

RUN pip install requests

CMD ["python","myapp.py"]