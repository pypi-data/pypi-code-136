from .Question import CodeRunner

class Category:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def __init__(self, name):
        self.name = name
        self.questions = []

    def addQuestion(self, newQuestion):
        self.questions.append(newQuestion)

    def convertQuestions(self, env):
        questionTemplate = []
        #This is where we can test each questions testcases 
        for questionOBJ in self.questions:
            if(isinstance(questionOBJ, CodeRunner)):
                questionOBJ.testTestCases()
            template = env.get_template(questionOBJ._XML_NAME)

            questionTemplate.append(template.render(question=questionOBJ))

        self.questions = questionTemplate

