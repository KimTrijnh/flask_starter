import os

POSTGRES = {
    'user': os.environ['PSQL_USER'],
    'pw': os.environ['PSQL_PWD'],
    'db': os.environ['PSQL_DB'],
    'host': os.environ['PSQL_HOST'],
    'port': os.environ['PSQL_PORT'],
}

class Config(object):
    SECRET_KEY = os.environ['SECRET_KEY'] or 'hard_to_guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
