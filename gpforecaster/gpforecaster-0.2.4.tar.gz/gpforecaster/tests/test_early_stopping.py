import unittest
from gpforecaster.model.gpf import GPF
import tsaugmentation as tsag
import shutil


class TestModel(unittest.TestCase):

    def setUp(self):
        self.data = tsag.preprocessing.PreprocessDatasets('prison').apply_preprocess()
        self.n = self.data['predict']['n']
        self.s = self.data['train']['s']
        shutil.rmtree("./data/original_datasets")
        self.gpf = GPF('prison', self.data)

    def test_early_stopping_fn(self):
        res = self.gpf.early_stopping([5.1, 5.2, 4.9, 5.0, 5.1, 5.2], 2)
        self.assertTrue(res)

    def test_early_stopping(self):
        model, like = self.gpf.train(n_iterations=500)
        self.gpf.plot_losses()
        self.assertEqual(len(self.gpf.losses), 146)
