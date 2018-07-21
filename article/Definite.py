class Definite(object):
    """
    This class represents an definite article
    """
    def __init__(self,article):
        self.article = article
    def getSingular(self)->str:
        if self.article == 'masculino':
            return 'el'
        return 'la'
    def getPlural(self)->str:
        if self.article.getGender() == 'masculino':
            return 'los'
        return 'las'
