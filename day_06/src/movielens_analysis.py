import os
import sys
import urllib
import requests
from bs4 import BeautifulSoup
import json
import pytest
import collections
import functools
import datetime
import re
from collections import defaultdict, Counter, OrderedDict
import csv
import statistics
from datetime import datetime


class Tags:
    """
    Analyzing data from tags.csv
    """

    def __init__(self, path_to_the_file):
        self.path_to_the_file = path_to_the_file

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
 where the keys are tags and the values are the number of words inside the tag.
 Drop the duplicates. Sort it by numbers descendingly.
        """
        tag_word_count = defaultdict(int)

        with open(self.path_to_the_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tag = row['tag']
                words = tag.split()
                tag_word_count[tag] = max(tag_word_count[tag], len(words))

        sorted_tags = sorted(tag_word_count.items(),
                             key=lambda x: x[1], reverse=True)
        top_n_tags = dict(sorted_tags[:n])
        return top_n_tags

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        tag_lengths = defaultdict(int)

        with open(self.path_to_the_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tag = row['tag']
                tag_lengths[tag] = max(tag_lengths[tag], len(tag))

        sorted_tags = sorted(tag_lengths.keys(),
                             key=lambda x: len(x), reverse=True)
        top_n_tags = sorted_tags[:n]

        return top_n_tags

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        most_words_tags = set(self.most_words(n).keys())
        longest_tags = set(self.longest(n))

        intersection_tags = most_words_tags.intersection(longest_tags)

        return list(intersection_tags)

    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        tag_counts = defaultdict(int)

        with open(self.path_to_the_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tag = row['tag']
                tag_counts[tag] += 1

        sorted_tags = sorted(tag_counts.items(),
                             key=lambda x: x[1], reverse=True)
        top_n_tags = dict(sorted_tags[:n])

        return top_n_tags

    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        tags_with_word = set()

        with open(self.path_to_the_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tag = row['tag']
                if word.lower() in tag.lower():
                    tags_with_word.add(tag)

        sorted_tags = sorted(tags_with_word)

        return sorted_tags


class Movies:
    """
    Analyzing data from movies.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path_to_the_file = path_to_the_file
        self.movies = []
        with open(path_to_the_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.movies.append(row)

    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts. 
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        release_years = Counter()
        for movie in self.movies:
            year = movie['title'].rstrip()[-5:-1]
            try:
                year = int(year)
                release_years[year] += 1
                sorted_release_years = dict(
                    sorted(release_years.items(), key=lambda item: item[1], reverse=True))
            except ValueError:
                continue
        return sorted_release_years

    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
     Sort it by counts descendingly.
        """
        genres = Counter()
        for movie in self.movies:
            for genre in movie['genres'].split('|'):
                genres[genre.strip()] += 1
        sorted_genres = dict(
            sorted(genres.items(), key=lambda item: item[1], reverse=True))
        return sorted_genres

    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and 
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        movies_by_genres = {}
        for movie in self.movies:
            genres_count = len(movie['genres'].split('|'))
            movies_by_genres[movie['title']] = genres_count
        sorted_movies = dict(
            sorted(movies_by_genres.items(), key=lambda item: item[1], reverse=True)[:n])
        return sorted_movies

    def longest_titles(self):
        longest_titles = Counter()
        for movie in self.movies:
            longest_titles[movie['title']] = len(movie['title'])
        return OrderedDict(sorted(longest_titles.items(), key=lambda x: x[1], reverse=True))


class Ratings:
    """
    Analyzing data from ratings.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path_to_the_file = path_to_the_file

    class Movies:
        def __init__(self, path_to_the_file):
            """
            Initialize the Movies class with the path to the ratings.csv file.
            """
            self.path_to_the_file = path_to_the_file
            self.data = []
            with open(path_to_the_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    ts = datetime.fromtimestamp(int(row['timestamp']))
                    row['timestamp'] = datetime.strptime(
                        str(ts), '%Y-%m-%d %H:%M:%S')
                    self.data.append(row)

        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            ratings_by_year = {}
            with open(self.path_to_the_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    timestamp = int(row[3])
                    year = datetime.fromtimestamp(timestamp).year
                    ratings_by_year[year] = ratings_by_year.get(year, 0) + 1
            return ratings_by_year

        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
         Sort it by ratings ascendingly.
            """
            ratings_distribution = {}
            with open(self.path_to_the_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    rating = float(row[2])
                    ratings_distribution[rating] = ratings_distribution.get(
                        rating, 0) + 1
            return ratings_distribution

        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings. 
            It is a dict where the keys are movie titles and the values are numbers.
     Sort it by numbers descendingly.
            """
            movie_ratings = defaultdict(int)
            for row in self.data:
                movie_ratings[row['movieId']] += 1
            top_movies = dict(sorted(movie_ratings.items(),
                              key=lambda item: item[1], reverse=True)[:n])
            return top_movies

        def top_by_ratings(self, n, metric='average'):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            top_movies = {}
            with open(self.path_to_the_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                movie_ratings = {}
                for row in reader:
                    movie_id = row[1]
                    rating = float(row[2])
                    if movie_id not in movie_ratings:
                        movie_ratings[movie_id] = []
                    movie_ratings[movie_id].append(rating)
                for movie_id, ratings in movie_ratings.items():
                    if metric == 'average':
                        metric_value = round(statistics.mean(ratings), 2)
                    elif metric == 'median':
                        metric_value = round(statistics.median(ratings), 2)
                    top_movies[movie_id] = metric_value
            top_movies = dict(
                sorted(top_movies.items(), key=lambda x: x[1], reverse=True)[:n])
            return top_movies

        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
          Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            movie_variances = defaultdict(list)
            for row in self.data:
                movie_variances[row['movieId']].append(
                    int(float(row['rating'])))
            top_movies = {}
            for movie, ratings in movie_variances.items():
                variance = sum((xi - sum(ratings) / len(ratings))
                               ** 2 for xi in ratings) / len(ratings)
                top_movies[movie] = round(variance, 2)
            top_movies = dict(
                sorted(top_movies.items(), key=lambda item: item[1], reverse=True)[:n])
            return top_movies

    class Users:
        """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
     Inherit from the class Movies. Several methods are similar to the methods from it.
        """

        def __init__(self, path_to_the_file):
            self.data = []
            with open(path_to_the_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    ts = datetime.fromtimestamp(int(row['timestamp']))
                    row['timestamp'] = datetime.strptime(
                        str(ts), '%Y-%m-%d %H:%M:%S')
                    self.data.append(row)

        def dist_by_num_of_ratings(self):
            user_ratings = defaultdict(int)
            for row in self.data:
                user_ratings[row['userId']] += 1
            return dict(sorted(user_ratings.items()))

        def dist_by_average_rating(self):
            user_ratings = defaultdict(list)
            for row in self.data:
                user_ratings[row['userId']].append(int(float(row['rating'])))
            user_averages = {}
            for user, ratings in user_ratings.items():
                avg_rating = round(sum(ratings) / len(ratings), 2)
                user_averages[user] = avg_rating
            return dict(sorted(user_averages.items(), key=lambda item: item[1], reverse=True))

        def top_variance(self, n):
            user_ratings = defaultdict(list)
            for row in self.data:
                user_ratings[row['userId']].append(int(float(row['rating'])))
            user_variances = {}
            for user, ratings in user_ratings.items():
                variance = round(
                    sum((x - sum(ratings) / len(ratings)) ** 2 for x in ratings) / len(ratings), 2)
                user_variances[user] = variance
            user_variances = dict(
                sorted(user_variances.items(), key=lambda item: item[1], reverse=True)[:n])
            return user_variances


class Links:
    """
    Analyzing data from links.csv
    """

    def get_imdb(self, list_of_movies, list_of_fields):
        """
        The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
        Sort it by movieId descendingly.
        """
        imdb_info = []
        for movie_id in list_of_movies:
            imdb_url = f"https://www.imdb.com/title/tt{movie_id}/"
            response = requests.get(imdb_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            movie_info = [movie_id]
            for field in list_of_fields:
                if field == "Director":
                    director = soup.find(
                        "div", class_="credit_summary_item").find("a").text.strip()
                    movie_info.append(director)
                else:
                    value = soup.find("h4", string=field).find_next(
                        "span").text.strip()
                    movie_info.append(value)
            imdb_info.append(movie_info)

        imdb_info.sort(reverse=True)
        return imdb_info

    def top_directors(self, n):
        """
        The method returns a dict with top-n directors where the keys are directors and 
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        directors = {}
        imdb_url = "https://www.imdb.com/chart/top"
        response = requests.get(imdb_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.find_all("td", class_="titleColumn")
        for movie in movies:
            director = movie.find("a").text.strip()
            if director in directors:
                directors[director] += 1
            else:
                directors[director] = 1

        top_directors = dict(
            sorted(directors.items(), key=lambda x: x[1], reverse=True)[:n])
        return top_directors

    def most_expensive(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """
        budgets = {}
        imdb_url = "https://www.imdb.com/chart/top"
        response = requests.get(imdb_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.find_all("td", class_="titleColumn")
        for movie in movies:
            title = movie.find("a").text.strip()
            budget = movie.find_next(
                "span", class_="secondaryInfo").text.strip()
            budgets[title] = budget

        top_budgets = dict(
            sorted(budgets.items(), key=lambda x: x[1], reverse=True)[:n])
        return top_budgets

    def most_profitable(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
        Sort it by the difference descendingly.
        """
        profits = {}
        imdb_url = "https://www.imdb.com/chart/top"
        response = requests.get(imdb_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.find_all("td", class_="titleColumn")
        for movie in movies:
            title = movie.find("a").text.strip()
            gross = movie.find_next("span", class_="secondaryInfo").find_next(
                "span", class_="secondaryInfo").text.strip()
            budget = movie.find_next(
                "span", class_="secondaryInfo").text.strip()
            profit = int(gross.replace(",", "").replace("$", "")) - \
                int(budget.replace(",", "").replace("$", ""))
            profits[title] = profit

        top_profits = dict(
            sorted(profits.items(), key=lambda x: x[1], reverse=True)[:n])
        return top_profits

    def longest(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version – choose any.
        Sort it by runtime descendingly.
        """
        runtimes = {}
        imdb_url = "https://www.imdb.com/chart/top"
        response = requests.get(imdb_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.find_all("td", class_="titleColumn")
        for movie in movies:
            title = movie.find("a").text.strip()
            runtime = movie.find_next("span", class_="runtime").text.strip()
            runtimes[title] = runtime

        top_runtimes = dict(sorted(runtimes.items(), key=lambda x: int(
            x[1].split(" ")[0]), reverse=True)[:n])
        return top_runtimes

    def top_cost_per_minute(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the budgets divided by their runtime. The budgets can be in different currencies – do not pay attention to it.
        The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """
        costs = {}
        imdb_url = "https://www.imdb.com/chart/top"
        response = requests.get(imdb_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.find_all("td", class_="titleColumn")
        for movie in movies:
            title = movie.find("a").text.strip()
            budget = movie.find_next(
                "span", class_="secondaryInfo").text.strip()
            runtime = movie.find_next("span", class_="runtime").text.strip()
            budget_value = float(budget.replace(",", "").replace("$", ""))
            runtime_value = int(runtime.split(" ")[0])
            cost_per_minute = round(budget_value / runtime_value, 2)
            costs[title] = cost_per_minute

        top_costs = dict(
            sorted(costs.items(), key=lambda x: x[1], reverse=True)[:n])
        return top_costs
