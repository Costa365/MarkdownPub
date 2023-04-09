FROM python:3.9-alpine

ADD . ./frontend
WORKDIR ./frontend

COPY ./requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8005

CMD python main.py
