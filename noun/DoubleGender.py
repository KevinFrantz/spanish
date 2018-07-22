from .Irregular import Irregular
from gender.Male import Male
from gender.Female import Female
from article.Article import Article
class DoubleGender(Irregular):
    """
    This class represents words which contain two genders
    """
    def __init__(self,noun:str):
        super(self).__init__(noun,Male())
        self.__second_article = Female()
    def getSecondArticle(self)->Article:
        return self.__second_article
    @staticmethod
    def getEndings()->list:
        return ['ista','ante']
