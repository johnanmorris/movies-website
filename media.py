# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Movie():
    ''' This class provides a way to store movie-related information.'''

    # initialize instance of class Movie
    def __init__(self, movie_title, release_year, rating,
                movie_storyline, actors, poster_image,
                trailer_youtube,):
        self.title = movie_title
        self.release_year = release_year
        self.rating = rating
        self.storyline = movie_storyline
        self.actors = actors
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube