from collections import deque

import gradio as gr
import ollama

chat_history = deque(maxlen=20)


def chat(msg, history):
    global chat_history
    chat_history.append({"role": "user", "content": msg})
    chat_model = ollama.Client(host="http://ollama:11434")
    res = chat_model.chat(
        model="ivan",
        messages=chat_history,
        keep_alive=60,
        stream=True,
        options={"f16_kv": True, "num_batch": 256, "num_thread": 10}
    )
    text = ''
    for item in res:
        text += item.message.content
        yield text
    chat_history.append({"role": "assistant", "content": text})


demo = gr.ChatInterface(fn=chat, type="messages", title="Chat Bot🤖",)

if __name__ == "__main__":
    demo.queue().launch(server_name="0.0.0.0", server_port=7860)
