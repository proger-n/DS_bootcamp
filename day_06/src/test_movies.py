import csv
from collections import Counter
from movielens_analysis import Movies


def test_init():
    movies = Movies('data/movies.csv')
    assert isinstance(movies.movies, list)
    assert len(movies.movies) > 0


def test_dist_by_release():
    movies = Movies('data/movies.csv')
    dist = movies.dist_by_release()
    assert isinstance(dist, dict)
    assert all(isinstance(year, int) for year in dist.keys())
    assert all(isinstance(count, int) for count in dist.values())
    assert sorted(dist.items(), key=lambda item: item[1], reverse=True) == list(
        dist.items())


def test_dist_by_genres():
    movies = Movies('data/movies.csv')
    dist = movies.dist_by_genres()
    assert isinstance(dist, dict)
    assert all(isinstance(genre, str) for genre in dist.keys())
    assert all(isinstance(count, int) for count in dist.values())
    assert sorted(dist.items(), key=lambda item: item[1], reverse=True) == list(
        dist.items())


def test_most_genres():
    movies = Movies('data/movies.csv')
    n = 5
    most_genres = movies.most_genres(n)
    assert isinstance(most_genres, dict)
    assert len(most_genres) == n
    assert all(isinstance(title, str) for title in most_genres.keys())
    assert all(isinstance(count, int) for count in most_genres.values())
    assert sorted(most_genres.items(), key=lambda item: item[1], reverse=True) == list(
        most_genres.items())


def test_longest_titles():
    movies = Movies('data/movies.csv')
    dist = movies.longest_titles()
    assert isinstance(dist, dict)
