from app import create_app
from app.flaskr import User, Post

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
