from jeopardy.adapters.repository import AbstractRepository
from jeopardy.domainmodel.model import Question, Answer, Scoreboard

def getScoreboard(repo: AbstractRepository):
    return repo.getScoreboard()