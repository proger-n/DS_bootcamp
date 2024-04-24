import requests
from bs4 import BeautifulSoup
import sys
import time


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

    time.sleep(5)  # To avoid rate limiting
    data = tuple(t.get_text()
                 for t in tags[breakdowns.index(breakdown)].find_all('span'))
    return data


def main():
    if len(sys.argv) != 3:
        raise ValueError("Expected 2 arguments: ticker symbol and breakdown")

    ticker, breakdown = sys.argv[1], sys.argv[2]
    try:
        data = fetch_financial_data(ticker, breakdown)
        print(data)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
