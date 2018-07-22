from .AbstractNoun import AbstractNoun
from article.Article import Article

class Irregular(AbstractNoun):
    """
    This class represents an irregular noun.
    """
    def __init__(self,noun:str,article:Article):
        self._noun = noun
        self._article = article
