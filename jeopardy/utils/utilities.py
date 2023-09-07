from jeopardy.adapters.repository import AbstractRepository
from jeopardy.domainmodel.model import Question, Answer

def getAllQuestions(repo: AbstractRepository):
    return repo.getAllQuestions()

def getAllAnswers(repo: AbstractRepository):
    return repo.getAllAnswers()

def getQuestion(category, value, repo):
    questions = repo.getAllQuestions()
    for question in questions:
        if question.category == category and question.value == value:
            return question
    return None

