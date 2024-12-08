import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'The-most-difficult-key-ever-666'
