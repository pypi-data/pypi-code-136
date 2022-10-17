import abc


class ConsensusClustering(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def consensus_cluster(self, patient_list):
        pass
