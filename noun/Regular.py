from gender.Female import Female
from gender.Male import Male
from article.Article  import Article
from .AbstractNoun import AbstractNoun
class Regular(AbstractNoun):
    """
    This class represents a noun.
    """
    def __init__(self,noun:str):
        super(Regular).__init__()
        self._noun = noun
        self._gender = None
        self.__setGenderRoutine()
        self._article = Article(self._gender)
    def __setGenderRoutine(self):
        last_letter = self._noun[-1:]
        if last_letter == 'a':
            self._gender = Female()
            return
        if last_letter == 'o':
            self._gender = Male()
            return
        raise Exception('The gender could not be defined!')
