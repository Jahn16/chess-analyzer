from pydantic import BaseModel


class Opening(BaseModel):
    eco: str
    name: str
    pgn: str
    uci: str
    epd: str
    move_count: int = -1
