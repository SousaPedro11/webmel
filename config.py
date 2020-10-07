import os


class Config:
    THREADED = True
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(16))
