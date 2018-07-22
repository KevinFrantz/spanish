from .Irregular import Irregular
from gender.Male import Male
from article.Article import Article

class IrregularMale(Irregular):
    """
    This class represents a word, which ends on a, but is Male
    """
    def __init__(self,noun:str):
        super().__init__(noun,Article(Male()))
    def getWords()->list:
        return ['problema','dìa','mapa','idioma']
