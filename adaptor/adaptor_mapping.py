from adaptor.always_attack.strategy import AlwaysAttack
from adaptor.double_attack.strategy import DoubleAttack
from adaptor.double_defense.strategy import DoubleDefense
from adaptor.random_moves.strategy import RandomMoves
from adaptor.tit_for_tat.strategy import TitForTat


strategies = {
    "tit_for_tat": TitForTat,
    "always_attack": AlwaysAttack,
    "double_attack": DoubleAttack,
    "double_defense": DoubleDefense,
    "random_moves": RandomMoves,
}
