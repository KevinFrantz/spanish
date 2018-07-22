from abc import ABC, abstractmethod
class AbstractNoun(ABC,object):
    def getNoun(self)->str:
        return self._noun
    def getGender(self):
        return self._gender
    def getArticle(self):
        return self._article
    def getPlural(self):
        return '{0}s'.format(self._noun)
