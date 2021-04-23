import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []

    for file in files:
        with open(file, "r") as open_json:
            data = open_json.read()
            movies.append(json.loads(data))

    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""

    for movie in movies:
        if "comedy" in movie["Genre"].lower():
            return movie["Title"]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    most_nominations = 0
    movie_most_nominations = None

    for movie in movies:
        current_nominations = int(movie["Awards"].split(" wins & ")[1].split(" ")[0])

        if current_nominations > most_nominations:
            most_nominations = current_nominations
            movie_most_nominations = movie["Title"]

    return movie_most_nominations


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    longest_runtime = 0
    movie_longest_runtime = None

    for movie in movies:
        current_runtime = int(movie["Runtime"].split(" ")[0])

        if current_runtime > longest_runtime:
            longest_runtime = current_runtime
            movie_longest_runtime = movie["Title"]

    return movie_longest_runtime
