from App import app, db
from App.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

from werkzeug.security import generate_password_hash