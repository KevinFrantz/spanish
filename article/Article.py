class Article:
    """
    This class represents an article
    """
    def __init__(self):
        self.gender = ''
    def setMale(self):
        self.gender = 'el'
    def setFemale(self):
        self.gender = 'la'
    def get(self):
        return self.gender
    def getPlural(self):
        if[self.gender=='la']:
            return self.gender + 's'
        else:
            return 'los'
