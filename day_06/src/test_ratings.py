import pytest
from movielens_analysis import Ratings


class TestMovies:
    @pytest.fixture
    def movies_instance(self):
        return Ratings.Movies('data/ratings.csv')

    def test_dist_by_year(self, movies_instance):
        result = movies_instance.dist_by_year()
        assert isinstance(result, dict)

    def test_dist_by_rating(self, movies_instance):
        result = movies_instance.dist_by_rating()
        assert isinstance(result, dict)

    def test_top_by_num_of_ratings(self, movies_instance):
        result = movies_instance.top_by_num_of_ratings(5)
        assert isinstance(result, dict)

    def test_top_by_ratings(self, movies_instance):
        result = movies_instance.top_by_ratings(5)
        assert isinstance(result, dict)

    def test_top_controversial(self, movies_instance):
        result = movies_instance.top_controversial(5)
        assert isinstance(result, dict)


class TestUsers:
    @pytest.fixture
    def users_instance(self):
        return Ratings.Users('data/ratings.csv')

    def test_dist_by_num_of_ratings(self, users_instance):
        result = users_instance.dist_by_num_of_ratings()
        assert isinstance(result, dict)

    def test_dist_by_average_rating(self, users_instance):
        result = users_instance.dist_by_average_rating()
        assert isinstance(result, dict)
