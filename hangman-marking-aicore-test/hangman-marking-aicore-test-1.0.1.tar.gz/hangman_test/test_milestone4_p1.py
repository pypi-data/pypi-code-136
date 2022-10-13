import unittest
import os
import ast

class HangmanTestCase(unittest.TestCase):
    def test_presence_milestone_4(self):
        self.assertIn('milestone_3.py', os.listdir('.'), 'You should have a file named milestone_4.py in your repository. If you created it, make sure it is in the root directory of your repository')

    def test_presence_class(self):
        with open('milestone_3.py', 'r') as f:
            code = f.read()

        node = ast.parse(code)
        node.body = [cs for cs in node.body if isinstance(cs, ast.ClassDef)]
        self.assertGreaterEqual(len(node.body), 1, 'You have not defined any class in milestone3.py yet. Make sure you have defined a class named "Hangman"')
        class_names = [name.name for name in node.body]
        self.assertIn('Hangman', class_names, 'You have defined a class, but it is not named Hangman. Make sure you have defined a class named "Hangman"')


if __name__ == '__main__':

    unittest.main(verbosity=0)
    