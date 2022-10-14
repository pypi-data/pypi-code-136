from category import Category
from type import Type


class Question:
    def __init__(self, question: str, answer: str, category: Category, type: Type):
        self.question = question
        self.answer = answer
        self.category = category
        self.type = type

    def from_json(json: dict):
        # get category from string

        return Question(
            json['question'],
            json['answer'],
            Category(json['category']),
            Type(json['type'])
        )
