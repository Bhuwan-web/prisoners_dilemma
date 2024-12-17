
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
## Let's understand a game


# The Prisoner's Dilemma: A Game of Strategy and Trust
In a dimly lit interrogation room, two suspects, Alex and Jordan, are apprehended by the authorities for a serious crime. They are taken into separate rooms and given a proposition that will test their loyalty and strategic thinking. This scenario, known as the Prisoner's Dilemma, is a classic example of game theory, exploring the tension between cooperation and self-interest.

## The Setup:
Alex and Jordan are accused of a crime they both participated in.
The Authorities offer them each the same deal, but they cannot communicate with each other.
The Choices:
Cooperate (Stay Silent): Both Alex and Jordan choose not to betray each other.
Defect (Betray the Other): One or both decide to betray the other in hopes of a lighter sentence.
## The Outcomes:
Both Cooperate: If Alex and Jordan both cooperate (stay silent), they each receive a light sentence, say, 1 year in prison. This is a moderately positive outcome for both.

Points: Alex: 3, Jordan: 3
One Defects, One Cooperates: If Alex defects (betrays Jordan) while Jordan cooperates (stays silent), Alex goes free, and Jordan receives a harsh sentence, say, 5 years in prison, and vice versa.

Points if Alex Defects and Jordan Cooperates: Alex: 5, Jordan: 0
Points if Jordan Defects and Alex Cooperates: Jordan: 5, Alex: 0
Both Defect: If both Alex and Jordan defect (betray each other), they each receive a moderate sentence, say, 3 years in prison. This is a less optimal outcome for both compared to mutual cooperation.

Points: Alex: 1, Jordan: 1
## The Dilemma:
Trust vs. Self-Interest: The dilemma lies in the fact that while mutual cooperation yields a better collective outcome, the fear of being betrayed and the lure of personal gain often push individuals towards defection.
Multiple Rounds: In a twist, imagine Alex and Jordan face this decision repeatedly, say up to 200 rounds. Each round's outcome influences their future decisions, testing their ability to build trust or descend into mutual betrayal.
## Example Round Scenarios:
First Round:

Alex and Jordan both decide to cooperate, hoping to establish trust. Each earns 3 points.
Middle Rounds:

Distrust begins to set in. Alex defects while Jordan cooperates. Alex earns 5 points while Jordan gets none. The next round, Jordan might retaliate.
Final Rounds:

With scores close and trust shattered, both may end up defecting repeatedly, each earning 1 point per round but missing the chance for a higher collective score.
Viewer Engagement:
As Alex and Jordan navigate through multiple rounds of this dilemma, viewers are drawn into the psychological battle, rooting for cooperation but often witnessing the inevitable defection. Each round brings new tension and strategic depth, making the Prisoner's Dilemma a fascinating study of human behavior, trust, and the fine line between cooperation and self-interest.```

*As there will be multiple rounds, Add up your own strategies That you believe could win*

Concept Reference From:https://www.youtube.com/watch?v=mScpHTIi-kM&ab_channel=Veritasium



# Add Your Strategy
Steps you can take to add up your strategy into the project and match against other's 

github secrets
ghp_abcdefghijklmnopqrstuvwxyz1234567890ABCD

1. Add Strategy In adaptor ( convention used is create directory of your strategy and add script strategy.py)
2. Follow the pattern using game_abc.py abstract method to design the basic structure of strategy
3. give one name to the strategy and add it in the adaptor_mapping.py strategies dict, strategy name as key and strategy class as value
4. run program , check if strategy is successfully added to the program using `/strategies` api
5. compare your strategies with another strategy using `/game` api 
