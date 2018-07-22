from .Irregular import Irregular
from gender.Female import Female
from article.Article import Article

class IrregularFemale(Irregular):
    """
    This class represents a word, which ends on o, but is female
    """
    def __init__(self,noun:str):
        super().__init__(noun,Article(Female()))
    @staticmethod
    def getWords()->list:
        return ['moto','mano','foto','radio']
