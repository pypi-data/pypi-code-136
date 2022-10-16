from dataclasses import dataclass
from datetime import date
from functools import reduce
from itertools import zip_longest
from typing import IO, List

from boatrace.models import BettingMethod, StadiumTelCode
from boatrace.official.v1707.decorators import (
    no_content_handleable,
    race_cancellation_handleable,
)
from boatrace.official.v1707.pages.race.utils import parse_race_key_attributes
from bs4 import BeautifulSoup


def _grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


# ※ 三連単のみ対応
@dataclass(frozen=True)
class Odds:
    race_holding_date: date
    stadium_tel_code: StadiumTelCode
    race_number: int
    betting_method: BettingMethod
    betting_number: int
    ratio: float


@no_content_handleable
@race_cancellation_handleable
def extract_odds(file: IO) -> List[Odds]:
    soup = BeautifulSoup(file, "html.parser")
    race_key_attributes = parse_race_key_attributes(soup)

    odds_table = soup.select(".table1")[1]
    if len(odds_table.select("tbody tr td.oddsPoint")) != 120:
        # 今の所三連単しか対応してないので、
        # オッズのページであっても三連単以外のファイルが渡されたらエラーとする
        raise TypeError

    second_arrived_cells = odds_table.select('tbody tr td[rowspan="4"]')
    second_arrived_numbers = reduce(
        lambda a, b: a + b,
        [
            [int(cell.text) for cell in cells] * 4
            for cells in _grouper(6, second_arrived_cells)
        ],
    )
    third_arrived_numbers = [
        int(td.text) for td in odds_table.select('tbody tr td[class^="is-boatColor"]')
    ]

    data = []
    for i, td in enumerate(odds_table.select("tbody tr td.oddsPoint"), 0):
        if td.text == "欠場":
            # データ自体を作らない
            # ratio を 0.0 にしてdtoを作ったりしてたこともあったが、0.0だとベットしたら0円になるってことだし
            # それも不自然なためデータ自体が作らないのが違和感がないため
            continue

        data.append(
            Odds(
                **race_key_attributes,
                betting_method=BettingMethod.TRIFECTA,
                betting_number=int(
                    f"{(i % 6) + 1}{second_arrived_numbers[i]}{third_arrived_numbers[i]}"
                ),
                ratio=float(td.text),
            )
        )

    return data
