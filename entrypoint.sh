#!/usr/bin/sh

ollama serve &

ollama pull llama3:8b

ollama create ivan -f /root/Modelfile

ollama rm llam3:8b

ollama run ivan