FROM python:3.9-alpine

COPY . /frontend
WORKDIR /frontend

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8005

CMD ["python", "main.py"]
