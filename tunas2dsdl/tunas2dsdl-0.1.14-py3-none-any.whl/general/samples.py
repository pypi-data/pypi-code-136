from .utils import Util


class DataSample:
    def __init__(self, struct, class_domain):
        self.sample_struct = struct
        self.class_domain = class_domain
        self.samples = []

    def add_item(self, item, pre_format=True):
        if pre_format:
            sample = self.add_quotes(item.copy())
            for k, v in sample.items():
                if Util.is_list_of(v, dict):
                    sample[k] = [Util.fmap(_) for _ in v]
            self.samples.append(sample)
        else:
            self.samples.append(item)

    def add_quotes(self, sample):
        if isinstance(sample, dict):
            for k, v in sample.items():
                sample[k] = self.add_quotes(v)
        elif isinstance(sample, list):
            for k, v in enumerate(sample):
                sample[k] = self.add_quotes(v)
        elif isinstance(sample, str):
            sample = Util.add_quotes(sample)

        return sample

    def set_domain(self, domain):
        if not isinstance(domain, list):
            self.class_domain = [domain]
        else:
            self.class_domain = domain

    @property
    def sample_type(self):
        ARG = self.sample_struct.args
        if not ARG:
            return self.sample_struct.name
        if not isinstance(ARG, list):
            ARG = [ARG]
        class_domain = self.class_domain
        if not isinstance(self.class_domain, list):
            class_domain = [class_domain]
        class_domain_name = [_.name for _ in class_domain]
        assert len(ARG) == len(class_domain_name), "argument and value not match"
        string = ', '.join(["=".join(item) for item in zip(ARG, class_domain_name)])
        return f"{self.sample_struct.name}[{string}]"

    def format(self, file_name="$local"):
        content = dict()
        content["sample-type"] = self.sample_type
        content["sample-path"] = file_name
        content["samples"] = self.samples
        return {"data": content}
