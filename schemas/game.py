import random
from typing import List, Optional
from adapter.adaptor_mapping import strategies
from pydantic import BaseModel, Field, field_validator, model_validator

from schemas.match import GameRecords


strategies = tuple(strategies.keys())


class GamePayload(BaseModel):
    first_strategy: Optional[str] = Field(
        default=None, description="Provide the name of one registered strategy"
    )
    second_strategy: Optional[str] = Field(
        default=None, description="Provide the name of one registered strategy"
    )
    random_strategies: bool = Field(
        default=False,
        description="Randomly select two strategies. If set to True, it will internally select two random strategies and give results between them.",
    )
    rounds: int = Field(
        default=200,
        description="Number of rounds to play",
        ge=1,
    )

    @field_validator("first_strategy", "second_strategy")
    def validate_stragegies(cls, value):
        if not value:
            value = random.choice(strategies)
        elif value not in strategies:
            raise ValueError(f"Strategy {value} not in {strategies}")
        return value

    @model_validator(mode="after")
    def validate_payload(cls, values: "GamePayload"):
        if values.random_strategies:
            values.first_strategy, values.second_strategy = (
                random.choice(strategies),
                random.choice(strategies),
            )
        if values.first_strategy == values.second_strategy:
            values.second_strategy = random.choice(strategies)
            if not values.first_strategy:
                values.first_strategy = random.choice(strategies)
            cls.validate_payload(values)
        return values


class GameReport(BaseModel):
    winner: str
    scores: List[dict]
    score_board: GameRecords


class Strategies(BaseModel):
    strategy_name: str
    strategy_description: str
