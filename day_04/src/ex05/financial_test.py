import requests
from bs4 import BeautifulSoup
import sys
import time
import pytest


def fetch_financial_data(ticker, breakdown):
    """Fetches financial data for a given ticker and breakdown from Yahoo Finance."""
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    if title == 'Symbol Lookup from Yahoo Finance':
        raise ValueError('Invalid ticker symbol')

    tags = soup.find_all(attrs={'data-test': 'fin-row'})
    breakdowns = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if breakdown not in breakdowns:
        raise ValueError('Breakdown not found')

    time.sleep(5)
    data = tuple(t.get_text()
                 for t in tags[breakdowns.index(breakdown)].find_all('span'))
    return data


def test_parse_valid_ticker():
    ticker = 'AAPL'
    breakdown = 'Total Revenue'
    data = fetch_financial_data(ticker, breakdown)
    assert isinstance(data, tuple)
    assert len(data) > 0
    print("test 1 passed")


def test_parse_invalid_ticker():
    ticker = 'INVALID'
    breakdown = 'Total Revenue'
    with pytest.raises(ValueError):
        fetch_financial_data(ticker, breakdown)
    print("test 2 passed")


def test_parse_invalid_breakdown():
    ticker = 'AAPL'
    breakdown = 'Invalid'
    with pytest.raises(ValueError):
        fetch_financial_data(ticker, breakdown)
    print("test 3 passed")


def tests():
    test_parse_valid_ticker()
    test_parse_invalid_ticker()
    test_parse_invalid_breakdown()


if __name__ == "__main__":
    tests()
