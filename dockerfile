FROM python:3.10.16-alpine

WORKDIR /app

COPY reuqirements.txt ./
RUN pip install -r requirements.txt

COPY src/ /app/src/
COPY config.yaml /app

CMD ["python", "src/red_chat_robot/main.py"]