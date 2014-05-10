import media
import fresh_tomatoes
now_you_see_me = media.Movie("Now you see me","This is great entertaining suspense movie","http://www.youtube.com/watch?v=8MHDYZJWLXA","http://upload.wikimedia.org/wikipedia/en/c/c7/Now_You_See_Me_Poster.jpg")

# now_you_see_me.show_trailer()

movie_list = [now_you_see_me]
fresh_tomatoes.open_movies_page(movie_list)
