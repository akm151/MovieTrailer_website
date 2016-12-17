import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=vwyZH85NQC4"
                      )
#print(toy_story.storyline)
avatar=media.Movie("Avatar",
                   "A marine on an alien planet",
                   "http://www.impawards.com/2009/posters/avatar.jpg",
                   "https://www.youtube.com/watch?v=d1_JBMrrYw8"
                   )
#print(avatar.storyline)
movies=[toy_story,avatar]
#avatar.show_trailer()
fresh_tomatoes.open_movies_page(movies)
