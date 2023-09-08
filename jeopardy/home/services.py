from jeopardy.adapters.repository import AbstractRepository
from jeopardy.domainmodel.model import Question, Answer, Scoreboard

def getScoreboard(repo: AbstractRepository):
    return repo.getScoreboard()

def getQuestion(category, value, repo: AbstractRepository):
    questions = repo.getAllQuestions()
    for question in questions:
        if question.category == category and question.value == value:
            return question
    return None

def getAnswer(category, value, repo: AbstractRepository):
    answers = repo.getAllAnswers()
    print(answers)
    for a in answers:
        if a.category == category and a.value == value:
            return a
    return None