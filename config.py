import os

class Config(object):
    '''
    As the application needs more configuration items, they can be added to this class, and later if I find that I need to have more than one configuration set, I can create subclasses of it.'''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'