from fenerbahce.crawler import Crawler


def _get_match_info(soup):
    return [data.text.replace('\n', '') for data in soup.find('ul', {'class': 'match-info'}) if data.text != '\n']


def _get_team_info(soup):
    return [data.text.replace('\n', '') for data in soup.find_all('div', {'class': 'team'})]


def next_match():
    URL = 'https://fenerbahce.org/branslar/futbolatakimi/haberler'
    soup = Crawler().get_soup(URL)

    parsed = ''

    for info in _get_match_info(soup):
        parsed += info + '\n'

    teams = _get_team_info(soup)
    parsed += teams[0] + '-' + teams[1]
    return parsed


if __name__ == '__main__':
    print(next_match())
