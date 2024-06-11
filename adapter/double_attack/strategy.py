from adapter.game_abc import Game
from schemas.records import MoveEnums, RecordType


class DoubleAttack(Game):
    def move(
        self, own_record: RecordType, opponent_record: RecordType
    ) -> MoveEnums:
        """
        Play Aggressive, Only attact if opponent has attacked before.But If Opponent Attack once it attack twice.

        Returns:

        """
        if opponent_record and (
            opponent_record[-1] == MoveEnums.DEFECT
            or (
                len(opponent_record) > 1
                and (opponent_record[-2] == MoveEnums.DEFECT)
            )
        ):
            return MoveEnums.DEFECT
        else:
            return MoveEnums.COOPERATE

    def description(self) -> str:
        return "Play Aggressive, Only attact if opponent has attacked before.But If Opponent Attack once it attack twice."
