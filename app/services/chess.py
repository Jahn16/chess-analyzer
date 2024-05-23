from io import StringIO

import chess
import chess.pgn
from chess.pgn import Game

from app.schemas.opening import Opening
from app.services.openings import load_openings


def read_pgn(pgn: str) -> Game:
    pgn_bytes = StringIO(pgn)
    game = chess.pgn.read_game(pgn_bytes)
    if game is None:
        raise Exception("Invalid PGN")
    return game


def determine_opening(game: Game, openings: list[Opening]) -> Opening:
    board = game.end().board()
    openings_epd = [o.epd for o in openings]
    while board.move_stack:
        if board.epd() in openings_epd:
            index = openings_epd.index(board.epd())
            opening = openings[index]
            opening.move_count = board.ply()
            return opening
        board.pop()
    raise ValueError("No opening found")


def in_opening(board_epd: str, openings: list[Opening]) -> bool:
    return board_epd in [o.epd for o in openings]


def analyze(pgn: str) -> list[str]:
    analysis = []
    openings = load_openings()
    game = read_pgn(pgn)
    board = game.board()
    opening = determine_opening(game, openings)
    print(opening)
    for index, move in enumerate(game.mainline_moves()):
        board.push(move)
        in_opening = board.ply() <= opening.move_count
        analysis.append(f"{index}. in opening: {in_opening} - {opening.name}")
    return analysis
