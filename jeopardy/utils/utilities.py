from jeopardy.adapters.repository import AbstractRepository
from jeopardy.domainmodel.model import Question, Answer


def getAllQuestions(repo: AbstractRepository):
    return repo.getAllQuestions()

def getAllAnswers(repo: AbstractRepository):
    return repo.getAllAnswers()
