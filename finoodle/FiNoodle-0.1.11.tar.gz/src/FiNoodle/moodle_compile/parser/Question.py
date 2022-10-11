import pathlib
from jinja2 import Environment, FileSystemLoader
import re
from datetime import datetime


class Question:
    def __init__(self):
        self.title = "null"
        self.prompt = "null"
        self.files = []
        self.images = []
        self.tags = []
        self.defaultgrade = 1
        self.penalty = 0
        self.answerlines = 15
        self.precheck = 0
        self.answerpreload = ''''''
        self.casesensitivity = 0
        

    def setTitle(self, title):
        self.title = title

    def setPrompt(self, prompt):
        self.prompt = prompt

    def setGrade(self, grade):
        self.grade = grade
    
    def addFile(self, file):
        self.files.append(file)

    def addImage(self, file):
        self.images.append(file)

class MultipleChoice(Question):
    _XML_NAME = "multiplechoice.xml"
    def __init__(self):
        super(MultipleChoice, self).__init__()
        self.shuffle = 'true'
        self.answernumbering = 'abc'
        self.singleAnswer = 'true'

    def setCases(self, answers):
        self.answers = answers

class ShortAnswer(Question):
    _XML_NAME = "shortanswer.xml"
    def __init__(self):
        super(ShortAnswer, self).__init__()
        
    def setCases(self, answers):
        self.answers = answers

    def setFeedback(self, feedback):
        self.feedback = feedback



class CodeRunner(Question):
    _XML_NAME = "coderunner.xml"
    def __init__(self):
        super(CodeRunner, self).__init__()
        self.coderunnertype = "python3_w_input"
        self.template = None

    def setAnswer(self, answer):
        self.answer = answer

    def setCases(self, testcases):
        self.testcases = testcases

    def testTestCases(self):
        #move the input part to a previous line
        #convert Answer inputs to console
        #testCaseCode = self.answer.replace('input(', 'print(')
        #print(testCaseCode)
        for loopNum, test in enumerate(self.testcases):
            test.testExpected(self, loopNum)