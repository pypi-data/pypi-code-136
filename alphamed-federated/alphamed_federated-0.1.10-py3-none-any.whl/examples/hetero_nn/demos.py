"""HeteroNN demos."""

import os
from time import time
from typing import Dict, List, Set, Tuple, Union

import cloudpickle as pickle
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as td
import torchvision

from ... import logger
from ...hetero_nn import (HeteroNNCollaboratorScheduler, HeteroNNHostScheduler,
                          SecureHeteroNNCollaboratorScheduler,
                          SecureHeteroNNHostScheduler)
from ...hetero_nn.psi import (RSAPSICollaboratorScheduler,
                              RSAPSIInitiatorScheduler)
from ...scheduler import register_metrics
from . import DEV_TASK_ID

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

_DATA_DIR = os.path.join(CURRENT_DIR, 'data')

VANILLA = 'vanilla'
SECURE = 'secure'

torch.manual_seed(42)


class ConvNet(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=10, kernel_size=(5, 3))
        self.conv2 = nn.Conv2d(in_channels=10, out_channels=20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(in_features=80, out_features=50)
        self.fc2 = nn.Linear(in_features=50, out_features=10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 80)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        return self.fc2(x)


class InferModule(nn.Module):

    def __init__(self) -> None:
        super().__init__()
        self.linear = nn.Linear(20, 10)

    def forward(self, input):
        out = self.linear(input)
        return F.log_softmax(out, dim=-1)


class DemoHeteroHost(HeteroNNHostScheduler):

    def __init__(self,
                 feature_key: str,
                 batch_size: int,
                 data_dir: str,
                 name: str = None,
                 max_rounds: int = 0,
                 calculation_timeout: int = 300,
                 schedule_timeout: int = 30,
                 data_channel_timeout: Tuple[int, int] = (30, 60),  # TODO 有共享存储后修改
                 log_rounds: int = 0,
                 is_feature_trainable: bool = True) -> None:
        super().__init__(feature_key=feature_key,
                         name=name,
                         max_rounds=max_rounds,
                         calculation_timeout=calculation_timeout,
                         schedule_timeout=schedule_timeout,
                         data_channel_timeout=data_channel_timeout,
                         log_rounds=log_rounds,
                         is_feature_trainable=is_feature_trainable)
        self.batch_size = batch_size
        self.data_dir = data_dir

        train_dataset = torchvision.datasets.MNIST(
            self.data_dir,
            train=True,
            download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,))
            ])
        )
        self.train_loader = td.DataLoader(train_dataset,
                                          batch_size=self.batch_size,
                                          shuffle=False)
        test_dataset = torchvision.datasets.MNIST(
            self.data_dir,
            train=False,
            download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,))
            ])
        )
        self.test_loader = td.DataLoader(test_dataset,
                                         batch_size=self.batch_size,
                                         shuffle=False)

    def load_local_ids(self) -> List[str]:
        train_ids = [str(_id) for _id in self.train_loader.sampler]
        test_ids = [str(-1 - _id) for _id in self.test_loader.sampler]
        return train_ids + test_ids

    def split_dataset(self, id_intersection: Set[str]) -> Tuple[Set[str], Set[str]]:
        ids = set(int(_id) for _id in id_intersection)
        train_ids = set(str(_id) for _id in ids if _id >= 0)
        test_ids = set(str(_id + 1) for _id in ids if _id < 0)
        return train_ids, test_ids

    def make_feature_model(self) -> nn.Module:
        return ConvNet()

    def make_feature_optimizer(self, feature_model: nn.Module) -> optim.Optimizer:
        return optim.SGD(feature_model.parameters(), lr=0.01, momentum=0.1)

    def _erase_right(self, _image: torch.Tensor) -> torch.Tensor:
        return _image[:, :, :, :14]

    def iterate_train_feature(self,
                              feature_model: nn.Module,
                              train_ids: List[str]) -> Tuple[torch.Tensor, torch.Tensor]:
        assert len(train_ids) == 60000, 'Some train samples lost.'
        for _data, _labels in self.train_loader:
            _data = self._erase_right(_data)
            yield feature_model(_data), _labels

    def iterate_test_feature(self,
                             feature_model: nn.Module,
                             test_ids: List[str]) -> Tuple[torch.Tensor, torch.Tensor]:
        assert len(test_ids) == 10000, 'Some test samples lost.'
        for _data, _labels in self.test_loader:
            _data = self._erase_right(_data)
            yield feature_model(_data), _labels

    def make_infer_model(self) -> nn.Module:
        return InferModule()

    def make_infer_optimizer(self, infer_model: nn.Module) -> optim.Optimizer:
        return optim.SGD(infer_model.parameters(), lr=0.01, momentum=0.1)

    def train_a_batch(self, feature_projection: Dict[str, torch.Tensor], labels: torch.Tensor):
        fusion_tensor = torch.concat((feature_projection['demo_host'],
                                      feature_projection['demo_collaborator']), dim=1)
        self.optimizer.zero_grad()
        out = self.infer_model(fusion_tensor)
        loss = F.nll_loss(out, labels)
        loss.backward()
        self.optimizer.step()

    @register_metrics(name='timer', keys=['run_time'])
    @register_metrics(name='test_results', keys=['average_loss', 'accuracy', 'correct_rate'])
    def test(self,
             batched_feature_projections: List[torch.Tensor],
             batched_labels: List[torch.Tensor]):
        start = time()
        test_loss = 0
        correct = 0
        for _feature_projection, _lables in zip(batched_feature_projections, batched_labels):
            fusion_tensor = torch.concat((_feature_projection['demo_host'],
                                          _feature_projection['demo_collaborator']), dim=1)
            out: torch.Tensor = self.infer_model(fusion_tensor)
            test_loss += F.nll_loss(out, _lables)
            pred = out.max(1, keepdim=True)[1]
            correct += pred.eq(_lables.view_as(pred)).sum().item()

        test_loss /= len(self.test_loader.dataset)
        accuracy = correct / len(self.test_loader.dataset)
        correct_rate = 100. * accuracy
        logger.info(f'Test set: Average loss: {test_loss:.4f}')
        logger.info(
            f'Test set: Accuracy: {accuracy} ({correct_rate:.2f}%)'
        )

        end = time()
        self.get_metrics('timer').append_metrics_item({'run_time': end - start})
        self.get_metrics('test_results').append_metrics_item({
            'average_loss': test_loss,
            'accuracy': accuracy,
            'correct_rate': correct_rate
        })

    def validate_context(self):
        super().validate_context()
        assert self.train_loader and len(self.train_loader) > 0, 'failed to load train data'
        logger.info(f'There are {len(self.train_loader.dataset)} samples for training.')
        assert self.test_loader and len(self.test_loader) > 0, 'failed to load test data'
        logger.info(f'There are {len(self.test_loader.dataset)} samples for testing.')

    # replace data channel ports used for debuging
    def _make_id_intersection(self) -> List[str]:
        """Make PSI and get id intersection for training."""
        local_ids = self.load_local_ids()
        psi_scheduler = RSAPSIInitiatorScheduler(
            task_id=self.task_id,
            initiator_id=self.id,
            ids=local_ids,
            collaborator_ids=self._partners,
            contractor=self.contractor,
            data_channel_timeout=(self.dc_conn_timeout, self.dc_timeout)
        )
        psi_scheduler._data_channel._ports = [i for i in range(21000, 21010)]
        self._id_intersection = psi_scheduler.make_intersection()


class DemoHeteroCollaborator(HeteroNNCollaboratorScheduler):

    def __init__(self,
                 feature_key: str,
                 batch_size: int,
                 data_dir: str,
                 name: str = None,
                 schedule_timeout: int = 30,
                 data_channel_timeout: Tuple[int, int] = (30, 60),
                 is_feature_trainable: bool = True) -> None:
        super().__init__(feature_key=feature_key,
                         name=name,
                         schedule_timeout=schedule_timeout,
                         data_channel_timeout=data_channel_timeout,
                         is_feature_trainable=is_feature_trainable)
        self.batch_size = batch_size
        self.data_dir = data_dir

        train_dataset = torchvision.datasets.MNIST(
            self.data_dir,
            train=True,
            download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,))
            ])
        )
        self.train_loader = td.DataLoader(train_dataset,
                                          batch_size=self.batch_size,
                                          shuffle=False)
        test_dataset = torchvision.datasets.MNIST(
            self.data_dir,
            train=False,
            download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,))
            ])
        )
        self.test_loader = td.DataLoader(test_dataset,
                                         batch_size=self.batch_size,
                                         shuffle=False)

    def load_local_ids(self) -> List[str]:
        train_ids = [str(_id) for _id in self.train_loader.sampler]
        test_ids = [str(-1 - _id) for _id in self.test_loader.sampler]
        return train_ids + test_ids

    def split_dataset(self, id_intersection: Set[str]) -> Tuple[Set[str], Set[str]]:
        ids = set(int(_id) for _id in id_intersection)
        train_ids = set(str(_id) for _id in ids if _id >= 0)
        test_ids = set(str(_id + 1) for _id in ids if _id < 0)
        return train_ids, test_ids

    def make_feature_model(self) -> nn.Module:
        return ConvNet()

    def make_feature_optimizer(self, feature_model: nn.Module) -> optim.Optimizer:
        return optim.SGD(feature_model.parameters(), lr=0.01, momentum=0.1)

    def _erase_left(self, _image: torch.Tensor) -> torch.Tensor:
        return _image[:, :, :, 14:]

    def iterate_train_feature(self,
                              feature_model: nn.Module,
                              train_ids: List[str]) -> torch.Tensor:
        assert len(train_ids) == 60000, 'Some train samples lost.'
        for _data, _ in self.train_loader:
            _data = self._erase_left(_data)
            yield feature_model(_data)

    def iterate_test_feature(self,
                             feature_model: nn.Module,
                             test_ids: List[str]) -> torch.Tensor:
        assert len(test_ids) == 10000, 'Some test samples lost.'
        for _data, _ in self.test_loader:
            _data = self._erase_left(_data)
            yield feature_model(_data)

    def validate_context(self):
        super().validate_context()
        assert self.train_loader and len(self.train_loader) > 0, 'failed to load train data'
        logger.info(f'There are {len(self.train_loader.dataset)} samples for training.')
        assert self.test_loader and len(self.test_loader) > 0, 'failed to load test data'
        logger.info(f'There are {len(self.test_loader.dataset)} samples for testing.')

    # replace data channel ports used for debuging
    def _make_id_intersection(self) -> List[str]:
        """Make PSI and get id intersection for training."""
        local_ids = self.load_local_ids()
        psi_scheduler = RSAPSICollaboratorScheduler(
            task_id=self.task_id,
            collaborator_id=self.id,
            ids=local_ids,
            contractor=self.contractor,
            data_channel_timeout=(self.dc_conn_timeout, self.dc_timeout)
        )
        psi_scheduler._data_channel._ports = [i for i in range(21000, 21010)]
        self._id_intersection = psi_scheduler.collaborate_intersection()


class DemoSecureHeteroHost(SecureHeteroNNHostScheduler):

    def __init__(self,
                 feature_key: str,
                 project_layer_config: List[Tuple[str, int, int]],
                 project_layer_lr: float,
                 batch_size: int,
                 data_dir: str,
                 name: str = None,
                 max_rounds: int = 0,
                 calculation_timeout: int = 300,
                 schedule_timeout: int = 30,
                 data_channel_timeout: Tuple[int, int] = (30, 60),  # TODO 有共享存储后修改
                 log_rounds: int = 0,
                 is_feature_trainable: bool = True) -> None:
        super().__init__(feature_key=feature_key,
                         project_layer_config=project_layer_config,
                         project_layer_lr=project_layer_lr,
                         name=name,
                         max_rounds=max_rounds,
                         calculation_timeout=calculation_timeout,
                         schedule_timeout=schedule_timeout,
                         data_channel_timeout=data_channel_timeout,
                         log_rounds=log_rounds,
                         is_feature_trainable=is_feature_trainable)
        self.batch_size = batch_size
        self.data_dir = data_dir

        train_dataset = LeftHalfMNIST(
            self.data_dir,
            train=True,
            download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,))
            ])
        )
        self.train_loader = td.DataLoader(train_dataset,
                                          batch_size=self.batch_size,
                                          shuffle=False)
        test_dataset = LeftHalfMNIST(
            self.data_dir,
            train=False,
            download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,))
            ])
        )
        self.test_loader = td.DataLoader(test_dataset,
                                         batch_size=self.batch_size,
                                         shuffle=False)

    def load_local_ids(self) -> List[str]:
        train_ids = [str(_id) for _id in self.train_loader.sampler]
        test_ids = [str(-1 - _id) for _id in self.test_loader.sampler]
        return train_ids + test_ids

    def split_dataset(self, id_intersection: Set[str]) -> Tuple[Set[str], Set[str]]:
        ids = set(int(_id) for _id in id_intersection)
        train_ids = set(str(_id) for _id in ids if _id >= 0)
        test_ids = set(str(_id + 1) for _id in ids if _id < 0)
        return train_ids, test_ids

    def make_feature_model(self) -> nn.Module:
        return ConvNet()

    def make_feature_optimizer(self, feature_model: nn.Module) -> optim.Optimizer:
        return optim.SGD(feature_model.parameters(), lr=0.01, momentum=0.1)

    def iterate_train_feature(self,
                              feature_model: nn.Module,
                              train_ids: List[str]) -> Tuple[torch.Tensor, torch.Tensor]:
        assert len(train_ids) == 60000, 'Some train samples lost.'
        for _data, _labels in self.train_loader:
            yield feature_model(_data), _labels

    def iterate_test_feature(self,
                             feature_model: nn.Module,
                             test_ids: List[str]) -> Tuple[torch.Tensor, torch.Tensor]:
        assert len(test_ids) == 10000, 'Some test samples lost.'
        for _data, _labels in self.test_loader:
            yield feature_model(_data), _labels

    def make_infer_model(self) -> nn.Module:
        return InferModule()

    def make_infer_optimizer(self, infer_model: nn.Module) -> optim.Optimizer:
        return optim.SGD(infer_model.parameters(), lr=0.01, momentum=0.1)

    def train_a_batch(self, feature_projection: Dict[str, torch.Tensor], labels: torch.Tensor):
        fusion_tensor = torch.concat((feature_projection['demo_host'],
                                      feature_projection['demo_collaborator']), dim=1)
        self.optimizer.zero_grad()
        out = self.infer_model(fusion_tensor)
        loss = F.nll_loss(out, labels)
        loss.backward()
        self.optimizer.step()

    @register_metrics(name='timer', keys=['run_time'])
    @register_metrics(name='test_results', keys=['average_loss', 'accuracy', 'correct_rate'])
    def test(self,
             batched_feature_projections: List[torch.Tensor],
             batched_labels: List[torch.Tensor]):
        start = time()
        test_loss = 0
        correct = 0
        for _feature_projection, _lables in zip(batched_feature_projections, batched_labels):
            fusion_tensor = torch.concat((_feature_projection['demo_host'],
                                          _feature_projection['demo_collaborator']), dim=1)
            out: torch.Tensor = self.infer_model(fusion_tensor)
            test_loss += F.nll_loss(out, _lables)
            pred = out.max(1, keepdim=True)[1]
            correct += pred.eq(_lables.view_as(pred)).sum().item()

        test_loss /= len(self.test_loader.dataset)
        accuracy = correct / len(self.test_loader.dataset)
        correct_rate = 100. * accuracy
        logger.info(f'Test set: Average loss: {test_loss:.4f}')
        logger.info(
            f'Test set: Accuracy: {accuracy} ({correct_rate:.2f}%)'
        )

        end = time()
        self.get_metrics('timer').append_metrics_item({'run_time': end - start})
        self.get_metrics('test_results').append_metrics_item({
            'average_loss': test_loss,
            'accuracy': accuracy,
            'correct_rate': correct_rate
        })

    def validate_context(self):
        super().validate_context()
        assert self.train_loader and len(self.train_loader) > 0, 'failed to load train data'
        logger.info(f'There are {len(self.train_loader.dataset)} samples for training.')
        assert self.test_loader and len(self.test_loader) > 0, 'failed to load test data'
        logger.info(f'There are {len(self.test_loader.dataset)} samples for testing.')

    # replace data channel ports used for debuging
    def _make_id_intersection(self) -> List[str]:
        """Make PSI and get id intersection for training."""
        local_ids = self.load_local_ids()
        psi_scheduler = RSAPSIInitiatorScheduler(
            task_id=self.task_id,
            initiator_id=self.id,
            ids=local_ids,
            collaborator_ids=self._partners,
            contractor=self.contractor,
            data_channel_timeout=(self.dc_conn_timeout, self.dc_timeout)
        )
        psi_scheduler._data_channel._ports = [i for i in range(21000, 21010)]
        self._id_intersection = psi_scheduler.make_intersection()


class DemoSecureHeteroCollaborator(SecureHeteroNNCollaboratorScheduler):

    def __init__(self,
                 feature_key: str,
                 project_layer_lr: int,
                 batch_size: int,
                 data_dir: str,
                 name: str = None,
                 schedule_timeout: int = 30,
                 data_channel_timeout: Tuple[int, int] = (30, 60),
                 is_feature_trainable: bool = True) -> None:
        super().__init__(feature_key=feature_key,
                         project_layer_lr=project_layer_lr,
                         name=name,
                         schedule_timeout=schedule_timeout,
                         data_channel_timeout=data_channel_timeout,
                         is_feature_trainable=is_feature_trainable)
        self.batch_size = batch_size
        self.data_dir = data_dir

        train_dataset = RightHalfMNIST(
            self.data_dir,
            train=True,
            download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,))
            ])
        )
        self.train_loader = td.DataLoader(train_dataset,
                                          batch_size=self.batch_size,
                                          shuffle=False)
        test_dataset = RightHalfMNIST(
            self.data_dir,
            train=False,
            download=True,
            transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,))
            ])
        )
        self.test_loader = td.DataLoader(test_dataset,
                                         batch_size=self.batch_size,
                                         shuffle=False)

    def load_local_ids(self) -> List[str]:
        train_ids = [str(_id) for _id in self.train_loader.sampler]
        test_ids = [str(-1 - _id) for _id in self.test_loader.sampler]
        return train_ids + test_ids

    def split_dataset(self, id_intersection: Set[str]) -> Tuple[Set[str], Set[str]]:
        ids = set(int(_id) for _id in id_intersection)
        train_ids = set(str(_id) for _id in ids if _id >= 0)
        test_ids = set(str(_id + 1) for _id in ids if _id < 0)
        return train_ids, test_ids

    def make_feature_model(self) -> nn.Module:
        return ConvNet()

    def make_feature_optimizer(self, feature_model: nn.Module) -> optim.Optimizer:
        return optim.SGD(feature_model.parameters(), lr=0.01, momentum=0.1)

    def iterate_train_feature(self,
                              feature_model: nn.Module,
                              train_ids: List[str]) -> torch.Tensor:
        assert len(train_ids) == 60000, 'Some train samples lost.'
        for _data in self.train_loader:
            yield feature_model(_data)

    def iterate_test_feature(self,
                             feature_model: nn.Module,
                             test_ids: List[str]) -> torch.Tensor:
        assert len(test_ids) == 10000, 'Some test samples lost.'
        for _data in self.test_loader:
            yield feature_model(_data)

    def validate_context(self):
        super().validate_context()
        assert self.train_loader and len(self.train_loader) > 0, 'failed to load train data'
        logger.info(f'There are {len(self.train_loader.dataset)} samples for training.')
        assert self.test_loader and len(self.test_loader) > 0, 'failed to load test data'
        logger.info(f'There are {len(self.test_loader.dataset)} samples for testing.')

    # replace data channel ports used for debuging
    def _make_id_intersection(self) -> List[str]:
        """Make PSI and get id intersection for training."""
        local_ids = self.load_local_ids()
        psi_scheduler = RSAPSICollaboratorScheduler(
            task_id=self.task_id,
            collaborator_id=self.id,
            ids=local_ids,
            contractor=self.contractor,
            data_channel_timeout=(self.dc_conn_timeout, self.dc_timeout)
        )
        psi_scheduler._data_channel._ports = [i for i in range(21000, 21010)]
        self._id_intersection = psi_scheduler.collaborate_intersection()


def get_task_id() -> str:
    return DEV_TASK_ID


def get_host(mode: str = VANILLA) -> Union[DemoHeteroHost, DemoSecureHeteroHost]:
    assert mode in (VANILLA, SECURE), f'unknown mode: {mode}'

    pickle_file = './scheduler_host.pickle'

    if os.path.exists(pickle_file):
        os.remove(pickle_file)

    if mode == VANILLA:
        scheduler = DemoHeteroHost(feature_key='demo_host',
                                   batch_size=128,
                                   data_dir=_DATA_DIR,
                                   name='demo_hetero_host',
                                   max_rounds=5,
                                   calculation_timeout=30,
                                   data_channel_timeout=(200, 200),
                                   log_rounds=1)
    else:
        project_layer_config = [
            ('demo_host', 10, 10),
            ('demo_collaborator', 10, 10)
        ]
        scheduler = DemoSecureHeteroHost(feature_key='demo_host',
                                         project_layer_config=project_layer_config,
                                         project_layer_lr=0.01,
                                         batch_size=128,
                                         data_dir=_DATA_DIR,
                                         name='demo_hetero_host',
                                         max_rounds=5,
                                         calculation_timeout=30,
                                         data_channel_timeout=(200, 200),
                                         log_rounds=1)

    with open(pickle_file, 'w+b') as pf:
        pickle.dump(scheduler, pf)

    with open(pickle_file, 'rb') as f:
        scheduler = pickle.load(f)
        return scheduler


def get_collaborator(mode: str = VANILLA) -> Union[DemoHeteroCollaborator,
                                                   DemoSecureHeteroCollaborator]:
    assert mode in (VANILLA, SECURE), f'unknown mode: {mode}'

    pickle_file = './scheduler_collaborator.pickle'

    if os.path.exists(pickle_file):
        os.remove(pickle_file)

    if mode == VANILLA:
        scheduler = DemoHeteroCollaborator(feature_key='demo_collaborator',
                                           batch_size=128,
                                           data_dir=_DATA_DIR,
                                           name='demo_hetero_collaborator',
                                           data_channel_timeout=(200, 200))

    else:
        scheduler = DemoSecureHeteroCollaborator(feature_key='demo_collaborator',
                                                 project_layer_lr=0.01,
                                                 batch_size=128,
                                                 data_dir=_DATA_DIR,
                                                 name='demo_hetero_collaborator',
                                                 data_channel_timeout=(200, 200))

    with open(pickle_file, 'w+b') as pf:
        pickle.dump(scheduler, pf)

    with open(pickle_file, 'rb') as f:
        scheduler = pickle.load(f)
        return scheduler
