from os import environ, path, getcwd

APP_NAME = environ.get('IDEA_APP_NAME', 'IDEA')
IP = environ.get('IDEA_IP', '127.0.0.1')
PORT = environ.get('IDEA_PORT', 5000)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = environ.get('IDEA_DATABASE_URI', 'sqlite:////{}'
                                      .format(path.join(getcwd(), 'data.db')))
