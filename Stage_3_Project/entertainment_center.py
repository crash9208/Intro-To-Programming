# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media #imports the class media
import fresh_tomatoes #imports the fresh_tomatoes files

#five movies, who use the media class and fill them with inputs like title, trailer, description and movie poster

babylon = media.Movie("Babylon A.D.", "A hero in a dark future", "babylon-ad-movie-poster-2008-1020413823.jpg", "https://www.youtube.com/watch?v=ylxl2UWMq_4")

avatar = media.Movie("Avatar", "A marine on an alien planet", "Unknown.jpeg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")

inception = media.Movie("Inception", "A thief in your dreams", "Inception_(2010)_theatrical_poster.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")

jason_bourne = media.Movie("Jason Bourne", "A spy with amnesia", "images.jpeg", "https://www.youtube.com/watch?v=F4gJsKZvqE4")

shooter = media.Movie("Shooter", "A sniper fights against corrupt politicians","Unknown-1.jpeg","https://www.youtube.com/watch?v=6ZVcPhDt-kM")

movies = [babylon, avatar, inception, jason_bourne, shooter] #the list which contains the movies
fresh_tomatoes.open_movies_page(movies) #calls the function which creates the movie page and opens it
