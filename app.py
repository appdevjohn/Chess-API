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
    board_position: str


@app.get('/', tags=['Default'])
def index():
    """
    Simple GET request that returns a helpful message.
    """
    return {'message': 'Go to \'/docs\' in your browser to view the documentation.'}


@app.post('/suggest-move', tags=['Chess Engine'])
def test_chess_engine(body: MoveSuggestionBody):
    """
    Suggests a move given a chess game. The game state is expected to
    be a FEN string.
    """
    stockfish = Stockfish()
    stockfish.set_fen_position(body.board_position)
    stockfish.set_elo_rating(1350)
    best_move = stockfish.get_best_move_time(1000)

    return {'best_move': best_move}
