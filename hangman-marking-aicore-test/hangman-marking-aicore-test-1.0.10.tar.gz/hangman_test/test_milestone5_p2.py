import unittest
import os
# import spacy
# import pkgutil
import ast

def read_function(node):
    whiles = []
    variables = []
    for function_node in node.body[0].body:
        if isinstance(function_node, ast.While):
            whiles.append(function_node)
        elif isinstance(function_node, ast.Assign):
            variables.append(function_node.targets[0].id)

    return whiles, variables

def read_while(node):
    ifs_in_while = []
    for function_node in node.body[0].body:
        if isinstance(function_node, ast.While):
            if hasattr(function_node, 'body'):
                for sub_node in function_node.body:
                    if isinstance(sub_node, ast.If):
                        ifs_in_while.append(sub_node)
    return ifs_in_while
            

class HangmanTestCase(unittest.TestCase):
    def test_function(self):
        path = 'milestone_5.py'

        with open(path, 'r') as f:
            code = f.read()

        node = ast.parse(code)
        node.body = [cs for cs in node.body if isinstance(cs, ast.FunctionDef)]
        function_names = [name.name for name in node.body]
        self.assertEqual(len(function_names), 1, 'You should define ONLY a function named play_hangman in your milestone_5.py file')
        self.assertIn('play_hangman', function_names, 'You should have a function named play_hangman in your milestone_5.py file')
        try:
            whiles, variables = read_function(node)
        except:
            self.fail('You have not defined the function correctly. Make sure that you have assigned the variables word_list and game and then you define the while loop to run the game')
        
        self.assertEqual(len(whiles), 1, 'You should have a while loop in your play_hangman function')
        self.assertGreaterEqual(len(variables), 2, 'You should have at least two variables defined in your play_hangman function: word_list and game')
        ifs_in_while = read_while(node)
        self.assertGreaterEqual(len(ifs_in_while), 1, 'You should have at least one if statement in your while loop to check if the game is over')
    
    def test_presence_readme(self):
        self.assertIn('README.md', os.listdir('.'), 'You should have a README.md file in your project folder')
        with open('README.md', 'r') as f:
            readme = f.read()
        self.assertGreater(len(readme), 2000, 'The README.md file should be at least 1000 characters long')
        # nlp = spacy.load("en_core_web_md")
        # tdata = str(pkgutil.get_data(__name__, "documentation.md"))
        # # with open('documentation.md', 'r') as f:
        # #     tdata = f.read()
        # doc_1 = nlp(readme)
        # doc_2 = nlp(tdata)
        # self.assertLessEqual(doc_1.similarity(doc_2), 0.98, 'The README.md file is almost identical to the one provided in the template')


if __name__ == '__main__':

    unittest.main(verbosity=0)
    