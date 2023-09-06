import abc
from jeopardy.adapters.datareader import csvdatareader
from jeopardy.domainmodel.model import Question, Answer, Scoreboard

repo_instance = None

class RepositoryException(Exception):
    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):
    """Interface for a repository providing access to game data."""

    @abc.abstractmethod
    def add_question(self, game: Question):
        """Adds a question to the repository."""
        raise NotImplementedError
    
    @abc.abstractmethod
    def add_answer(self, answer: Answer):
        """Adds an answer to the repository."""
        raise NotImplementedError
    
    def add_scoreboard(self, scoreboard: Scoreboard):
        """Adds a scoreboard to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def getAllQuestions(self):
        """Retrieve all questions stored in the repository."""
        raise NotImplementedError
    
    @abc.abstractmethod
    def getAllAnswers(self):
        """Retrieve all answers stored in the repository."""
        raise NotImplementedError
    
    @abc.abstractmethod
    def getScoreboard(self):
        """Retrieve the scoreboard stored in the repository."""
        raise NotImplementedError

