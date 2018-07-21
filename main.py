from article.Article import Article
from gender.Gender import Gender
from gender.Male import Male
from gender.Female import Female
from noun.Noun import Noun

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
print ('\nSubstantivos:\n')
def printNoun(name:str):
    noun = Noun(name)
    print('{0}:'.format(name));
    print ('específico singular\t{0} {1}'.format(noun.getArticle().getDefinite().getSingular(),noun.getNoun()))
    print ('específico plural\t{0} {1}'.format(noun.getArticle().getDefinite().getPlural(),noun.getPlural()))
    print ('indefinido singular\t{0} {1}'.format(noun.getArticle().getUndefinite().getSingular(),noun.getNoun()))
    print ('indefinido plural\t{0} {1}'.format(noun.getArticle().getUndefinite().getPlural(),noun.getPlural()))
    print()
print('Substantivos regulares:\n')
for name in ['libro','casa']:
    printNoun(name)
