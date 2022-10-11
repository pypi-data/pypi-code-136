import sys
from io import StringIO
from contextlib import redirect_stdout

class TestCase:
    def __init__(self, example, display, testcode, stdin, expected):
        self.example = example
        self.display = display
        self.testcode = testcode
        self.stdin = stdin
        self.expected = expected

    def __init__(self):
        self.example = None
        self.display = None
        self.testcode = ""
        self.stdin = ""
        self.expected = ""

    def testExpected(self, question, testNumber):
        stds = self.stdin.split("\n")
        splitAnswer = question.answer.split("\n")

        #add a print statement for the input, since setting the sys.stdin doesn't print the user input
        for i in range(len(splitAnswer)):
            if "input(" in splitAnswer[i]:
                splitAnswer[i] += '\nprint("'+ stds.pop(0) + '")'
        answer = "\n".join(splitAnswer)

        #runs the answer using the IO and then saves it in a temporary console
        sys.stdin = StringIO(self.stdin)
        with redirect_stdout(StringIO()) as tempConsole:
            exec(answer)

        knownExpected = tempConsole.getvalue()[:-1]
        if self.expected == "":
            #add expected output using answer
            self.expected = knownExpected
        else:
            #run expected using answer and compare
            if(knownExpected != self.expected):
                raise Exception(f"Testcase doesn't have correct expected output for CodeRunner question titles='{question.title}'. Testcase #{testNumber+1}")
