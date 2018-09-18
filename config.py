import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    '''
    As the application needs more configuration items, they can be added to this class, and later if I find that I need to have more than one configuration set, I can create subclasses of it.'''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #.., configurtin fo 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

