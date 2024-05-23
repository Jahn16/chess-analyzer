from fastapi import FastAPI

from app.services.chess import analyze

app = FastAPI()


@app.get("/")
async def root(pgn: str) -> list[str]:
    analysys = analyze(pgn)
    return analysys
