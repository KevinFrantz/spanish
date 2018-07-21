class Gender(object):
    """
        Represents a gender
    """
    def __init__(self):
        self.__gender = None
    def setMale(self):
        self.__gender = 'masculino'
    def setFemale(self):
        self.__gender = 'feminimo'
    def isMale(self):
        return (self.__gender == 'masculino')
    def isFemale(self):
        return (self.__gender == 'feminimo')
    def getName(self)->str:
        return self.__gender
