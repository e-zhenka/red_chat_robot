#!/bin/sh

ollama serve &

sleep 5

if ! ollama pull llama3:8b; then
    echo "Error during model loading"
    exit 1
fi

if [ ! -f /root/Modelfile ]; then
    echo "Error: /root/Modelfile not found"
    exit 1
fi

if ! ollama create ivan -f /root/Modelfile; then
    echo "Error during model creating"
    exit 1
fi

if ! ollama rm llama3:8b; then
    echo "Error during model deleting"
    exit 1
fi

if ! ollama run ivan; then
    echo "Error during model startup"
    exit 1
fi

echo "All operations completed successfully!"