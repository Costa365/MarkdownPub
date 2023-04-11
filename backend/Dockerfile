FROM python:3.9-alpine

COPY . /backend
WORKDIR /backend

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD ["python", "main.py"]
