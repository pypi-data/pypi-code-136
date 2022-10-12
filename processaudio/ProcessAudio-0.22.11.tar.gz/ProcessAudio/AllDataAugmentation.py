from ProcessAudio.AudioAugmentation import AudioAugmentation
from ProcessAudio.Features import Features


class AllDataAugmentation(AudioAugmentation):

    def __init__(self, file_path, label: list = None, path_save: str = "", grafica: bool = False):
        super().__init__(file_path, save=path_save, graph=grafica)
        self.label = label

    def build_all(self, extract_features: bool = False):
        all_data = [
            self.get_original(),
            self.add_noise(factor_ruido=0.05),
            self.add_noise2(),
            self.stretch(rate_stretch=0.8),
            self.shift(),
            self.add_crop(),
            self.loudness(),
            self.speed(),
            self.normalizer(),
            self.polarizer()
        ]

        if extract_features:
            print("Extracting features to", self.audio_file)
            all_data = self.extract_features(all_data)

        all_label = [self.label for _ in range(len(all_data))]
        return all_data, all_label

    def extract_features(self, all_data) -> list:
        """
        Extract features from all data
        :param all_data:
        :return:
        """
        features = Features()
        for i in range(len(all_data)):
            info_audio = (all_data[i], self.rate)
            features.set_data(info_audio)
            all_data[i] = features.build_all()
        return all_data
