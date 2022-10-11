"""
This code is based on DYGIE++'s codebase
"""

import numpy as np


def fields_to_batches(d, keys_to_ignore=[]):
    keys = [key for key in d.keys() if key not in keys_to_ignore]
    lengths = [len(d[k]) for k in keys]
    assert len(set(lengths)) == 1
    length = lengths[0]
    res = [{k: d[k][i] for k in keys} for i in range(length)]
    return res


class Document:
    def __init__(self, js):
        self._doc_key = js["doc_key"]
        entries = fields_to_batches(js, ["doc_key", "clusters", "predicted_clusters", "section_starts", "tokens",
                                         "entities", "orig_id", "relations"])
        sentence_lengths = [len(entry["sentences"]) for entry in entries]
        sentence_starts = np.cumsum(sentence_lengths)
        sentence_starts = np.roll(sentence_starts, 1)
        sentence_starts[0] = 0
        self.sentence_starts = sentence_starts
        self.sentences = [Sentence(entry, sentence_start, sentence_ix)
                          for sentence_ix, (entry, sentence_start)
                          in enumerate(zip(entries, sentence_starts))]

    def __repr__(self):
        return "\n".join([str(i) + ": " + " ".join(sent.text) for i, sent in enumerate(self.sentences)])

    def __getitem__(self, ix):
        return self.sentences[ix]

    def __len__(self):
        return len(self.sentences)

    def print_plaintext(self):
        for sent in self:
            print(" ".join(sent.text))

    @property
    def n_tokens(self):
        return sum([len(sent) for sent in self.sentences])


class Sentence:
    def __init__(self, entry, sentence_start, sentence_ix):
        self.sentence_start = sentence_start
        self.text = entry["sentences"]
        self.sentence_ix = sentence_ix
        # Gold
        if "ner" in entry:
            self.ner = [NER(this_ner, self.text, sentence_start)
                        for this_ner in entry["ner"]]
        if "relations" in entry:
            self.relations = [Relation(this_relation, self.text, sentence_start) for
                              this_relation in entry["relations"]]

    def __repr__(self):
        the_text = " ".join(self.text)
        the_lengths = np.array([len(x) for x in self.text])
        tok_ixs = ""
        for i, offset in enumerate(the_lengths):
            true_offset = offset if i < 10 else offset - 1
            tok_ixs += str(i)
            tok_ixs += " " * true_offset

        return the_text + "\n" + tok_ixs

    def __len__(self):
        return len(self.text)

    def get_flavor(self, argument):
        the_ner = [x for x in self.ner if x.span == argument.span]
        if len(the_ner) > 1:
            print("Weird")
        if the_ner:
            the_flavor = the_ner[0].flavor
        else:
            the_flavor = None
        return the_flavor


class Span:
    def __init__(self, start, end, text, sentence_start):
        self.start_doc = start
        self.end_doc = end
        self.span_doc = (self.start_doc, self.end_doc)
        self.start_sent = start - sentence_start
        self.end_sent = end - sentence_start
        self.span_sent = (self.start_sent, self.end_sent)
        self.text = text[self.start_sent:self.end_sent + 1]

    def __repr__(self):
        return str((self.start_sent, self.end_sent, self.text))

    def __eq__(self, other):
        return (self.span_doc == other.span_doc and
                self.span_sent == other.span_sent and
                self.text == other.text)

    def __hash__(self):
        tup = self.span_doc + self.span_sent + (" ".join(self.text),)
        return hash(tup)


class NER:
    def __init__(self, ner, text, sentence_start, flavor=None):
        self.span = Span(ner[0], ner[1], text, sentence_start)
        self.label = ner[2]
        self.flavor = flavor

    def __repr__(self):
        return self.span.__repr__() + ": " + self.label

    def __eq__(self, other):
        return (self.span == other.span and
                self.label == other.label and
                self.flavor == other.flavor)


class Relation:
    def __init__(self, relation, text, sentence_start):
        start1, end1 = relation[0], relation[1]
        start2, end2 = relation[2], relation[3]
        label = relation[4]
        span1 = Span(start1, end1, text, sentence_start)
        span2 = Span(start2, end2, text, sentence_start)
        self.pair = (span1, span2)
        self.label = label

    def __repr__(self):
        return self.pair[0].__repr__() + ", " + self.pair[1].__repr__() + ": " + self.label

    def __eq__(self, other):
        return (self.pair == other.pair) and (self.label == other.label)
