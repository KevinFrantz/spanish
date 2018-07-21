from article.Article import Article
"""
    Overview over the articles:
"""
print ('Article:')
article = Article()
def articleOverview(article:Article,gender:str):
    print ('{}:'.format(gender))
    print(article.get())
    print(article.getPlural())
article.setMale()
articleOverview(article,'male')
article.setFemale()
articleOverview(article,'female')
