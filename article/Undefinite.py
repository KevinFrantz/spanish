class Undefinite(object):
    """
    This class represents an undefinite article
    """
    def __init__(self,article):
        self.article = article
    def getSingular(self)->str:
        if self.article.getGender() == 'masculino':
            return 'un'
        return 'una'
    def getPlural(self)->str:
        if self.article.getGender() == 'masculino':
            return 'unos'
        return 'unas'
