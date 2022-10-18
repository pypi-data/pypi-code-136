import csv

import torch

from .dataset import Task


def convert_to_bio_scheme(tokens: list) -> list:
    def b_or_i(w, w_prev):
        if w == 'O':
            return 'O'
        elif w == w_prev:
            return f'I-{w}'
        else:
            return f'B-{w}'

    return [
        [b_or_i(w, None if i == 0 else sequence[i-1]) for i, w in enumerate(sequence)]
        for sequence in tokens
    ]


class DeidDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {
            key: torch.tensor(val[idx])
            for key, val in self.encodings.items()
        }
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

    def get_example(self, i, id2label):
        """Output a tuple for the given index."""
        input_ids = self.encodings['input_ids'][i]
        attention_mask = self.encodings['attention_mask'][i]
        token_type_ids = self.encodings.encodings[i].type_ids
        label_ids = self.labels[i]
        return input_ids, attention_mask, token_type_ids, label_ids

def create_deid_dataset(texts, labels, tokenizer,
                        label2id: dict) -> DeidDataset:
    """Creates a dataset from set of texts and labels.

       Args:
            texts: dict of text data, from, e.g., DeidTask.train['text']
            labels: dict of annotations, from, e.g., DeidTask.train['ann']
            tokenizer: HuggingFace tokenizer, e.g., loaded from AutoTokenizer.from_pretrained()
            label2id: dict property of a DeidTask (see data.py)

       Returns:
            DeidDataset; see class definition in data.py
    """

    # specify dataset arguments
    split_long_sequences = True

    # split text/labels into multiple examples
    # (1) tokenize text
    # (2) identify split points
    # (3) output text as it was originally
    if split_long_sequences:
        texts, labels = split_sequences(tokenizer, texts, labels)

    encodings = tokenizer(texts,
                          is_split_into_words=False,
                          return_offsets_mapping=True,
                          padding=True,
                          truncation=True)

    # use the offset mappings in train_encodings to assign labels to tokens
    tags = assign_tags(encodings, labels)

    # encodings are dicts with three elements:
    #   'input_ids', 'attention_mask', 'offset_mapping'
    # these are used as kwargs to model training later
    tags = encode_tags(tags, encodings, label2id)

    # prepare a dataset compatible with Trainer module
    encodings.pop("offset_mapping")
    dataset = DeidDataset(encodings, tags)

    return dataset


def load_data(task_name, dataDir, testDir, tokenizerArch: str):
    """Creates a DeidTask; loads the training, validation, and test data.

       Args:
            task_name: origin of training data, e.g., 'i2b2_2014'
            dataDir: directory with training data containing two folders ('txt' and 'ann')
                divided 80-20 between training and validation sets
            testDir: directory with testing data containing two folders ('txt' and 'ann')
            tokenizerArch: name of HuggingFace pretrained tokenizer
                e.g., 'bert-base-cased'

       Returns:
            deid_task: DeidTask, see data.py
            train_dataset: DeidDataset of training data, generally 80% of train set
            val_dataset: DeidDataset of validation data, generally 20% of train set
            test_dataset: DeidDataset of training data
    """

    # specify dataset arguments
    label_transform = 'base'

    # definition in data.py
    deid_task = Task(
        task_name,
        # data_dir=f'/home/alistairewj/git/deid-gs/{task_name}',
        data_dir=dataDir,
        test_dir=testDir,
        label_transform=label_transform)

    train_texts, train_labels = deid_task.train['text'], deid_task.train['ann']
    split_idx = int(0.8 * len(train_texts))
    val_texts, val_labels = train_texts[split_idx:], train_labels[split_idx:]
    train_texts, train_labels = train_texts[:split_idx], train_labels[:split_idx]
    test_texts, test_labels = deid_task.test['text'], deid_task.test['ann']

    tokenizer = AutoTokenizer.from_pretrained(tokenizerArch)
    label2id = deid_task.label2id

    train_dataset = create_deid_dataset(train_texts, train_labels, tokenizer,
                                        label2id)
    val_dataset = create_deid_dataset(val_texts, val_labels, tokenizer,
                                      label2id)
    test_dataset = create_deid_dataset(test_texts, test_labels, tokenizer,
                                       label2id)

    return deid_task, train_dataset, val_dataset, test_dataset


def load_new_test_set(deid_task, newTestPath: str, tokenizerArch: str):
    """Sets a new dataset as the test set in the DeidTask.

       Args:
            deid_task: DeidTask to be changed, see data.py
            newTestPath: directory to new test data containing txt and ann folders
            tokenizerArch: name of HuggingFace pretrained tokenizer
                e.g., 'bert-base-cased'

       Returns:
            deid_task: modified DeidTask
            test_dataset: DeidDataset corresponding to new directory
    """

    deid_task.set_test_set(newTestPath)
    test_texts, test_labels = deid_task.test['text'], deid_task.test['ann']
    tokenizer = AutoTokenizer.from_pretrained(tokenizerArch)

    test_dataset = create_deid_dataset(test_texts, test_labels, tokenizer,
                                       deid_task.label2id)

    return deid_task, test_dataset

