"""
generator.py

This is the actual generator.
"""

from random import seed, random

class KeywordGenerator(object):
    """
    The generator class
    """
    def __init__(self, keywords):
        self.keywords = keywords

    def generate(self, words=5):
        """
        Generates a list of keywords.
        """
        seed()
        return sorted(self.keywords, key=lambda *args: random())[0:words]

