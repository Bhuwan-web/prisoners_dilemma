from adapter.game_abc import Game
from schemas.records import MoveEnums, RecordType


class AlwaysAttack(Game):
    def move(
        self, own_record: RecordType, opponent_record: RecordType
    ) -> None:
        return MoveEnums.DEFECT

    def description(self) -> str:
        return "Always attack"
