from .DoubleGender import DoubleGender
from .IrregularMale import IrregularMale
from .IrregularFemale import IrregularFemale
from .Regular import Regular

class Controller(object):
    """
    This controller decide which kind of noun exists
    """
    def __init__(self,name:str):
        self.__name = name
        self.__noun = None
        self.__strategy()
    def __strategy(self):
        if not self.__doubleGender():
            if not self.__irregularMale():
                if not self.__irregularFemale():
                    self.__regular()
    def getNoun(self):
        return self.__noun
    def __doubleGender(self):
        for end in DoubleGender.getEndings():
            if self.__name.endswith(end):
                self.__noun = DoubleGender(self.__name)
                return True
        return False
    def __irregularMale(self):
        if self.__name in IrregularMale.getWords():
            self.__noun = IrregularMale(self.__name)
            return True
        return False
    def __irregularFemale(self):
        if self.__name in IrregularFemale.getWords():
            self.__noun = IrregularFemale(self.__name)
            return True
        return False
    def __regular(self):
        self.__noun = Regular(self.__name)
        return True
