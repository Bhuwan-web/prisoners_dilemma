from adapter.game_abc import Game
from schemas.records import MoveEnums, RecordType


class TitForTat(Game):
    def move(
        self, own_record: RecordType, opponent_record: RecordType
    ) -> MoveEnums:
        """Play fair, Only attact if opponent has attacked before.

        Returns:

        """
        if opponent_record and opponent_record[-1] == MoveEnums.DEFECT:
            return MoveEnums.DEFECT
        else:
            return MoveEnums.COOPERATE

    def description(self) -> str:
        return "Never Attact first by itself, but attact if opponent has attacked on recent previous round."
