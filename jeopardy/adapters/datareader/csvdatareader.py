import csv
import os

from jeopardy.domainmodel.model import Question, Answer


class GameFileCSVReader:
    def __init__(self, filename):
        self.__filename = filename
        self.__dataset_of_questions = set()
        self.__dataset_of_answers = set()

    def read_csv_file(self):
        if not os.path.exists(self.__filename):
            print(f"path {self.__filename} does not exist!")
            return
        with open(self.__filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    category = row["Category"]
                    question = row["Question"]
                    value = row["Value"]
                    q = Question(category,question,value)
                    q.image = row["Image"]
                    answer = row["Answer"]
                    
                    self.__dataset_of_questions.add(q)
                    self.__dataset_of_answers.add(Answer(answer))

                except ValueError as e:
                    print(f"Skipping row due to invalid data: {e}")
                except KeyError as e:
                    print(f"Skipping row due to missing key: {e}")

    def get_unique_questions(self):
        return len(self.__dataset_of_questions)

    def get_unique_answers(self):
        return len(self.__dataset_of_answers)

    @property
    def dataset_of_questions(self) -> set:
        return self.__dataset_of_questions

    @property
    def dataset_of_answers(self) -> set:
        return self.__dataset_of_answers
