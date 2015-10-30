# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

# uses media.py
import media

# uses fresh_tomatoes.py
import fresh_tomatoes

ten_things = media.Movie("10 Things I Hate About You",
	"1999",
	"PG-13",
	"A modern adaptation of <i>The Taming of the Shrew</i>.",
	"Julia Stiles, Heath Ledger, Joseph Gordon-Levitt, Larisa Oleynik",
	"https://upload.wikimedia.org/wikipedia/en/9/95/10_Things_I_Hate_About_You_film.jpg",
	"https://www.youtube.com/watch?v=uE7qjQlfoRs")

blazing_saddles = media.Movie("Blazing Saddles",
	"1974",
	"R",
	"A corrupt politician appoints a black sheriff.",
	"Cleavon Little, Gene Wilder, Harvey Korman, Madeline Kahn, Mel Brooks",	
	"https://upload.wikimedia.org/wikipedia/en/7/7b/Blazing_saddles_movie_poster.jpg",
	"https://www.youtube.com/watch?v=iLNQv19YpG4")

coneheads = media.Movie("Coneheads",
	"1993",
	"PG",
	"Aliens from outer space are stranded on Earth.",
	"Dan Aykroyd, Jane Curtin, David Spade, Michelle Burke, Chris Farley",
	"https://upload.wikimedia.org/wikipedia/en/9/93/Coneheads_Poster.jpg",
	"https://www.youtube.com/watch?v=_Q8CpaejCk8")

dr_strangelove = media.Movie("Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb",
	"1964",
	"PG",
	"A dark comedy about the insanity of the Cold War.",
	"Peter Sellers, George C. Scott, Sterling Hayden, Slim Pickens",
	"https://upload.wikimedia.org/wikipedia/en/e/e6/Dr._Strangelove_poster.jpg",
	"https://www.youtube.com/watch?v=KdJS1iatxmY")

gattaca = media.Movie("Gattaca",
	"1997",
	"PG-13",
	"In the not-too-distant future, our DNA will determine everything about us...",
	"Ethan Hawke, Uma Thurman, Jude Law",
	"https://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster_B.jpg",
	"https://www.youtube.com/watch?v=BpzVFdDeWyo")

groundhog_day = media.Movie("Groundhog Day",
	"1993",
	"PG",
	"A weatherman finds himself living the same day over and over again.",
	"Bill Murray, Andie McDowell, Chris Elliott, Stephen Tobolowsky",
	"https://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg",
	"https://www.youtube.com/watch?v=tSVeDx9fk60")

incendies = media.Movie("Incendies",
	"2010",
	"R",
	"Twins journey to the Middle East to discover their family history, and fulfill thier mother's last wishes.",
	"Remy Girard, Melissa Desormeaux-Poulin, Maxim Gaudette, Lubna Azabal",
	"https://upload.wikimedia.org/wikipedia/en/a/a0/Incendies.jpg",
	"https://www.youtube.com/watch?v=0nycksytL1A")

king_and_i = media.Movie("The King and I",
	"1956",
	"G",
	"An English schoolteacher travels to Siam to teach the king's children.",
	"Deborah Kerr, Yul Brynner, Rita Moreno, Rex Thompson",
	"https://upload.wikimedia.org/wikipedia/en/1/17/Original_movie_poster_for_the_film_The_King_and_I.jpg",
	"https://www.youtube.com/watch?v=jfvpFluHQaA")

holy_grail = media.Movie("Monty Python and the Holy Grail",
	"1975",
	"PG",
	"King Arthur and his knights embark on a low-budget quest for the Grail, encountering many very silly obstacles.",
	"Graham Chapman, John Cleese, Eric Idle, Terry Gilliam, Terry Jones, Michael Palin, Carol Cleveland",
	"https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png",
	"https://www.youtube.com/watch?v=urRkGvhXc8w")

sound_of_music = media.Movie("The Sound of Music",
	"1965",
	"G",
	"A woman leaves an Austrian convent to become a governess to the children of a Naval officer widow.",
	"Julie Andrews, Christopher Plummer, Charmian Carr, Heather Menzies",
	"https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
	"https://www.youtube.com/watch?v=UY6uw3WpPzY")

# List of movies
movies = [ten_things, blazing_saddles, coneheads, dr_strangelove, gattaca, 
		groundhog_day, incendies, king_and_i, holy_grail, sound_of_music]

# Takes the movies list and runs it through the fresh_tomatoes.py
# open_movies_page function to generate the movies page.

fresh_tomatoes.open_movies_page(movies)