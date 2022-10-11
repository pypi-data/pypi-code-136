from hadata.answer import MongoUserAssessmentsQuestionAnswer
from hautils.mongo import create_db
from hautils.web import mongo_to_dict

FOOBAR = "x"


def fooxbar():
    print("hello world")


class MyTestClass():

    def __int__(self):
        print("hello")


if __name__ == "__main__":
    create_db()
    m = MongoUserAssessmentsQuestionAnswer.objects(id="6322cb052eb4a968587b85d7").first()
    r = mongo_to_dict(m)
    print(r)
