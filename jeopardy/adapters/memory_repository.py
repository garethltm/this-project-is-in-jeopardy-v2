from pathlib import Path

import random

from jeopardy.adapters.repository import AbstractRepository, RepositoryException
from jeopardy.domainmodel.model import Question, Answer, Scoreboard
from jeopardy.adapters.datareader import csvdatareader

class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__questions = list()
        self.__answers = list()
        self.__scoreboard = list()

    def add_question(self, question: Question):
        if question not in self.__questions:
            self.__questions.append(question)

    def add_answer(self, answer: Answer):
        if answer not in self.__answers:
            self.__answers.append(answer)
            
    def getAllQuestions(self):
        return self.__questions

    def getAllAnswers(self):
        return self.__answers
    
    def getScoreboard(self):
        return self.__scoreboard

def load_gamedata(data_path: Path, repo: MemoryRepository):
    data_path = Path(data_path) / 'questions.csv'
    reader = csvdatareader.GameFileCSVReader(data_path)
    reader.read_csv_file()
    for question in reader.dataset_of_questions:
        repo.add_question(question)
    for answer in reader.dataset_of_answers:
        repo.add_answer(answer)
        
def populate(data_path: Path, repo: MemoryRepository):
    load_gamedata(data_path, repo)