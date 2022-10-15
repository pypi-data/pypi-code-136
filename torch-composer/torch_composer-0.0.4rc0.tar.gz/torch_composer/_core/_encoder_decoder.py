

from ._torch_net import TorchNet
import numpy as np


class BaseEncoderDecoder:
    def __init__(self):
        super(BaseEncoderDecoder, self).__init__()

    def _power_space(start, stop, n, power):

        start = np.power(start, 1 / float(power))
        stop = np.power(stop, 1 / float(power))

        return np.power(np.linspace(start, stop, num=n), power).astype(int)

    def _direction(self, data_dim, latent_dim):
        if hasattr(self, "ENCODER"):
            return data_dim, latent_dim
        if hasattr(self, "DECODER"):
            return latent_dim, data_dim

    def __compose__(self, data_dim, latent_dim, hidden_layers, power, dropout=0.5):

        START_DIM, STOP_DIM = self._direction(self, data_dim, latent_dim)
        pow_space = self._power_space(
            START_DIM, STOP_DIM, int(hidden_layers + 2), power
        )
        EncoderDecodeerDict = {}
        for n, (i, j) in enumerate(zip(pow_space[1:-1], pow_space[2:-1])):
            EncoderDecodeerDict[int(n + 1)] = [i, j]

        return TorchNet(
            START_DIM, STOP_DIM, hidden=EncoderDecodeerDict, dropout=dropout
        )


class TorchNetDecoder(BaseEncoderDecoder):
    DECODER = True

    def __init__(self):
        super(self, TorchNetDecoder).__init__()

    def __new__(self, data_dim, latent_dim, hidden_layers=3, power=2, dropout=0.5):
        return self.__compose__(
            self,
            data_dim,
            latent_dim,
            hidden_layers=hidden_layers,
            power=power,
            dropout=dropout,
        )


class TorchNetEncoder(BaseEncoderDecoder):
    ENCODER = True

    def __init__(self):
        super(TorchNetEncoder, self).__init__()

    def __new__(self, data_dim, latent_dim, hidden_layers=3, power=2, dropout=0.5):
        return self.__compose__(
            self,
            data_dim,
            latent_dim,
            hidden_layers=hidden_layers,
            power=power,
            dropout=dropout,
        )