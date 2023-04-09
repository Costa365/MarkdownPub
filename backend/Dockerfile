FROM python:3.9-alpine

ADD . ./backend
WORKDIR ./backend

COPY ./requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python main.py
