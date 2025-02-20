class Movie:

    all = []
    
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise AttributeError("Must be of type string and at least 1 character")   
    
    def reviews(self):
        return [review for review in Review.all if review.movie == self]
    
    def reviewers(self):
        return list([review.viewer for review in self.reviews() if review.movie == self])
    
    def average_rating(self):
        return mean([review.rating for review in self.reviews()])
    
    @classmethod
    def highest_rated(cls):
        return max(cls.all, key=lambda el: el.average_rating())
    
from classes.review import Review
from classes.viewer import Viewer
from statistics import mean
