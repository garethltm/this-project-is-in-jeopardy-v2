"""Initialize Flask app."""

from flask import Flask, render_template
from pathlib import Path

import jeopardy.adapters.repository as repo
from jeopardy.adapters.memory_repository import MemoryRepository, populate

from jeopardy.home.routes import home

def create_app():
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    data_path = Path('jeopardy') / 'adapters' / 'data'

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    # fill the content with the repository from the provided csv files
    populate(data_path, repo.repo_instance)

    # Register the blueprints.
    app.register_blueprint(home)
    
    return app
