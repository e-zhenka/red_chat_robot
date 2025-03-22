from collections import deque
from pathlib import Path

import gradio as gr
import ollama
from config import Config

chat_history = deque(maxlen=20)
# config_path = Path(__file__).parents[-3] / "config.yaml"
settings = Config.from_yaml("config.yaml").model_dump()


def chat(msg, history):
    global chat_history
    chat_history.append({"role": "user", "content": msg})
    chat_model = ollama.Client(host="http://ollama:11434")
    res = chat_model.chat(messages=chat_history, **settings)
    text = ''
    for item in res:
        text += item.message.content
        yield text
    chat_history.append({"role": "assistant", "content": text})


demo = gr.ChatInterface(fn=chat, type="messages", title="Chat Bot🤖",)

if __name__ == "__main__":
    demo.queue().launch(server_name="0.0.0.0", server_port=7860)
