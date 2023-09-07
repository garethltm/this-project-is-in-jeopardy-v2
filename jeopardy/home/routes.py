from flask import Blueprint, render_template
from flask import request

from jeopardy.home import services
from jeopardy.utils import utilities
import jeopardy.adapters.repository as repo

home = Blueprint('home', __name__, static_folder='static', template_folder='templates')


@home.route('/', methods=['GET'])
def home_home():
    scoreboard = services.getScoreboard(repo.repo_instance)
    questions = utilities.getAllQuestions(repo.repo_instance)
    answers = utilities.getAllAnswers(repo.repo_instance)

    return render_template('layout.html',
                           scoreboard = scoreboard,
                           questions = questions,
                           answers = answers
                           )

@home.route('/question', methods=['GET'])
def question():
    value = request.args.get('value')
    category = request.args.get('category')

    # Retrieve the question data from the repository
    question = utilities.getQuestion(category, value, repo.repo_instance)

    return render_template('question.html',
                           question=question)
