FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app .

ENV PORT 8000

CMD ["uvicorn", "app.pong_server:app", "--host", "0.0.0.0", "--port", "$PORT"]
