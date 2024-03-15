FROM python:3.9-slim

WORKDIR /app

COPY main.py /app/main.py

COPY etudiants.json /app/etudiants.json

# boucle pour faire tourner le conteneur indefiniment
CMD ["python", "-c", "while True: pass"]