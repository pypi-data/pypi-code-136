import unittest
from feature_engineering import names
import pandas as pd


class FeatureEngineeringTest(unittest.TestCase):
    def test_names(self):
        #Given
        train = pd.DataFrame(
            {
                "Name":
                    ['Braund, Mr. Owen Harris',
                     'Cumings, Mrs. John Bradley '
                     '(Florence Briggs Thayer)',
                     'Heikkinen, Miss. Laina',
                     'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
                     'Allen, Mr. William Henry']
            })
        test = pd.DataFrame(
            {
                "Name":
                    ['Kelly, Mr. James',
                     'Wilkes, Mrs. James (Ellen Needs)',
                     'Myles, Mr. Thomas Francis',
                     'Wirz, Mr. Albert',
                     'Hirvonen, Mrs. Alexander (Helga E Lindqvist)']
            })

        #When
        new_train, new_test = names(train,test)
        #Then

        self.assertIsInstance(new_train, pd.DataFrame)  # add assertion here
        self.assertIsInstance(new_test, pd.DataFrame)
        self.assertNotIn("names",new_train.columns)
        self.assertNotIn("names", new_test.columns)

if __name__ == '__main__':
    unittest.main()
