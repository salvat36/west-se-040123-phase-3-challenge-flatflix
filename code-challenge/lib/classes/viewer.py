class Viewer:

    all = []
    
    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 6<= len(username) <=16:
            self._username = username
        else:
            raise AttributeError("Must be of type string and between 6-16 characters")
    
    def reviews(self):
        return [review for review in Review.all if review.viewer == self]
    
    def reviewed_movies(self):
        return [review.movie for review in self.reviews() if review.viewer == self]

#if there is a Review instance that has this Viewer and Movie
    def has_reviewed_movie(self, movie):
        if self.movie == movie.review:
            return True

from classes.review import Review
from classes.movie import Movie