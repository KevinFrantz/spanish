from article.Article import Article
from gender.Gender import Gender
from gender.Male import Male
from gender.Female import Female
from noun.Controller import Controller as NounController

"""
    Overview over the articles:
"""
print ('artìculo:\n')
def articleSpecific(article:Article,kind:str):
    print('artículo {0} singular:\t{1}'.format(kind,article.getSingular()))
    print('artículo {0} plural:\t{1}'.format(kind,article.getPlural()))
def articleOverview(article:Article):
    print ('{}:'.format(article.getGender().getName()))
    articleSpecific(article.getDefinite(),'específico')
    articleSpecific(article.getUndefinite(),'indefinido')
    print()
articleOverview(Article(Female()))
articleOverview(Article(Male()))
"""
    Overview over the Nouns
"""
print ('\nsubstantivos:\n')
def printNoun(name:str):
    nounController = NounController(name)
    noun = nounController.getNoun()
    print('{0}:'.format(name));
    print ('específico singular\t{0} {1}'.format(noun.getArticle().getDefinite().getSingular(),noun.getNoun()))
    print ('específico plural\t{0} {1}'.format(noun.getArticle().getDefinite().getPlural(),noun.getPlural()))
    print ('indefinido singular\t{0} {1}'.format(noun.getArticle().getUndefinite().getSingular(),noun.getNoun()))
    print ('indefinido plural\t{0} {1}'.format(noun.getArticle().getUndefinite().getPlural(),noun.getPlural()))
    print()
print('substantivos regulares:\n')
for name in ['libro','casa']:
    printNoun(name)
print('substantivos irregulares:\n')
for name in ['moto','mano','foto','radio','problema','dìa','mapa','idioma']:
    printNoun(name)
print('substantivos de dos generòs:\n')
for name in ['periodista','cantante']:
    printNoun(name)
