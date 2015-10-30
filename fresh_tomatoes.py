""""derived from Udacity's fresh_tomatoes.py
Edits made by J. Noelle Morris"""

import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>The Best Movies Ever!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

    <!-- Web Font -->
    <link href='https://fonts.googleapis.com/css?family=Special+Elite' rel='stylesheet' type='text/css'>

    <style type="text/css" media="screen">
        body {
            padding-top: 10em;
            background-color: #FBEED3;
            color: #429398;
            font-family: 'Special Elite', cursive;
        }

        .navbar {
            background-color: #6B5D4D;
            font-weight: bold;
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }

        .hanging-close {
            position: absolute;
            top: -13px;
            right: -13px;
            z-index: 9001;
            color: #6B5D4D;
            background-color: #B0A18F;
            border-radius: 100%;
            border: 3px solid #6B5D4D;
            padding: 5px;
        }

        .hanging-close:hover{
            color: #429398;
        }

        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            padding-top: 20px;
            height: 45em;
        }

        .movie-tile:hover {
            background-color: #DFCDB4;
            cursor: pointer;
            border-radius: 45px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: 2px solid;
            border-color: #429398;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: #DFCDB4;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
    <body>
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
            <div class="modal-dialog">
                <div class="modal-content">
                    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                        <span class="glyphicon glyphicon-remove"></span>
                    </a>
                    <div class="scale-media" id="trailer-video-container">
                    </div>
                </div>
            </div>
        </div>

    <!-- Main Page Content -->
        <div class="container">
            <div class="navbar navbar-fixed-top" role="navigation">
                <div class="container">
                    <div class="text-left h1">
                        The Best Movies Ever!
                    </div>
                    <div class="text-right h3">
                        a list by Noelle Morris
                    </div>
                </div>
            </div>
        </div>
        <div class="container">
            <p class="lead text-center">The following movies are just a few of the
            best of all time! Well &hellip; at least according to me.</p>
            <p class="lead text-center">To check out a movie&rsquo;s trailer, click the movie poster. Enjoy!</p>
        </div>
        <div class="container-fluid">
            {movie_tiles}
        </div>
    </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-3 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342" class="img-rounded">
    <h2>{movie_title}</h2>
    <h3>({release_year}, {rating})</h3>
    <h4>Synopsis: {storyline}</h4>
    <h5>Starring: {actors}</h5>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title = movie.title,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            release_year = movie.release_year,
            storyline = movie.storyline,
            actors = movie.actors,
            rating = movie.rating)
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

