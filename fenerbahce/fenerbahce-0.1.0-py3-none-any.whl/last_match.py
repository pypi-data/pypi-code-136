from fenerbahce.crawler import Crawler


def last_match():
    URL = 'https://fenerbahce.org/branslar/futbolatakimi/haberler'
    soup = Crawler().get_soup(URL)

    return soup.find('h1', {'class': 'banner-title secondary'}).text
