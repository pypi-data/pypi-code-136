import copy
import random
import unittest
from unittest.mock import MagicMock
import torch
from irisml.tasks.train_with_gradient_cache import Task, GradientCachingTrainer


def fake_transform(x, y):
    return x, y


class TestTrainWithGradientCache(unittest.TestCase):
    def test_split_tensor_or_list(self):
        trainer = GradientCachingTrainer(sub_batch_size=2, model=MagicMock(), lr_scheduler_factory=MagicMock(), optimizer_factory=MagicMock())
        results = trainer._split_tensor_or_list(torch.tensor([[3]] * 4))
        self.assertIsInstance(results, tuple)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].shape, (2, 1))

        results = trainer._split_tensor_or_list((torch.tensor([[3]] * 4), torch.tensor([[2, 2]] * 4)))
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)
        self.assertIsInstance(results[0], tuple)
        self.assertEqual(results[0][0].shape, (2, 1))
        self.assertEqual(results[0][1].shape, (2, 2))
        self.assertEqual(results[1][0].shape, (2, 1))
        self.assertEqual(results[1][1].shape, (2, 2))

        # scalar tensor is returned as-is.
        results = trainer._split_tensor_or_list(torch.tensor(3))
        self.assertEqual(results, torch.tensor(3))

    def test_single_feature(self):
        class Model(torch.nn.Module):
            def __init__(self):
                super().__init__()
                self._model = torch.nn.Conv2d(3, 3, 3)

            @property
            def criterion(self):
                return torch.nn.CrossEntropyLoss()

            def forward(self, inputs):
                return self._model(inputs).flatten(1)

        self._check_with_model(Model())

    def test_three_features(self):
        class Model(torch.nn.Module):
            class Criterion(torch.nn.Module):
                def forward(self, features, targets):
                    return sum(torch.nn.functional.cross_entropy(f, targets) for f in features)

            def __init__(self):
                super().__init__()
                self._model = torch.nn.Conv2d(3, 3, 3)
                self._model2 = torch.nn.Conv2d(3, 3, 3)
                self._model3 = torch.nn.Conv2d(3, 3, 3)

            @property
            def criterion(self):
                return self.Criterion()

            def forward(self, inputs):
                return self._model(inputs).flatten(1), self._model2(inputs).flatten(1), self._model3(inputs).flatten(1)

        self._check_with_model(Model())

    def test_scalar_feature(self):
        class Model(torch.nn.Module):
            class Criterion(torch.nn.Module):
                def forward(self, features, targets):
                    return torch.sum(features[0]) + torch.sum(features[1])

            def __init__(self):
                super().__init__()
                self._model = torch.nn.Conv2d(3, 3, 3)
                self._param = torch.nn.Parameter(torch.tensor(0.1))

            @property
            def criterion(self):
                return self.Criterion()

            def forward(self, inputs):
                return self._param, self._model(inputs)

        self._check_with_model(Model())

    def test_two_inputs(self):
        class Dataset(torch.utils.data.Dataset):
            def __init__(self, num_examples=8, num_classes=3):
                self._data = [((torch.rand(3, 3, 3), torch.rand(4, 3, 3)), 0)] * num_examples

            def __len__(self):
                return len(self._data)

            def __getitem__(self, index):
                return self._data[index]

        class FakeModel(torch.nn.Module):
            class Criterion(torch.nn.Module):
                def forward(self, features, targets):
                    return sum(torch.sum(f) for f in features)

            def __init__(self):
                super().__init__()
                self._conv = torch.nn.Conv2d(3, 3, 3)
                self._conv2 = torch.nn.Conv2d(4, 3, 3)
                self._received_inputs = []

            def forward(self, inputs):
                self._received_inputs.append(copy.deepcopy(inputs))
                return self._conv(inputs[0]).flatten(1), self._conv2(inputs[1]).flatten(1)

            @property
            def criterion(self):
                return self.Criterion()

        dataset = Dataset()
        model = FakeModel()
        config = Task.Config(batch_size=4, sub_batch_size=1, num_epochs=1)
        outputs = Task(config).execute(Task.Inputs(model, dataset, fake_transform))
        self.assertTrue(all(torch.allclose(dataset[0][0][0], i[0]) for i in outputs.model._received_inputs))
        self.assertTrue(all(torch.allclose(dataset[0][0][1], i[1]) for i in outputs.model._received_inputs))

    def _check_with_model(self, model):
        class Dataset(torch.utils.data.Dataset):
            def __init__(self, num_examples=8, num_classes=3):
                self._data = [(torch.rand(3, 3, 3), random.randrange(num_classes)) for i in range(num_examples)]

            def __len__(self):
                return len(self._data)

            def __getitem__(self, index):
                return self._data[index]

        dataset = Dataset()
        config = Task.Config(batch_size=4, sub_batch_size=1, num_epochs=1)
        outputs = Task(config).execute(Task.Inputs(copy.deepcopy(model), dataset, fake_transform))
        model0 = outputs.model

        config = Task.Config(batch_size=4, sub_batch_size=2, num_epochs=1)
        outputs = Task(config).execute(Task.Inputs(copy.deepcopy(model), dataset, fake_transform))
        model1 = outputs.model

        config = Task.Config(batch_size=4, sub_batch_size=4, num_epochs=1)
        outputs = Task(config).execute(Task.Inputs(copy.deepcopy(model), dataset, fake_transform))
        model2 = outputs.model

        config = Task.Config(batch_size=4, sub_batch_size=4, num_epochs=3)
        outputs = Task(config).execute(Task.Inputs(copy.deepcopy(model), dataset, fake_transform))
        model3 = outputs.model

        # All three models are exactly same.
        parameters0 = list(model0.parameters())
        parameters1 = list(model1.parameters())
        parameters2 = list(model2.parameters())
        parameters3 = list(model3.parameters())
        for i in range(len(parameters0)):
            self.assertTrue(torch.allclose(parameters0[i], parameters1[i]))
            self.assertTrue(torch.allclose(parameters0[i], parameters2[i]))
            self.assertFalse(torch.allclose(parameters0[i], parameters3[i]))  # Make sure the allclose() is not too loose.
