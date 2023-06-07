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
    
    #returns a list of all reviews for a specific viewer(self)
    def reviews(self):
        return [review for review in Review.all if review.viewer == self]
    
    #returns a list of all reviewed movies for a specific viewer(self)
    def reviewed_movies(self):
        return [review.movie for review in self.reviews() if review.viewer == self]

#if there is a Review instance that has this Viewer and Movie
#review.movie AND review.viewer  NEEDS review.viewer == self
#review holds both viewer and movie
#checking to see if the passed movie is a reviewed movie
    def has_reviewed_movie(self, movie):
        if movie in self.reviewed_movies():
            return True
        else:
            return False
        

from classes.review import Review
from classes.movie import Movie