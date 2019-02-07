import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Whether or not to signal the application everytime a change to the database is about to
                                           # be m
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'd??R???kq@XJD=?'
