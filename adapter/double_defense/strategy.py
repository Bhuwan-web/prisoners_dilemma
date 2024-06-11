from adapter.game_abc import Game
from schemas.records import MoveEnums, RecordType


class DoubleDefense(Game):
    def move(
        self, own_record: RecordType, opponent_record: RecordType
    ) -> MoveEnums:
        """
        Plays Defensive, Only Defect if opponent has Defected before twice consecutively.

        """
        if len(opponent_record) > 1 and (
            opponent_record[-1] == opponent_record[-2] == MoveEnums.DEFECT
        ):
            return MoveEnums.DEFECT
        else:
            return MoveEnums.COOPERATE

    def description(self) -> str:
        return "Play Aggressive, Only attact if opponent has attacked before.But If Opponent Attack once it attack twice."
