import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from stockfish import Stockfish

DESCRIPTION = """
This API does one thing only: it takes a chess game and returns the
best next move. This project will grow, but for now it is intended to
be a REST API to interface with the Stockfish chess engine.
"""

app = FastAPI(
    title='Chess API',
    description=DESCRIPTION,
    version='1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class MoveSuggestionBody(BaseModel):
    fen: str
    skill_level: int = 10


@app.get('/', tags=['Default'])
def index():
    """
    Simple GET request that returns a helpful message.
    """
    return {'message': 'Go to \'/docs\' in your browser to view the documentation.'}


@app.post('/suggest-move', tags=['Chess Engine'])
def test_chess_engine(body: MoveSuggestionBody):
    """
    Suggests a move given a chess game and skill level. The game state is expected to
    be a FEN string, and the skill level is an integer between 0 and 20 inclusive.
    """
    STOCKFISH_PATH = os.getenv('STOCKFISH_PATH') or 'stockfish'

    stockfish = Stockfish(path=STOCKFISH_PATH)
    stockfish.set_fen_position(body.fen)
    stockfish.set_skill_level(body.skill_level)
    best_move = stockfish.get_best_move()

    return {'best_move': best_move}
