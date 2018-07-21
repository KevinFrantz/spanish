from article.Article import Article
"""
    Overview over the articles:
"""
print ('artìculo:')
article = Article()
def articleSpecific(article:Article,kind:str):
    print('artículo {0}: {1}'.format(kind,article.getSingular()))
    print('artículo {0}: {1}'.format(kind,article.getPlural()))
def articleOverview(article:Article,gender:str):
    print ('{}:'.format(gender))
    articleSpecific(article.getDefinite(),'específico')
    articleSpecific(article.getUndefinite(),'indefinido')
article.setMale()
articleOverview(article,'masculino')
article.setFemale()
articleOverview(article,'feminimo')
