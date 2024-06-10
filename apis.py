from fastapi import APIRouter

from schemas.game import GamePayload, GameReport, Strategies
from services.game import GameService
from services.strategies import Strategy as StrategyService

api_router = APIRouter()


@api_router.get("/health")
def health_check():
    return {"status": "ok"}


@api_router.post("/game")
def game(game_payload: GamePayload) -> GameReport:
    game = GameService(game_payload)
    game_summary = game.play()
    return game.report(game_summary)


@api_router.get("/strategies")
def strategies() -> list[Strategies]:
    return StrategyService().list_strategies()
