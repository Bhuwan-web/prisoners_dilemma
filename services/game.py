from adapter.adaptor_mapping import strategies
from adapter.game_abc import Game
from schemas.game import GamePayload, GameReport
from schemas.match import GameRecords, MatchRecord, PlayerRecord
from schemas.records import MoveEnums, RecordType


class GameService:
    def __init__(self, game_payload: GamePayload) -> None:
        self.game_payload: GamePayload = game_payload
        strategy1, strategy2 = (
            game_payload.first_strategy,
            game_payload.second_strategy,
        )
        self.strategy1_moves: RecordType = []
        self.strategy2_moves: RecordType = []
        self.strategy1_game: Game = strategies.get(strategy1)()
        self.strategy2_game: Game = strategies.get(strategy2)()
        self.strategy1_score = 0
        self.strategy2_score = 0
        self.game_record: GameRecords = []

    def update_match_socres(self, match_record: MatchRecord):
        strategy1_move = match_record.strategy1.move
        strategy2_move = match_record.strategy2.move
        COOPERATE = MoveEnums.COOPERATE.value
        DEFECT = MoveEnums.DEFECT.value
        if strategy1_move == strategy2_move == COOPERATE:
            match_record.strategy1.score = 3
            match_record.strategy2.score = 3
        elif strategy1_move == strategy2_move == DEFECT:
            match_record.strategy1.score = 1
            match_record.strategy2.score = 1
        elif strategy1_move == COOPERATE and strategy2_move == DEFECT:
            match_record.strategy2.score = 5
        elif strategy1_move == DEFECT and strategy2_move == COOPERATE:
            match_record.strategy1.score = 5
        self.strategy1_score += match_record.strategy1.score
        self.strategy2_score += match_record.strategy2.score
        return match_record

    def play(self):
        for _ in range(self.game_payload.rounds):
            strategy1_move = self.strategy1_game.move(
                self.strategy1_moves, self.strategy2_moves
            )
            strategy2_move = self.strategy2_game.move(
                self.strategy2_moves, self.strategy1_moves
            )
            self.strategy1_moves.append(strategy1_move)
            self.strategy2_moves.append(strategy2_move)

            match_record = self.generate_match_record(
                strategy1_move, strategy2_move
            )
            self.game_record.append(match_record)

        return self.game_record

    def generate_match_record(self, strategy1_move, strategy2_move):
        match_record = MatchRecord(
            strategy1=PlayerRecord(
                strategy=self.game_payload.first_strategy,
                move=strategy1_move,
            ),
            strategy2=PlayerRecord(
                strategy=self.game_payload.second_strategy,
                move=strategy2_move,
            ),
        )
        revised_match_record = self.update_match_socres(match_record)
        return revised_match_record

    def game_summary(self):
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

    def get_winner(self):
        if self.strategy1_score == self.strategy2_score:
            return "Draw"
        else:
            return max(self.game_summary(), key=lambda x: x.get("score")).get(
                "strategy"
            )

    def report(self):
        game_summary = self.game_summary()
        game_records = GameRecords(records=self.game_record)
        winner = self.get_winner()
        return GameReport(
            winner=winner, scores=game_summary, score_board=game_records
        )
