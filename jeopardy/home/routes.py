from flask import Blueprint, render_template
from flask import request

from jeopardy.home import services
from jeopardy.utils import utilities
import jeopardy.adapters.repository as repo

home = Blueprint('home', __name__, static_folder='static', template_folder='templates')


@home.route('/', methods=['GET'])
def home_home():
    scoreboard = services.getScoreboard(repo.repo_instance)

    return render_template('layout.html',
                           scoreboard = scoreboard,
                           )

@home.route('/question', methods=['GET'])
def question():
    category = request.args.get('category')
    value = request.args.get('value')
    
    # Retrieve the question data from the repository
    question = services.getQuestion(category, value, repo.repo_instance)

    return render_template('question.html',
                           question=question.question,
                           image=question.image,
                           value=question.value)
    
@home.route('/answer', methods=['GET'])
def answer():
    category = request.args.get('category')
    value = request.args.get('value')
        
    # Retrieve the answer data from the repository
    answer = services.getAnswer(category, value, repo.repo_instance)

    return render_template('answer.html',
                           answer=answer.answer
                           )
