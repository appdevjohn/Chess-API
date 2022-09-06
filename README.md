# Chess API
This API does one thing only: it takes a chess game and returns the best next move. This project will grow, but for now it is intended to be a REST API to interface with the Stockfish chess engine.

### Environment Variables
| Name           | Description | Required |
| -------------- | ----------- | -------- |
| STOCKFISH_PATH | The path to call Stockfish from the terminal. | True, if Stockfish is not available globally. |

### Getting Started
1. Ensure python and pip are installed on your machine.
1. Ensure Stockfish is installed on your machine.
2. Ensure the environment variables are set up as needed.
3. Install python dependencies by running `pip install -r requirements.txt`
4. Run `uvicorn app:app --reload` to run the project.

### Running with Docker
1. Run `docker build -t chess-api .`
2. Run `docker run -p 8000:8000 chess-api` ensuring the port is exposed.