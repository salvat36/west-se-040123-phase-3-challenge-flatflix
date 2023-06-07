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
            raise AttributeError("Must be of type string and 1--5 characters")   
    
    def reviews(self):
        return [review for review in Review.all if review.movie == self]
    
    def reviewers(self):
        return list([review.viewer for review in self.reviews() if review.movie == self])
    
    def average_rating(self):
        pass
    
    @classmethod
    def highest_rated(cls):
        pass
    
from classes.review import Review
from classes.viewer import Viewer
from statistics import mean
