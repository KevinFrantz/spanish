class Definite(object):
    """
    This class represents an definite article
    """
    def __init__(self,article:object):
        self.article = article
    def getSingular(self)->str:
        if self.article.getGender().isMale():
            return 'el'
        return 'la'
    def getPlural(self)->str:
        if self.article.getGender().isMale():
            return 'los'
        return 'las'
