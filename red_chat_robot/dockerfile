FROM python:3.10.16-alpine as builder

WORKDIR /app

RUN pip install poetry
COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY src/ /app/src/

WORKDIR /app/src/red_chat_robot

CMD ["python", "main.py"]