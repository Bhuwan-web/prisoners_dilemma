from adapter.always_attack.strategy import AlwaysAttack
from adapter.double_attack.strategy import DoubleAttack
from adapter.double_defense.strategy import DoubleDefense
from adapter.random_moves.strategy import RandomMoves
from adapter.tit_for_tat.strategy import TitForTat


strategies = {
    "tit_for_tat": TitForTat,
    "always_attack": AlwaysAttack,
    "double_attack": DoubleAttack,
    "double_defense": DoubleDefense,
    "random_moves": RandomMoves,
}
