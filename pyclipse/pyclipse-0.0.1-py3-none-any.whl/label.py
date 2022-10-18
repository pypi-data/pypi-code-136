"""Classes and functions for working with entity labels."""
from dataclasses import dataclass, field

"""
A label contains four attributes of primary interest:
    * entity_type - the type of entity which is labeled
    * start - the start offset of the label in the source text
    * length - the length of the label in the source text
    * entity - the actual text of the entity
"""

@dataclass
class Label:
    """Single label state"""
    entity_type: str
    start: int
    length: int
    stop: int = field(init=False)

    def __post_init__(self):
        # enforce case on entity_type
        self.entity_type = self.entity_type.lower()
        # add stop var
        self.stop = self.start + self.length

    def shift(self, offset: int):
        self.start += offset

    def contains(self, i: int) -> bool:
        """Returns true if any label contains the offset."""
        return (self.start <= i) & (self.stop > i)

    def overlaps(self, start: int, stop: int) -> bool:
        """Returns true the label overlaps the start/stop offset."""
        contains_start = (self.start >= start) & (self.start < stop)
        contains_stop = (self.stop >= start) & (self.stop < stop)
        return contains_start | contains_stop

    def within(self, start: int, stop: int) -> bool:
        """Returns true if the label is within a start/stop offset."""
        after_start = (self.start >= start) or (self.stop >= start)
        before_stop = self.start < stop
        return after_start & before_stop
    
    def tolist(self) -> list:
        """Convert class to list, useful for writing to CSV."""
        return [self.start, self.length, self.entity_type]

def shift(label: Label, offset: int) -> Label:
    label.start += offset
    return label

def contains(label, i):
    """Returns true if any label contains the offset."""
    return (label.start >= i) & ((label.start + label.length) < i)

def overlaps(label, start, stop):
    """Returns true if any label contains the start/stop offset."""
    contains_start = (label.start >= start) & (label.start < stop)
    contains_stop = ((label.start + label.length) >=
                        start) & ((label.start + label.length) < stop)
    return contains_start | contains_stop

def within(label, start, stop):
    """Returns true if the label is within a start/stop offset."""
    after_start = (label.start >= start) or ((label.start + label.length) >= start)
    before_stop = label.start < stop
    return after_start & before_stop

def convert_to_bio_scheme(labels: list) -> list:
    def b_or_i(w, w_prev):
        if w == 'O':
            return 'O'
        elif w == w_prev:
            return f'I-{w}'
        else:
            return f'B-{w}'

    return [
        Label(
            b_or_i(label.entity_type, None if i == 0 else labels[i-1].entity_type),
            label.start, label.length
        )
        for i, label in enumerate(labels)
    ]