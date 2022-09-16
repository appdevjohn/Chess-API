FROM python:3.10

RUN apt-get update
RUN apt-get install stockfish

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV STOCKFISH_PATH='/usr/games/stockfish'

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]