from dataclasses import dataclass, asdict

@dataclass
class Instance(object):
    """Instance class.
    """
    labels: str
    users: str
    items: str
    cates: str
    timestamp: str
    history_item_ids: str
    history_category_ids: str
    history_timestamp: str

    def dict(self):
        return {k: [str(v)] for k, v in asdict(self).items()}

    def __str__(self):
        return '\t'.join(list(asdict(self).values()))
