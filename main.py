from article.Article import Article
from gender.Gender import Gender
from gender.Male import Male
from gender.Female import Female
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
