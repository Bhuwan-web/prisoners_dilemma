from abc import ABC, abstractmethod

from schemas.records import MoveEnums, RecordType


class Game(ABC):
    """
    Defind a move method to make a next moves based of of current game state
    """

    @abstractmethod
    def move(
        self, own_record: RecordType, opponent_record: RecordType
    ) -> MoveEnums:
        pass

    @abstractmethod
    def description(self) -> str:
        pass
