import re
from dataclasses import dataclass
from datetime import date
from typing import IO

from boatrace.models import Branch, Prefecture, RacerRank
from boatrace.official.factories import PrefectureFactory
from boatrace.official.v1707.decorators import no_content_handleable
from bs4 import BeautifulSoup


# note: 体重も級別も一応保持する
# 体重は節間日次で変動し、レースの直前情報でレース時の最新情報は取得できる
# 級別も成績に応じて期毎に改められる
# ただ、取得できるデータ（特にコストもかからないもの）は保持しておいた方がライブラリとしての汎用性が高くなるため持っておく
# 血液型は流石にいらないと思うので取ってない
@dataclass(frozen=True)
class Racer:
    last_name: str
    first_name: str
    registration_number: int
    birth_date: date
    height: int
    weight: float
    branch_prefecture: Branch
    born_prefecture: Prefecture
    term: int
    current_rating: RacerRank


@no_content_handleable
def extract_racer_profile(file: IO) -> Racer:
    soup = BeautifulSoup(file, "html.parser")

    full_name = soup.select_one(".racer1_bodyName").get_text()
    last_name, first_name = re.split(r"[\s　]+", full_name)

    dd_list = soup.select_one("dl.list3").select("dd")

    registration_number = int(dd_list[0].get_text())
    birth_date = date(*[int(ymd) for ymd in dd_list[1].get_text().split("/")])

    if m := re.match(r"(\d{3})cm", dd_list[2].get_text()):
        height = int(m.group(1))
    if m := re.match(r"(\d{2})kg", dd_list[3].get_text()):
        weight = int(m.group(1))
    branch_prefecture = Branch(PrefectureFactory.create(dd_list[5].get_text()))
    born_prefecture = PrefectureFactory.create(dd_list[6].get_text())
    if m := re.match(r"(\d{2,3})期", dd_list[7].get_text()):
        term = int(m.group(1))
    racer_rank = RacerRank(dd_list[8].get_text()[:2])

    return Racer(
        last_name=last_name,
        first_name=first_name,
        registration_number=registration_number,
        birth_date=birth_date,
        height=height,
        weight=weight,
        branch_prefecture=branch_prefecture,
        born_prefecture=born_prefecture,
        term=term,
        current_rating=racer_rank,
    )
