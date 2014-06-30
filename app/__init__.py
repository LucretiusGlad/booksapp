import os
import sys

from flask import Flask, render_template
from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object('config')
flask load sql from file
babel = Babel(app)
db = SQLAlchemy(app)

mail = Mail(app)

def import_user_role():
    from users.models import User, Role
    return User, Role

user_datastore = SQLAlchemyUserDatastore(db, *import_user_role())
security = Security(app, user_datastore)

def init_db():
    with app.app_context():
        dump_file_dir = os.path.dirname(os.path.abspath(__name__))
        dump_file = os.path.join(dump_file_dir, 'app.sql')
        with app.open_resource(dump_file, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

########################
# Configure Secret Key #
########################
def install_secret_key(app, filename='secret_key'):
    """Configure the SECRET_KEY from a file
    in the instance directory.

    If the file does not exist, print instructions
    to create it from a shell with a random key,
    then exit.
    """
    filename = os.path.join(app.instance_path, filename)

    try:
        app.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        print('Error: No secret key. Create it with:')
        full_path = os.path.dirname(filename)
        if not os.path.isdir(full_path):
            print('mkdir -p {filename}'.format(filename=full_path))
        print('head -c 24 /dev/urandom > {filename}'.format(filename=full_path))
        sys.exit(1)

if not app.config['DEBUG']:
    install_secret_key(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.books.views import mod as books_module
app.register_blueprint(books_module)

from app.authors.views import mod as authors_module
app.register_blueprint(authors_module)
