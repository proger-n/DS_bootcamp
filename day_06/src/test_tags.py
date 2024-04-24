import pytest
from movielens_analysis import Tags


@pytest.fixture
def tags():
    return Tags('data/tags.csv')


def test_most_words(tags):
    top_n_tags = tags.most_words(5)
    assert isinstance(top_n_tags, dict)
    assert all(isinstance(tag, str) for tag in top_n_tags.keys())
    assert all(isinstance(count, int) for count in top_n_tags.values())
    assert sorted(top_n_tags.items(), key=lambda x: x[1], reverse=True) == list(
        top_n_tags.items())


def test_longest(tags):
    top_n_tags = tags.longest(5)
    assert isinstance(top_n_tags, list)
    assert all(isinstance(tag, str) for tag in top_n_tags)
    assert sorted(top_n_tags, key=lambda x: len(x), reverse=True) == top_n_tags


def test_most_words_and_longest(tags):
    intersection_tags = tags.most_words_and_longest(5)
    assert isinstance(intersection_tags, list)
    assert all(isinstance(tag, str) for tag in intersection_tags)


def test_most_popular(tags):
    top_n_tags = tags.most_popular(5)
    assert isinstance(top_n_tags, dict)
    assert all(isinstance(tag, str) for tag in top_n_tags.keys())
    assert all(isinstance(count, int) for count in top_n_tags.values())
    assert sorted(top_n_tags.items(), key=lambda x: x[1], reverse=True) == list(
        top_n_tags.items())


def test_tags_with(tags):
    tags_with_word = tags.tags_with('python')
    assert isinstance(tags_with_word, list)
    assert all(isinstance(tag, str) for tag in tags_with_word)
    assert tags_with_word == sorted(tags_with_word)
