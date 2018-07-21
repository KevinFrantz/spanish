class Article(object):
    """
    This class represents an article
    """
    def __init__(self):
        self.gender = ''
    def setMale(self):
        self.gender = 'el'
    def setFemale(self):
        self.gender = 'la'
    def get(self)->str:
        return self.gender
    def getPlural(self)->str:
        if self.gender=='la':
            return '{}s'.format(self.gender)
        else:
            return 'los'
