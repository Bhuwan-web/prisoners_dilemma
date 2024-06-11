from schemas.game import Strategies
from adapter.adaptor_mapping import strategies


class Strategy:
    def list_strategies(self):
        strategies_details = []
        strategies_lst = list(strategies.keys())
        for strategy in strategies_lst:
            strategy_obj = strategies[strategy]()
            strategies_details.append(
                Strategies(
                    **{
                        "strategy_name": strategy,
                        "strategy_description": strategy_obj.description(),
                    }
                )
            )
        return strategies_details
