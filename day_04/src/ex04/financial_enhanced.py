# python3 -m cProfile -s time financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-http.txt
# python3 -m cProfile -s ncalls financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-ncalls.txt
# python3 financial_enhanced.py 'MSFT' 'Total Revenue' > pstats-cumulative.txt

import httpx
from bs4 import BeautifulSoup
import sys
import pstats
import profile


def fetch_financial_data(ticker, breakdown):
    """Fetches financial data for a given ticker and breakdown from Yahoo Finance."""
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    headers = {'User-Agent': 'Custom'}
    response = httpx.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    if title == 'Symbol Lookup from Yahoo Finance':
        raise ValueError('Invalid ticker symbol')

    tags = soup.find_all(attrs={'data-test': 'fin-row'})
    breakdowns = [tag.find(class_='Va(m)').get_text() for tag in tags]
    if breakdown not in breakdowns:
        raise ValueError('Breakdown not found')

    data = tuple(t.get_text()
                 for t in tags[breakdowns.index(breakdown)].find_all('span'))
    print(data)
    return


def main():
    if len(sys.argv) != 3:
        raise ValueError("Expected 2 arguments: ticker symbol and breakdown")

    ticker, breakdown = sys.argv[1], sys.argv[2]
    try:
        fetch_financial_data(ticker, breakdown)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        p = profile.Profile()
        p.run("main()")

        s = pstats.Stats(p)
        s.sort_stats("cumtime").print_stats(5)
    except Exception as err:
        print(type(err).__name__, err, sep=': ')
