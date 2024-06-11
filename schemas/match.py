from typing import List
from pydantic import BaseModel


class PlayerRecord(BaseModel):
    strategy: str
    move: str
    score: int = 0


class MatchRecord(BaseModel):
    strategy1: PlayerRecord
    strategy2: PlayerRecord


class GameRecords(BaseModel):
    records: List[MatchRecord]
