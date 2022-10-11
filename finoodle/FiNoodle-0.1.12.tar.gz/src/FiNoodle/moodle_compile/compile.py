from msilib.schema import Patch
import pathlib
from os import path
import base64
import re
from .parser.Question import CodeRunner
from .parser.Question import MultipleChoice
from .parser.TestCase import TestCase
from .parser.Answer import Answer
from .parser.Question import ShortAnswer
from .parser.File import File
from .parser.Category import Category
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

def validate(fileLines):
    pass
    #print("Content:", fileLines)


def getQuestion(dir):
    print("[{}] Loading questions from {}".format(datetime.now().strftime("%H:%M:%S"), dir))

    if dir.suffix == ".cr":
        print("[{}]   Question format: CodeRunner".format(datetime.now().strftime("%H:%M:%S")))
        newQuestion = CodeRunner()
    elif dir.suffix == ".mc":
        print("[{}]   Question format: Multiple choice".format(datetime.now().strftime("%H:%M:%S")))
        newQuestion = MultipleChoice()
    elif dir.suffix == ".sa":
        newQuestion = ShortAnswer()
    for p in dir.iterdir():
        if not p.is_file():
            for sf in p.iterdir():
                if sf.is_file():
                    with open(sf, "rb") as f:
                        content = f.read()
                        newFile = File(sf.name, '/')
                        newFile.setContent(base64.b64encode(content))
                        if sf.suffix in ".png,.jpg,.jpeg":
                            newQuestion.addImage(newFile)
                        else:
                            newQuestion.addFile(newFile)
            continue

        with open(p) as f:
            if p.suffix == ".py":
                print("[{}]   Input format: .py".format(datetime.now().strftime("%H:%M:%S")))

                answer = f.read()
                newQuestion.setAnswer(answer)

            elif p.suffix == ".md":
                print("[{}]   Input format: .md".format(datetime.now().strftime("%H:%M:%S")))

                prompt = f.read()
                newQuestion.setPrompt(prompt)
            elif p.suffix == ".txt":
                feedback = f.read()
                newQuestion.setFeedback(feedback)

            elif p.suffix == ".toml":
                fileRead = f.readlines()
                #Validation
                validate(fileRead)
                print("[{}]   Input format: .toml".format(datetime.now().strftime("%H:%M:%S")))

                cases = []
                lines = iter(fileRead)
                for line in lines:
                    if line.strip() == "":
                        continue
                    if "[[testcases]]" in line:
                        cases.append(TestCase())
                    elif "[[answers]]" in line:
                        cases.append(Answer())
                    else:
                        splitLine = line.split("=")
                        #take what's before an equal sign and that's our variable name we are manipulating
                        attributeName = splitLine[0].strip()
                        attributeValue = None
                        #get everything inbetween the three ''' '''
                        if "'''" not in line:
                            attributeValue = splitLine[1].strip()
                        else:
                            equator = splitLine[1].split("'''")
                            attributeValue = equator[1]
                            if len(equator) == 2:
                                while True:
                                    nextLine = next(lines)
                                    if "'''" in nextLine:
                                        attributeValue += nextLine.split("'''")[0]
                                        break
                                    attributeValue += nextLine
                        if len(cases) > 0:
                            cases[-1].__setattr__(attributeName, attributeValue)
                        else:
                            if attributeName == "tags":
                                attributeValue = attributeValue.split(",")
                            newQuestion.__setattr__(attributeName, attributeValue)
                newQuestion.setCases(cases)          
    return newQuestion


def IterateChildren(dir, cat, globLocations, globPattern):
    #if it's a question
    if(dir.suffix != ""):
        [questionName, type] = dir.name.split(".")
        question = getQuestion(dir)
        question.setTitle(questionName)
        cat[-1].addQuestion(question)
    else:       
        cat.append(createCategory(dir))
        #checkSubDirectories
        for p in dir.iterdir():
            if p not in globLocations["whitelist"] and globPattern["IterateChildren"] and p not in globLocations["blacklist"]:

                cat = (IterateChildren(p, cat, globLocations, globPattern))
    return cat
    


def createCategory(location, startingPart = 1):
    if len(location.parts) == 1:
       catName = str(pathlib.Path(location.parts[0]))
    else:
        catName = str(pathlib.Path(*location.parts[startingPart:]))
    return Category(catName)

def importQuestions(root, globPattern):
    globLocations = {
        "whitelist": list(root.rglob(globPattern["exportGlob"])),
        "blacklist": list(root.rglob(globPattern["blackListGlob"]))
    } 
    if globPattern["blackListGlob"] == "":
        globLocations["blacklist"] = []
    if len(globLocations["whitelist"]) == 0:
        return ""
    globLocations["whitelist"] = [x for x in globLocations["whitelist"] if (x.is_dir() and str(x.parent.suffix) == "")]
    numQuestions = len([x for x in globLocations["whitelist"] if x.suffix != ""])

    smallestParent = min([len(x.parts) for x in globLocations["whitelist"]])-1

    categories = []
    #if all in the glob are questions then
    if numQuestions == len(globLocations["whitelist"]):
        categories.append(createCategory(globLocations["whitelist"][0].parent, smallestParent-1))


    for pa in globLocations["whitelist"]:
        #if path contains anything from any of the blacklist strings
        for location in globLocations["blacklist"]:
            if str(location) in str(pa):
                break
        else:
            categories = (IterateChildren(pa, categories, globLocations, globPattern))  
            continue
        break

    print("pathToTemplates =", path.join(path.dirname(__file__), 'templates'))
    file_loader = FileSystemLoader(path.join(path.dirname(__file__), 'templates'))

    env = Environment(loader=file_loader)

    #get our questions/answers
    #categories = getCategories(root)
    quizTemplate = env.get_template('quiz.xml')

    for cat in categories:
        cat.convertQuestions(env)

    output = quizTemplate.render(categories=categories)


    return output