"""Module for loading and convering datasets across various storage formats."""
import csv
import os

from typing import Union
from pathlib import Path
import xml.etree.ElementTree as ET

import pandas as pd

from .label import Label
from .dataset import DeidDataset

def load_label(filename: Union[str, Path]) -> Label:
    """
    Loads annotations from a CSV file.
    CSV file should have entity_type/start/stop columns.
    """
    with open(filename, 'r') as fp:
        csvreader = csv.reader(fp, delimiter=',', quotechar='"')
        header = next(csvreader)
        # identify which columns we want
        idx = [
            header.index('entity_type'),
            header.index('start'),
            header.index('stop'),
            header.index('entity')
        ]

        # iterate through the CSV and load in the labels
        labels = [
            Label(
                entity_type=row[idx[0]].upper(),
                start=int(row[idx[1]]),
                length=int(row[idx[2]]) - int(row[idx[1]]),
                # entity=row[idx[3]]
            ) for row in csvreader
        ]

    return labels

def _read_file(data_dir, input_file, delimiter=',', quotechar='"'):
    """Reads a comma separated value file."""
    fn = data_dir / input_file
    with open(fn, "r") as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        lines = []
        for line in reader:
            lines.append(line)
    return lines

def _read_tsv(input_file, quotechar=None):
    """Reads a tab separated value file."""
    return _read_file(input_file, delimiter='\t', quotechar=quotechar)

def _read_csv(input_file, quotechar='"'):
    """Reads a comma separated value file."""
    return _read_file(input_file, delimiter=',', quotechar=quotechar)

def read_task(input_dir: Union[str, Path]):
    """Read data from disk using the given format."""
    examples = {'guid': [], 'text': [], 'ann': []}

    input_dir = Path(input_dir)

    # for deid datasets, "path" is a folder containing txt/ann subfolders
    # "txt" subfolder has text files with the text of the examples
    # "ann" subfolder has annotation files with the labels
    txt_path = input_dir / 'txt'
    ann_path = input_dir / 'ann'
    for f in os.listdir(txt_path):
        if not f.endswith('.txt'):
            continue

        # guid is the file name
        guid = f[:-4]
        with open(txt_path / f, 'r') as fp:
            text = ''.join(fp.readlines())

        # load the annotations from disk
        # these datasets have consistent folder structures:
        #   root_path/txt/RECORD_NAME.txt - has text
        #   root_path/ann/RECORD_NAME.gs - has annotations
        labels = load_label(ann_path / f'{f[:-4]}.gs')

        examples['guid'].append(guid)
        examples['text'].append(text)
        examples['ann'].append(labels)

    # shared representation of data:
    return Task(examples)

def write_task(task: Task, output_dir: Union[str, Path], format: str='csv'):
    """Write data from a task out to disk using the given format."""
    output_dir = Path(output_dir)
    txt_dir = output_dir / 'txt'
    ann_dir = output_dir / 'ann'

    output_dir.mkdir(exist_ok=True)
    txt_dir.mkdir(exist_ok=True)
    ann_dir.mkdir(exist_ok=True)

    for i, guid in enumerate(task.data['guid']):
        with open(txt_dir / f'{guid}.txt', 'w') as fp:
            fp.write(task.data['text'][i])
        
        with open(ann_dir / f'{guid}.ann', 'w') as fp:
            csvwriter = csv.writer(fp)
            csvwriter.writerow(['start','length','entity_type'])
            # call label method to convert into list
            csvwriter.writerows([l.tolist() for l in task.labels[i]])

def bioc2df(filename: Union[str, Path], encoding: str='UTF-8') -> pd.DataFrame:
    """Given an XML annotation file, output a DataFrame with notes.
    The XML format is a "standoff" format: BioC.
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3889917/
    https://github.com/2mh/PyBioC/blob/master/BioC.dtd
    A sample of this XML would look like:
        <annotation id="11">
            <infon key="type">Doctor Last Name</infon>
            <infon key="pattern">Name Pattern1</infon>
            <location length="4" offset="831"/>
            <text>____</text>
        </annotation>
    Optionally specify the encoding. Default is 'UTF-8'.
    A common option is Latin-1, or 'ISO-8859-1'
    """

    cols = [
        'document_id', 'column', 'annotator', 'start', 'stop', 'entity',
        'replacement', 'entity_type', 'confidence'
    ]
    df = pd.DataFrame(columns=cols)

    # read the xml file
    with open(filename, 'r', encoding=encoding) as f:
        xml_data = f.read()

    # parse the string
    tree = ET.fromstring(xml_data)

    for doc in tree.iter('document'):
        # document ID
        document_id = doc.find('id').text

        passage = doc.find('passage')

        # loop through annotations and add them to the dataframe
        anns = list()
        for ann in passage.iter('annotation'):
            pattern_name = None
            pattern_type = None
            # loop through infon fields
            # if any match, update the corresponding variable
            for infon in ann.iter('infon'):
                if infon.attrib['key'] == 'type':
                    pattern_type = infon.text
            text = ann.find('text').text
            loc = ann.find('location')
            start = int(loc.attrib['offset'])
            stop = start + int(loc.attrib['length'])

            anns.append(
                [
                    document_id, None, pattern_name, start, stop, text, None,
                    pattern_type, None
                ]
            )

        anns = pd.DataFrame(anns, columns=cols)
        df = pd.concat([df, anns], axis=0, ignore_index=True)

    return df


def bioc2text(filename: Union[str, Path], encoding: str='UTF-8') -> list:
    """Given an XML annotation file, extract the passages as a list.
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3889917/
    https://github.com/2mh/PyBioC/blob/master/BioC.dtd
    A sample of this XML would look like:
        <annotation id="11">
            <infon key="type">Doctor Last Name</infon>
            <infon key="pattern">Name Pattern1</infon>
            <location length="4" offset="831"/>
            <text>____</text>
        </annotation>
    Optionally specify the encoding. Default is 'UTF-8'.
    A common option is Latin-1, or 'ISO-8859-1'
    """

    # read the xml file
    with open(filename, 'r', encoding=encoding) as f:
        xml_data = f.read()

    # parse the string
    tree = ET.fromstring(xml_data)
    passages = []

    for doc in tree.iter('document'):
        # document ID
        # document_id = doc.find('id').text
        passage = doc.find('passage')
        passages.append(passage.find('text').text)

    return passages


def brat2df(filename: Union[str, Path]) -> pd.DataFrame:
    """Read a file with brat standoff annotations into a dataframe.
    brat format annotations follow the same basic structure:
        - Each line contains one annotation
        - Each annotation is given an ID that appears first on the line,
          separated from the rest of the annotation by a single TAB character.
    The rest of the structure varies by annotation type. For details, see:
    http://brat.nlplab.org/standoff.html
    Optionally, the function can output the annotations to a file.
    Here is an example of the annotation format read by the function:
        T1  Organization 0 4    Sony
        T2  MERGE-ORG 14 27 joint venture
        T3  Organization 33 41  Ericsson
        T4  Date 55 65;70 72	May 19, 22 23
        E1  MERGE-ORG:T2 Org1:T1 Org2:T3
        T4  Country 75 81   Sweden
        R1  Origin Arg1:T3 Arg2:T4
    Note that the "date" is a multi-segment annotation, where entities are
    non-continuous.
    """

    cols = [
        'document_id', 'annotation_id', 'start', 'stop', 'entity', 'entity_type'
    ]

    if isinstance(filename, str):
        filename = Path(filename)

    if not filename.exists():
        raise Exception('File not found.')

    # assume input is a path to a file
    with open(filename, 'r') as fp:
        text = ''.join(fp.readlines())

    # remove file extension for doc id
    doc_id = filename.stem

    # split into a list
    text = text.split('\n')
    annot = list()
    for a in text:
        segments = None
        if a == '':
            continue
        ann = a.split('\t')

        # check for multi-segment annotations
        if ';' in ann[1]:
            segments = ann[1].split(';')
            entity_type, start, stop = segments[0].split(' ')
            start = int(start)
            stop = int(stop)
            segments = segments[1:]
            # split segments into start/stop
            segments = [s.split(' ') for s in segments]
            extra_entities = list()
            # create a list of secondary entities
            e_start = stop - start
            for s in segments:
                segment_length = int(s[1]) - int(s[0]) + 1
                e = ann[2][e_start + 1:e_start + segment_length]
                extra_entities.append(e)
                e_start += segment_length

            entity = ann[2][0:stop - start]

        else:
            entity_type, start, stop = ann[1].split(' ')
            start = int(start)
            stop = int(stop)
            entity = ann[2]

        # replace escaped newlines with real newlines
        if '\\n' in entity:
            entity = entity.replace('\\n', '\n')

        annot.append([doc_id, ann[0], start, stop, entity, entity_type])

        if segments:
            # add in additional segments for multi-segment annotation
            for i, s in enumerate(segments):
                annot.append(
                    [
                        doc_id, ann[0], s[0], s[1], extra_entities[i],
                        entity_type
                    ]
                )

    df = pd.DataFrame(annot, columns=cols)
    return df


def brat2text(filename: Union[str, Path]) -> str:
    """Read a text file associated with a brat annotation file."""
    with open(filename, 'r') as fp:
        return ''.join(fp.readlines())

def load_hdf5(filename: Union[str, Path]) -> dict:
    pass