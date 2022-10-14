import random


class Question_Generator:
    def __init__(self):
        self.a=1
        self.b=1
        self.ops = ['+', '-']
        self.c=1
        self.current_ques=str(self.a) + self.ops[self.c] + str(self.b)

    def generate_ques(self):
        self.a = random.randint(1, 99)
        self.b = random.randint(1, 99)
        self.c = random.randint(0, 1)
        self.current_ques=str(self.a) + self.ops[self.c] + str(self.b)
        return (self.current_ques)

    def answer(self):
        if self.ops[self.c] == '+':
            return self.a + self.b
        else:
            return self.a - self.b