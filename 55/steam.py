from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple("Game", "title link")


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""

    data = feedparser.parse(FEED_URL)

    game_list = []

    for entry in data.entries:
        title = entry.title
        link_ = entry.link

        game_list.append(Game(title=title, link=link_))

    return game_list
