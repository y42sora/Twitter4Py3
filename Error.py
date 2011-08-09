__author__ = 'y42sora'

class PyTwiError(Exception):
    message = ""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return message
    