import random
from adaptor.game_abc import Game
from schemas.records import MoveEnums, RecordType


class RandomMoves(Game):
    def move(
        self, own_record: RecordType, opponent_record: RecordType
    ) -> MoveEnums:
        """
        Plays Random,Unpredictable Moves.

        """
        return random.choice([MoveEnums.DEFECT, MoveEnums.COOPERATE])

    def description(self) -> str:
        return "Plays Very random,Unpredictable Moves. Could attack or coperate any time, without depending upon previous moves."
