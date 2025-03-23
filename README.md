# Инструкция по запуску чат-бота

1) Подымаем докер `docker-compose up`
2) Ожидаем полнецнной загрузки приложения. Индикатор того, что приложение готово к работе - это следующие сообщения в консоли:
```
chat    | Watching: '/app' '/app'
chat    |
chat    | * Running on local URL:  http://0.0.0.0:7860
chat    |
chat    | To create a public link, set `share=True` in `launch()`.
```
3) Перейти в браузер по адресу `http://localhost:7860/`; можно начать общаться

# Техничесие подробности решения

- LLM: llama3:8b
- GUI: gradio
- memory: реализована на основе очереди
- libraries:
	- ollama
	- gradio
- docker
