from .Definite import Definite
from .Undefinite import Undefinite
from gender.Gender import Gender

class Article(object):
    """
    This class represents the ruleset of an article
    """
    def __init__(self,gender:Gender):
        self.__gender = gender
        self.__definite = Definite(self)
        self.__undefinite = Undefinite(self)
    def getGender(self):
        return self.__gender
    def getDefinite(self)->str:
        return self.__definite
    def getUndefinite(self)->str:
        return self.__undefinite
