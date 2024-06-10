from adaptor.adaptor_mapping import strategies
from adaptor.game_abc import Game
from schemas.game import GamePayload, GameReport
from schemas.records import MoveEnums, RecordType


class GameService:
    def __init__(self, game_payload: GamePayload) -> None:
        self.game_payload: GamePayload = game_payload
        strategy1, strategy2 = (
            game_payload.first_strategy,
            game_payload.second_strategy,
        )
        self.strategy1_record: RecordType = []
        self.strategy2_record: RecordType = []
        self.strategy1_game: Game = strategies.get(strategy1)()
        self.strategy2_game: Game = strategies.get(strategy2)()
        self.strategy1_score = 0
        self.strategy2_score = 0

    def compute_score(self, strategy1_move, strategy2_move):
        if strategy1_move == strategy2_move == MoveEnums.COOPERATE:
            self.strategy1_score += 3
            self.strategy2_score += 3
        elif strategy1_move == strategy2_move == MoveEnums.DEFECT:
            self.strategy1_score += 1
            self.strategy2_score += 1
        elif (
            strategy1_move == MoveEnums.COOPERATE
            and strategy2_move == MoveEnums.DEFECT
        ):
            self.strategy2_score += 5
        elif (
            strategy1_move == MoveEnums.DEFECT
            and strategy2_move == MoveEnums.COOPERATE
        ):
            self.strategy1_score += 5

    def play(self):
        for _ in range(self.game_payload.rounds):
            strategy1_move = self.strategy1_game.move(
                self.strategy1_record, self.strategy2_record
            )
            strategy2_move = self.strategy2_game.move(
                self.strategy2_record, self.strategy1_record
            )
            self.strategy1_record.append(strategy1_move)
            self.strategy2_record.append(strategy2_move)
            self.compute_score(strategy1_move, strategy2_move)

        return [
            {
                "strategy": f"{self.game_payload.first_strategy}",
                "score": self.strategy1_score,
            },
            {
                "strategy": f"{self.game_payload.second_strategy}",
                "score": self.strategy2_score,
            },
        ]

    def report(self, game_summary):
        if self.strategy1_score == self.strategy2_score:
            return GameReport(winner="Draw", scores=game_summary)
        winner = max(game_summary, key=lambda x: x.get("score")).get(
            "strategy"
        )
        return GameReport(winner=winner, scores=game_summary)
