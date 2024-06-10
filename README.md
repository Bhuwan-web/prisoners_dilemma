
### README.md

```markdown
# FastAPI Application

A simple FastAPI application to mimic famous game theory with different strategies.

## Prerequisites

- Python 3.7+
- `pip` for dependency management


### Clone the Repository

```bash
git clone git@github.com:Bhuwan-web/game_theory.git
cd game_theory
```

### Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn main:app --reload
```

Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Interactive API Documentation

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


# Game Theory
## Let's understand a game by an example

```In a bustling city, two struggling entrepreneurs, Alice and Bob, find themselves indebted to a powerful banker named Mr. Gold. Desperate to settle their debts, they agree to participate in a series of challenges orchestrated by Mr. Gold.

The rules are simple: In each round of the challenge, Alice and Bob must decide whether to cooperate or defect. Their choices will determine their fate and their standing with Mr. Gold.

If Alice cooperates while Bob defects, Bob earns 5 points, leaving Alice with nothing.
If both Alice and Bob cooperate, they each earn 3 points, showing unity in their struggle.
If both Alice and Bob defect, they each receive 1 point, showcasing their individualistic approach.
As the rounds progress, the tension mounts, and Alice and Bob must navigate the complexities of trust, loyalty, and self-preservation. Will they choose to stand together against Mr. Gold's schemes, or will they succumb to the temptation to betray each other for personal gain?

With each decision, viewers are drawn deeper into the drama, eagerly anticipating the next twist in the tale of greed, ambition, and the quest for redemption. And as the final round approaches, the true test of character awaits, revealing who will emerge victorious in the ultimate game of survival.```

*As there will be multiple rounds, Add up your own strategies That you believe could win*

Concept Reference From:https://www.youtube.com/watch?v=mScpHTIi-kM&ab_channel=Veritasium


```
# Add Your Strategy
Steps you can take to add up your strategy into the project and match against other's 

1. Add Strategy In adaptor ( convention used is create directory of your strategy and add script strategy.py)
2. Follow the pattern using game_abc.py abstract method to design the basic structure of strategy
3. give one name to the strategy and add it in the adaptor_mapping.py strategies dict, strategy name as key and strategy class as value
4. run program , check if strategy is successfully added to the program using `/strategies` api
5. compare your strategies with another strategy using `/game` api 