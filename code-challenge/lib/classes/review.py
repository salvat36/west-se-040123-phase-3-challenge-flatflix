class Review:

    all = []
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        type(self).all.append(self)
    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1<= rating <=5:
            self._rating = rating
        else:
            raise AttributeError("Must be a number between 1-5 characters")
    
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise AttributeError("Must be a Viewer instance")
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise AttributeError("Must be a Movie instance")
    
    
from classes.movie import Movie
from classes.viewer import Viewer