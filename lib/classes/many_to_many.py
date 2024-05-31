class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) and not (5 <= len(title) <= 50):
            print("Title must be a string between 5 and 50 characters.")
      
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title

 
class Author:
    def __init__(self, name):
        if not isinstance(name, str) and len(name) == 0:
            print("The name must be a string and not empty")
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
        pass
    
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
        pass
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        pass
    
    def topic_areas(self):
        return list(set([magazine.category for magazine in self.magazines()]))
        pass

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) and (2 <= len(name) <= 16):
            print("The name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) and len(category) == 0:
            print("The category must be a string and not empty")
        self._name = name
        self._category = category
        Magazine._all_magazines.append(self)
    
    @property
    def name(self):
        return self._name

    
    @property
    def category(self):
        return self._category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        pass
    
    def contributors(self):
        return list(set([article.author for article in self.articles()]))
        pass
    
    def article_titles(self):
        return [article.title for article in self.articles()]
        pass
    
    def contributing_authors(self):
        pass
    
  