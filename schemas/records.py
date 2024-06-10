from enum import Enum
from pydantic import BaseModel
from typing import List


class MoveEnums(Enum):
    DEFECT = "Attack"
    COOPERATE = "Defense"


RecordType = List[MoveEnums]


class Records(BaseModel):
    player1: RecordType
    player2: RecordType
