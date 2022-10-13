"""Client library for folding proteins using Cradle's implementation of Alphafold.

Example::

    from cradlebio import alphafold

    creds_path = 'path to JSON firebase credentials obtained from https://auth.internal.cradle.bio/'
    fasta_file = 'path to fasta file containing proteins to be folded'
    sequences = alphafold.predict(creds_path, fasta_file)

    for sequence in sequences:
        print(f'PDB file for folded sequence {sequence.name} is {await sequence.pdb()}')
"""
import concurrent
import os
from concurrent.futures import Future
from datetime import datetime
from enum import Enum
import json
import logging
import hashlib
from pathlib import Path
from typing import Dict, List, Union, Optional, TextIO, Tuple
import sys

import fsspec
from Bio import SeqIO
from fsspec.core import OpenFile
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.api_core.exceptions import PermissionDenied, AlreadyExists
from google.cloud import firestore

from cradlebio import auth
from cradlebio import watch

CRADLE_GCS_BUCKET = 'cradle-bio.appspot.com'
JOBS = 'jobs'  # the name of the sub-collection where jobs are stored in Firebase
SEQUENCES = 'sequences'  # name of the sub-collection within jobs where sequences are stored
FIRESTORE_PREFIX = ''
DONE_JOB_STATUS = frozenset(('DONE', 'MSA_FAILED', 'FOLDING_FAILED'))


class MsaException(Exception):
    """Indicator class for a server-side error during Multiple Sequence Alignment (MSA)"""
    pass


class PdbException(Exception):
    """Indicator class for a server-side error during sequence folding"""
    pass


class AmberRelax(Enum):
    """ Which of the generated PDB files should be relaxed using Amber relaxation """
    ALL = 0  # relax all 5 PDBs
    BEST = 1  # relax only the best PDB (by plddt score)
    NONE = 2  # don't relax the PDBs at all


def _assign_name(sequence: str, idx: int, hash_len: int = 4):
    seq_hash = hashlib.md5(sequence.encode('utf-8'))
    return f'{idx}_{int(seq_hash.hexdigest(), 16) % (10 ** hash_len)}'


class Sequence:
    """
    Represents a single named and optionally described amino acid chain.

    A single `Sequence` object can be created from:
        * `string`: using ``Sequence.from_str()``

    The input to a folding job is a list of ``Sequence`` objects. It can be created from:
        * `list`: using ``Sequence.from_list()``
        * `dict`: using ``Sequence.from_dict()``
        * `fasta`: using ``Sequence.from_fasta()``

    see their respective docstrings for usage.
    """

    def __init__(
            self,
            sequence: str,
            *,
            name: str,
            description: Optional[str]):
        self.sequence = sequence
        self.name = name
        self.description = description

    def __repr__(self):
        return 'Sequence(' + \
               f'sequence={self.sequence}, name=\'{self.name}\'' + \
               (f', description={self.description}' if self.description else '') + \
               ')'

    def to_fasta(self):
        """
        Returns:
            a fasta formatted `string` representing the ``Sequence`` object

        Examples:
            ::

                from cradlebio.alphafold import Sequence
                sequence = Sequence.from_str("BANANA", name='banana', description='yellow')
                sequence.to_fasta()

            .. code-block:: console

                >banana | yellow
                BANANA
        """
        description = '| ' + (self.description or '')
        return f'>{self.name}{description}\n' \
               f'{self.sequence}'

    @staticmethod
    def from_str(
            sequence: str,
            *,
            name: Optional[str] = None,
            description: Optional[str] = None,
    ) -> 'Sequence':
        """
        Creates a ``Sequence`` object from a `string` representing its amino acid sequence.

        Args:
            sequence:
                an amino acid sequence (`string`)
            name:
                a name for the ``Sequence`` object, if not provided it will be assigned based on a 4-letter hash of its amino acid sequence
            description:
                a description for the Sequence object

        Returns:
            a ``Sequence`` object
        Examples:
            ::

                from cradlebio.alphafold import Sequence
                sequence = Sequence.from_str("BANANA", name='banana', description='yellow')
                other_sequence = Sequence.from_str("ZEBRA")
                print(sequence)
                print(other_sequence)

            .. code-block:: console

                Sequence(sequence='BANANA', name='banana', description='yellow')
                Sequence(sequence='ZEBRA', name='0_2110')
        """
        return Sequence(
            sequence,
            name=name or _assign_name(sequence, 0),
            description=description,
        )

    @staticmethod
    def from_fasta(path: Union[str, Path, TextIO]) -> List['Sequence']:
        """
        Creates a list ``Sequence`` objects from a fasta file.

        Args:
            path: a `string`, `Path` (fsspec compatible) or an open file handle to the fasta file

        Returns:
            a list of ``Sequence`` objects

        Examples:
            Contents of ``seq.fasta``::

                >tr|A0A024QZA8|A0A024QZA8_HUMAN Receptor protein-tyrosine kinase
                MELQAARA...
                >tr|A0A024R0Y5|A0A024R0Y5_HUMAN ATP-dependent 6-phosphofructokinase
                MTHEEHHA...

            Importing from ``seq.fasta``::

                from cradlebio.alphafold import Sequence
                sequences = Sequence.from_fasta('seq.fasta')
                print(sequences)

            .. code-block:: console

                [
                    Sequence(
                        sequence='MELQAARA...',
                        name='tr|A0A024QZA8|A0A024QZA8_HUMAN',
                        description='tr|A0A024QZA8|A0A024QZA8_HUMAN Receptor protein-tyrosine kinase'),
                    Sequence(
                        sequence='MTHEEHHA...',
                        name='tr|A0A024R0Y5|A0A024R0Y5_HUMAN',
                        description='tr|A0A024R0Y5|A0A024R0Y5_HUMAN ATP-dependent 6-phosphofructokinase'),
                ]
        """
        return [
            Sequence(
                sequence=str(chain.seq),
                name=chain.name or _assign_name(str(chain.seq), idx),
                description=chain.description,
            )
            for idx, chain in enumerate(SeqIO.parse(path, 'fasta'))
        ]

    @staticmethod
    def from_list(
            input_list: List[str],
            names: Optional[List[str]] = None,
            descriptions: Optional[List[str]] = None,
    ) -> List['Sequence']:
        """
        Creates a list of ``Sequence`` objects from a list of `strings` representing their amino acid sequences.

        Args:
            input_list: a list of amino acid sequences
            names: a list of names for each of the sequences. If not provided (or `None`) the Sequences will
                be named based on their index in the list suffixed with a 4-letter hash of their amino acid sequence
            descriptions: a list of descriptions for each of the sequences. If not provided (or `None`) the descriptions
                will not be automatically generated

        Returns:
            a list of ``Sequence`` objects

        Examples:
            ::

                from cradlebio.alphafold import Sequence
                sequences = Sequence.from_list(['BANANA', 'ZEBRA'], names=['banana seq', None])
                print(sequences)

            .. code-block:: console

                [Sequence(sequence='BANANA', name='banana seq', ...),
                 Sequence(sequence='ZEBRA', name='1_2110', ...)]
        """
        names = names or [None] * len(input_list)
        descriptions = descriptions or [None] * len(input_list)

        return [
            Sequence(
                sequence=sequence,
                name=name or _assign_name(sequence, idx),
                description=description,
            )
            for idx, (sequence, name, description)
            in enumerate(zip(input_list, names, descriptions))
        ]

    @staticmethod
    def from_dict(input_dict: Dict[str, str]) -> List['Sequence']:
        """
        Creates a list of ``Sequence`` objects from a dict containing ``{sequence_name: sequence}`` pairs.

        Args:
            input_dict: a mapping of sequence names to amino acid sequences
        Returns:
            a list of ``Sequence`` objects

        Examples:
            ::

                from cradlebio.alphafold import Sequence

                sequences = Sequence.from_dict(input_dict={
                    'banana seq': 'BANANA',
                    'zebra seq': 'ZEBRA'})

                print(sequences)

            .. code-block:: console

                [Sequence(sequence='BANANA', name='banana seq', ...),
                 Sequence(sequence='ZEBRA', name='zebra seq', ...)]
        """
        return [
            Sequence(sequence=sequence, name=name, description=None)
            for name, sequence in input_dict.items()
        ]

    def to_dict(self) -> Dict[str, str]:
        """
        Returns:
            a dict representing the ``Sequence`` object
        """
        result = {
            'name': self.name,
            'seq': self.sequence,
        }

        if self.description:
            result.update({'description': self.description})

        return result


class MultimerSequence:
    """
    Represents a single named and optionally described multimer. The amino acid chains within the multimer
    are represented as a list of their respective sequences.

    The input to a folding job can be a list of ``MultimerSequence`` objects. It can be created from:
        * list: using ``MultimerSequence.from_list()``
        * dict: using ``MultimerSequence.from_dict()``
        * fasta: using ``MultimerSequence.from_fasta()``

    see their respective docstrings for usage.
    """

    def __init__(
            self,
            chains: List[Sequence],
            *,
            name: str,
            description: Optional[str]):
        self.chains = chains
        self.description = description
        self.name = name

    def __repr__(self):
        return f'MultimerSequence(' + \
               f'sequence={self.chains}, name=\'{self.name}\'' + \
               (f', description=\'{self.description}\'' if self.description else '') +\
               ')'

    @property
    def sequence(self):
        """
        Returns:
            colon separated amino acid sequences of the multimer chains

        Examples:
            ::

                from cradlebio.alphafold import MultimerSequence

                multimer_sequences = MultimerSequence.from_list(
                    input_list=[['BANANA', 'ZEBRA'], ['RAIN', 'PEAR', 'PEAR']])

                for multimer_sequence in multimer_sequences:
                    print(multimer_sequence.sequence)


            .. code-block:: console

                BANANA:ZEBRA
                RAIN:PEAR:PEAR
        """
        return ':'.join([chain.sequence for chain in self.chains])

    def to_fasta(self):
        """
        Returns:
            a fasta formatted `string` representing the ``MultimerSequence`` object

        Examples:
            ::

                from cradlebio.alphafold import MultimerSequence

                multimer_sequences = MultimerSequence.from_list(
                    input_list=[['BANANA', 'ZEBRA'], ['RAIN', 'PEAR', 'PEAR']],
                    names=['banana zebra heterodimer', 'two pears in the rain'],
                    descriptions=['yellow and eats grass', 'probably rotten'])

                for sequence in multimer_sequences:
                   print(sequence.to_fasta())

            .. code-block:: console

                >banana zebra heterodimer| yellow and eats grass
                BANANA:ZEBRA
                >two pears in the rain| probably rotten
                RAIN:PEAR:PEAR
        """
        description = '| ' + (self.description or '')

        return f'>{self.name}{description}\n' \
               f'{self.sequence}'

    @staticmethod
    def _create_named(
            chains: List[Sequence],
            *,
            name: Optional[str],
            idx: Optional[int],
            description: Optional[str],
            hash_len: Optional[int] = 4,
    ) -> 'MultimerSequence':
        name = name or _assign_name(
            sequence=':'.join([chain.sequence for chain in chains]),
            idx=idx,
            hash_len=hash_len,
        )

        return MultimerSequence(
            chains=chains,
            name=name,
            description=description,
        )

    @staticmethod
    def from_fasta(
            input_paths: List[Union[str, Path]],
            names: Optional[List[str]] = None,
            descriptions: Optional[List[str]] = None,
    ) -> List['MultimerSequence']:
        """
        Creates a list of ``MultimerSequence`` objects from a list of fasta files each representing a multimer.

        Args:
            input_paths: a list of `strings`, `Paths` (fsspec compatible) or open file handles to the fasta files
            names: [optional] a list of names for each of the multimer sequences. If not provided (or `None`)
                they will be automatically generated, (see ``Sequence``)
            descriptions: [optional] a list of descriptions for each of the multimer sequences. If not provided
                (or `None`) they won't be automatically generated, (see ``Sequence``)
        Returns:
            a list of ``MultimerSequence`` objects

        Examples:
            Contents of ``seq.fasta``::

                >tr|A0A024QZA8|A0A024QZA8_HUMAN Receptor protein-tyrosine kinase
                MELQAARA...
                >tr|A0A024R0Y5|A0A024R0Y5_HUMAN ATP-dependent 6-phosphofructokinase
                MTHEEHHA...

            Importing from ``seq.fasta``::

                from cradlebio.alphafold import MultimerSequence
                from pathlib import Path
                multimer_sequences = MultimerSequence.from_fasta(
                    input_paths=[Path('seq.fasta')],
                    names='my first .fasta multimer',
                    descriptions='copied from uniprot')
                print(multimer_sequences)

            .. code-block:: console

                [MultimerSequence(
                    chains=[
                        Sequence(
                            sequence='MELQAARA...',
                            name='tr|A0A024QZA8|A0A024QZA8_HUMAN',
                            description='tr|A0A024QZA8|A0A024QZA8_HUMAN Receptor protein-tyrosine kinase')),
                        Sequence(
                            sequence='MELQAARA...',
                            name='tr|A0A024QZA8|A0A024QZA8_HUMAN',
                            description='tr|A0A024QZA8|A0A024QZA8_HUMAN Receptor protein-tyrosine kinase'))],
                    name='my first .fasta multimer',
                    description='copied from uniprot')]
        """
        names = names or [None] * len(input_paths)
        descriptions = descriptions or [None] * len(input_paths)

        return [
            MultimerSequence._create_named(
                chains=Sequence.from_fasta(file),
                name=name,
                description=description,
                idx=idx,
            )
            for idx, (file, name, description)
            in enumerate(zip(input_paths, names, descriptions))
        ]

    @staticmethod
    def from_list(
            input_list: List[Union[List[str], Dict[str, str]]],
            names: Optional[List[str]] = None,
            descriptions: Optional[List[str]] = None,
    ) -> List['MultimerSequence']:
        """
        Creates a list of ``MultimerSequence`` objects from a list of:
            * list of amino acid sequences
            * mapping of sequence names to amino acid sequences

        each representing the sub-chains of a multimer (and in the case of a mapping the name of the multimer).

        Args:
            input_list: a list of multimer sequences. Each multimer sequence is represented by a lists of amino acids
                sequences (`strings`) of its sub-chains
            names: [optional] a list of names for each of the multimer sequences. If not provided (or `None`)
                they will be automatically generated, (see ``Sequence``)
            descriptions: [optional] a list of descriptions for each of the multimer sequences. If not provided
                (or `None`) they won't be automatically generated, (see ``Sequence``)
        Returns:
            a list of ``MultimerSequence`` objects

        Examples:
            Passing subchains as lists of `strings`::

                from cradlebio.alphafold import MultimerSequence

                multimer_sequences = MultimerSequence.from_list(
                    [['BANANA', 'ZEBRA'], ['RAIN', 'PEAR', 'PEAR']],
                    names=['banana zebra heterodimer', 'two pears in the rain'],
                    descriptions=['yellow and eats grass', 'probably rotten'])

                print(multimer_sequences)

            .. code-block:: console

                [MultimerSequence(
                     chains=[
                         Sequence('BANANA', name='0_3065'),
                         Sequence('ZEBRA', name='1_2110')],
                     name='banana zebra heterodimer',
                     description='yellow and eats grass'),
                 MultimerSequence(
                     chains=[
                         Sequence('RAIN', name='0_8772'),
                         Sequence('PEAR', name='1_8874')],
                         Sequence('PEAR', name='2_8874')]
                     name='two pears in the rain',
                     description='probably rotten')]

            Passing subchains as dictionaries::

                from cradlebio.alphafold import MultimerSequence

                multimer_sequences = MultimerSequence.from_list(
                    [{'banana seq': 'BANANA', 'zebra seq': 'ZEBRA'}],
                    names=['banana zebra heterodimer'],
                    descriptions=['yellow and eats grass'])

                print(multimer_sequences)

            .. code-block:: console

                [MultimerSequence(
                 chains=[Sequence('BANANA', name='banana seq'), Sequence('ZEBRA', name='zebra seq')],
                 name='banana zebra heterodimer',
                 description='yellow and eats grass')]
        """
        names = names or [None] * len(input_list)
        descriptions = descriptions or [None] * len(input_list)

        if not all(isinstance(x, (list, dict)) for x in input_list):
            raise ValueError(f'Expected a list of lists.')

        return [
            MultimerSequence._create_named(
                chains=(
                    Sequence.from_list(chains) if isinstance(chains, list)
                    else Sequence.from_dict(chains)
                ),
                name=name,
                description=description,
                idx=idx,
            )
            for idx, (chains, name, description)
            in enumerate(zip(input_list, names, descriptions))
        ]

    @staticmethod
    def from_dict(
            input_dict: Dict[str, Union[List[str], Dict[str, str]]],
    ) -> List['MultimerSequence']:
        """
        Creates a list of ``MultimerSequence`` objects from a dict.

        Args:
            input_dict: a mapping of multimer sequence names to one of:

                * list of amino acid sequences (`strings`) of its sub-chains
                * mapping of sub-chain names to its amino acid sequences (`strings`)

        Returns:
            a list of ``MultimerSequence`` objects

        Examples:
            Building from a mapping of sub-chain names to amino acid sequences::

                 from cradlebio.alphafold import MultimerSequence

                 multimer_sequences = MultimerSequence.from_dict({
                     'banana zebra heterodimer': {
                         'banana seq': 'BANANA',
                         'zebra seq': 'ZEBRA'
                     }
                 })

                 print(multimer_sequences)

            .. code-block:: console

                 [MultimerSequence(
                    chains=[Sequence('BANANA', name='banana seq'),
                            Sequence('ZEBRA', name='zebra seq'),],
                    name='banana zebra heterodimer'
                 )]

            Building from list of amino sub-chain amino acid sequences::

                    from cradlebio.alphafold import MultimerSequence

                    multimer_sequences = MultimerSequence.from_dict(
                        input_dict={'zebra homodimer': ['ZEBRA', 'ZEBRA']})

                    print(multimer_sequences)

            .. code-block:: console

                    [MultimerSequence(
                            chains=[Sequence('ZEBRA', name='0_2110'),
                                    Sequence('ZEBRA', name='1_2110')],
                            name='zebra homodimer',
                    )]
        """
        if not all(isinstance(x, (list, dict)) for x in input_dict.values()):
            raise ValueError(f'Expected a dict of lists or dict of dicts')

        return [
            MultimerSequence(
                chains=(
                    Sequence.from_dict(chains) if isinstance(chains, dict)
                    else Sequence.from_list(chains)
                ),
                name=name,
                description=None,
            )
            for name, chains in input_dict.items()
        ]

    def to_dict(self):
        """
        Returns:
            a dict representing the ``MultimerSequence`` object
        """
        result = {
            'name': self.name,
            'seq': [chain.sequence for chain in self.chains],
            'chain_names': [chain.name for chain in self.chains]
        }

        if self.description:
            result.update({'description': self.description})

        chain_descriptions = [chain.description or '' for chain in self.chains]
        if any(chain_descriptions):
            result.update({'chain_descriptions': [desc for desc in chain_descriptions]})

        return result


class Protein:
    """A protein sequence that is being folded by AlphaFold.

    This object is immutable and represents the state of folding at the moment of object creation.

    To get an updated copy run::

        protein: Protein = protein.update()

    Some functions will only return values after significant computation such as ``protein.a3m()`` or ``protein.pdb()``
    for these functions, the convenience method ``with_a3m`` and ``with_pdb`` will return a `Future` the result of which
    is a copy of the ``Protein`` object where those fields are available.

    For example:

    Print out protein IDs and scores::

        from concurrent.futures import as_completed
        from cradlebio import auth, alphafold, Sequence

        credentials = auth.authorize()
        folder = alphafold.Alphafold(credentials)
        sequences = Sequence.from_list(['BANANA', 'ZEBRA'], names=['banana seq', None])
        proteins = folder.predict(sequences)

        for protein_future in as_completed(s.with_pdb() for s in proteins):
            protein = protein_future.result()
            print(f'Name: {protein.name} Scores: {protein.to_dict()["ptms"]}')

    Or launch followup computation once each protein has completed::

        def my_callback(sequence_future: 'Future[Sequence]'):
            seq = sequence_future.result()
            # Do stuff

        sequences = client.predict(my_sequences)
        for seq in sequences:
            seq.with_pdbs().add_done_callback(my_callback)

    See `concurrent.futures` for full details on how to use these objects.
    """
    _snapshot: firestore.DocumentSnapshot

    def __init__(self, snapshot: firestore.DocumentSnapshot):
        self._snapshot = snapshot

    def __str__(self) -> str:
        return f'Id: {self.id}\n{json.dumps(self.to_dict(), indent=4)}'

    @property
    def id(self) -> str:
        """This ``Protein``'s id."""
        return self._snapshot.id

    @property
    def name(self) -> str:
        """The name of this ``Protein``'s amino acid sequence."""
        return self._snapshot.get('name')

    @property
    def seq(self) -> str:
        """This ``Protein``'s amino acid sequence."""
        return self._snapshot.get('seq')

    @property
    def _user_id(self) -> str:
        # the path to a sequence is 'users/<user_id>/jobs/<job_id>/sequences/<sequence_id>'
        return self._snapshot.reference._path[-5]

    def update(self) -> 'Protein':
        """
        Returns:
            an updated version of this ``Protein`` object
        """
        return Protein(self._snapshot.reference.get())

    def to_dict(self) -> Dict:
        """
        Returns:
            a dict representation of the ``Protein`` object
        """
        return self._snapshot.to_dict()

    def parent(self) -> 'Job':
        """
        Returns:
             the job this ``Protein`` belongs to
        """
        return Job(self._snapshot.reference.parent.parent)

    @property
    def a3m_path(self) -> Optional[str]:
        """Serializable path to the a3m file, or `None` if it is not available."""
        a3m_path = self._snapshot.get('a3m')
        if a3m_path:
            return os.path.join(f'gs://{CRADLE_GCS_BUCKET}', a3m_path)

    def a3m(self) -> Optional[OpenFile]:
        """Get a reference to the .a3m file produced by the input MSA for this protein.

        Note this is a reference, and the file will not actually be opened until used in a context manager, e.g::

            with protein.a3m() as f:
                alignment = Bio.AlignIO.parse(f, 'fasta')

        This reference is not serializable, so if you need to store the location for later use, use ``protein.a3m_path``.
        """

        if self.a3m_path:
            with auth.fsspec_creds(self._snapshot._client._credentials):
                return fsspec.open(self.a3m_path, mode='rt')
        else:
            return None

    @property
    def pdb_relaxed_paths(self) -> Tuple[str]:
        """Serializable references to relaxed PDB file locations, if any are available."""
        result = self.to_dict()
        if 'gcs_path' in result:
            return tuple(
                os.path.join(f'gs://{CRADLE_GCS_BUCKET}', result['gcs_path'], p)
                for p in result.get('pdbs', [])
            )
        else:
            return tuple()

    @property
    def pdb_unrelaxed_paths(self) -> Tuple[str]:
        """Serializable references to unrelaxed PDB file locations, if any are available."""
        result = self.to_dict()
        if 'gcs_path' in result:
            return tuple(
                os.path.join(f'gs://{CRADLE_GCS_BUCKET}', result['gcs_path'], p)
                for p in result.get('pdbs_unrelaxed', [])
            )
        elif 'pdbs' in result:
            # From EMBL cache
            return tuple(result['pdbs'])
        else:
            return tuple()

    def pdb(self, rank: int = 0, relaxed: bool = True) -> OpenFile:
        """Get references to PDB files.

        Note this is a reference, and the file will not actually be opened until used in a context manager, e.g::

            with protein.pdb() as f:
                struct = Bio.PDB.PDBParser.PDBParser().get_structure('my_structure_tag', f)

        Args:
            rank: which ensemble ID (ordered by output pTM) to get the file for
            relaxed: whether to get the reference for `PDB` after `AMBER` relaxation or not

        Returns:
            an ``OpenFile`` object if it is available.

        Raises:
            `IndexError` if the requested PDB is not available.

                This can happen in three situations.

                    1. Relaxation was not requested for the PDB e.g. you set ``rank=1`` and the job was invoked with
                    ``relax=AmberRelax.BEST`` or the structure you requested was found in the EMBL cache.

                    2. Folding is not yet complete.

                    3. Folding has errored.


                You can ensure this will happen only in the first case by using a ``Protein`` object from a
                ``with_pdbs`` call (see Examples) or by using a callback (see class docstring for details)

        Examples:
            Ensuring only the first case can raise `IndexError` by using a ``Protein`` object from a ``with_pdbs``
            call:

            .. code-block::

                protein: Protein = protein.with_pdbs().result()  # Blocks until complete
        """
        # TODO Fix this to zip up different outputs of folding in a proper dataclass object
        if relaxed:
            path = self.pdb_relaxed_paths[rank]
        else:
            path = self.pdb_unrelaxed_paths[rank]

        with auth.fsspec_creds(self._snapshot._client._credentials):
            return fsspec.open(path, mode='rt')

    def with_a3m(self) -> 'Future[Protein]':
        """
        Fetches the alignment file for the given protein, waiting for it to be generated if needed.

        Returns:
            a Future object, the successful ``result()`` of which returns a copy the current ``Protein``.
            The ``a3m()`` method of the returned protein is guaranteed to return a reference to the
            ``.a3m`` file representing the MSA for this sequence
        """
        return watch.callback_future(self._snapshot.reference, self._a3m_callback)

    def with_pdbs(self) -> 'Future[Protein]':
        """
        Fetches the structure file for the given protein, waiting for it to be generated if needed.

        Returns:
            a Future object, the successful ``result()`` of which returns a copy the current ``Protein``.
            The ``pdb()`` method of the returned protein is guaranteed to return a reference to the
            ``.pdb`` file representing this sequence
        """
        return watch.callback_future(self._snapshot.reference, self._pdb_callback)

    def _a3m_callback(self, document: firestore.DocumentSnapshot) -> 'Protein':
        result = document.to_dict()
        if 'a3m' in result:
            return Protein(document)

        elif 'a3m_error' in result:
            logging.error(f"Error performing MSA for {self.name}: {result['a3m_error']}")
            raise MsaException(result['a3m_error'])

    def _pdb_callback(self, document: firestore.DocumentSnapshot) -> 'Protein':
        result = document.to_dict()
        if 'pdbs' in result or 'pdbs_unrelaxed' in result:
            return Protein(document)

        if 'pdb_error' in result:
            logging.error(f"Error folding {self.name}: {result['pdb_error']}")
            raise PdbException(result['pdb_error'])
        elif 'a3m_error' in result:
            logging.error(f"Error performing MSA for {self.name}: {result['a3m_error']}")
            raise MsaException(result['a3m_error'])


class Job:
    """A protein-folding job."""
    _doc: firestore.DocumentReference
    _ready: 'Optional[Future[str]]'

    def __init__(self, job_doc: firestore.DocumentReference):
        self._doc = job_doc
        self._ready = None

    @property
    def id(self) -> str:
        """``Job`` id, can be used to fetch the ``Job``, see ``Alphafold.get_job_by_id``."""
        return self._doc.id

    @property
    def data(self) -> Dict[str, str]:
        """Information about the ``Job``."""
        return self._doc.get().to_dict()

    @property
    def status(self) -> str:
        """Status of the ``Job``."""
        return self.data["status"]

    @property
    def ready(self) -> 'Future[str]':
        """A Future returning the status `string` once it is available."""
        if self._ready is None:
            self._ready = watch.field(self._doc, 'status')
        return self._ready

    @property
    def proteins(self):
        """A dictionary of ``Protein`` s associated with this job, where keys are sequence names."""
        return {
            seq_doc.get('name'): Protein(seq_doc)
            for seq_doc in self._doc.collection(SEQUENCES).stream()
        }

    def __repr__(self):
        data = {k: v for k, v in self.data.items() if not isinstance(v, DatetimeWithNanoseconds)}
        return f'Job: {self.id}\n{json.dumps(data, indent=4)}'


class _DuplicationStatus(Enum):
    OK = 'ok'
    AA_SEQUENCE = 'duplicate aa sequence with different names'
    FULL = 'duplicate aa sequence with same name'


def _check_for_duplicates(
        sequence: Union[Sequence, MultimerSequence],
        rev_map: Dict[str, List[str]],
        result: Dict[str, Protein]
) -> _DuplicationStatus:
    aa_sequence = sequence.sequence
    if aa_sequence not in rev_map:
        return _DuplicationStatus.OK

    logging.info(f'Duplicate amino acid sequence detected...')
    if sequence.name not in result:
        return _DuplicationStatus.AA_SEQUENCE

    if sequence.name in rev_map[aa_sequence]:
        return _DuplicationStatus.FULL

    raise ValueError(
        f'Multiple amino acid sequences with for name: {sequence.name},'
        'raising error to prevent data loss'
    )


def _all_of_same_type(sequences: List[Union[Sequence, MultimerSequence]]) -> bool:
    first_type = type(sequences[0])
    return all(isinstance(sequence, first_type) for sequence in sequences)


class Alphafold:
    """ Main entry point for folding proteins. """

    def __init__(self, creds: auth.IdentityPlatformTokenCredentials):
        self.creds = creds
        self.client = auth.get_client(creds)

        self.user_doc = self.client.document(f'{FIRESTORE_PREFIX}users/{self.creds.uid}')
        try:
            self.user_doc.create({})
        except PermissionDenied:
            print('Access to Cradle Alphafold is only permitted for trusted testers. Please sign up at '
                  'https://ielcu542t0e.typeform.com/to/lEzf6l1E if you would like to try Cradle Alphafold.')
            sys.exit(1)
        except AlreadyExists:
            pass

    def predict(
            self,
            sequences: List[Union[Sequence, MultimerSequence]],
            show_progress: bool = True,
            block: bool = False,
            relax: AmberRelax = AmberRelax.ALL,
            use_cache: bool = True,
    ) -> List[Protein]:
        """Predict structures from a list of Sequence or ``MultimerSequence`` objects. For creation of the inputs
        see the ``Sequence`` and ``MultimerSequence`` documentation.

        Args:
            sequences: a list of Sequence or ``MultimerSequence`` objects (mutually exclusive)
            show_progress: whether to display a progress bar for folding or not
            block: whether to block until all folding is complete or not
            relax: the ``AmberRelax`` mode to use
            use_cache: whether to fetch references to matching sequences that have already been folded or are
               in progress

        Returns:
            a list of ``Protein`` objects

        Note that if there are duplicate sequences, these will refer to the same ``Protein`` object.
        See the ``Protein`` docstring for usage.
        """

        if not isinstance(sequences, list):
            raise ValueError(f'Unexpected type {type(sequences)} for argument `sequences`. Must be a list.')

        if len(sequences) < 1:
            raise ValueError('Expected at least one sequence')

        if not _all_of_same_type(sequences):
            raise ValueError('Expected all sequences to be of the same type (`Sequence` or `MultimerSequence`).')

        if not isinstance(sequences[0], (Sequence, MultimerSequence)):
            raise ValueError(f'Unexpected type list[{type(sequences[0])}] for argument `sequences`. '
                             f'Must be a list of `Sequences` or `MultimerSequences`.')

        batch: firestore.WriteBatch = self.client.batch()
        result: Dict[str, Protein] = {}
        rev_map: Dict[str, List[str]] = {}  # input aa sequences -> all known names

        job_doc = self.user_doc.collection(JOBS).document()
        job_doc.create(
            {'creation_time': datetime.utcnow(),
             'relax': relax.name,
             'is_multimer': isinstance(sequences[0], MultimerSequence)}
        )

        job_hash = hashlib.md5()
        for sequence_count, sequence in enumerate(sequences):
            aa_sequence = sequence.sequence

            duplication_status = _check_for_duplicates(
                sequence,
                rev_map,
                result,
            )

            if duplication_status != _DuplicationStatus.OK:
                if duplication_status == _DuplicationStatus.AA_SEQUENCE:
                    logging.info('Found two differently named instances with same sequence. Reusing folding job')
                    result[sequence.name] = result[rev_map[aa_sequence][0]]
                    rev_map[aa_sequence].append(sequence.name)

                elif duplication_status == _DuplicationStatus.FULL:
                    logging.warning('Fully duplicated sequence (name and sequence), ignoring')

                continue

            if len(aa_sequence) > 1400:
                raise RuntimeError(f'Sequence {sequence.name} is too long. Sequences must be shorter than 1400 AAs')

            # since colabfold_search names sequences in the file starting with 0, we adopt
            # the same convention for convenience

            sequence_doc: firestore.DocumentReference = job_doc.collection(SEQUENCES).document(str(sequence_count))
            batch.create(
                sequence_doc, {
                    'status': 'PENDING',
                    **sequence.to_dict()
                }
            )

            sequence_fasta = sequence.to_fasta()
            logging.debug(sequence_fasta)
            job_hash.update(sequence_fasta.encode('utf-8'))

            result[sequence.name] = Protein(sequence_doc.get())
            rev_map[aa_sequence] = [sequence.name]

            if (sequence_count + 1) % 500 == 0:  # a batch supports at most 500 operations
                batch.commit()
                batch = self.client.batch()

        hash_digest = job_hash.hexdigest()
        identical_jobs = self.user_doc.collection(JOBS).where('md5sum', '==', hash_digest).get()
        if identical_jobs and use_cache:
            for seq in job_doc.collection(SEQUENCES).stream():
                seq.reference.delete()
            job_doc.delete()

            job_doc = identical_jobs[0].reference
            job = Job(job_doc)
            logging.info(f'Found job {job} with the same hash. Waiting for job to be ready.')
            job.ready.result()
            result = job.proteins
        else:
            batch.commit()
            job_doc.update({
                'status': 'PENDING',
                'md5sum': hash_digest,
                'sequence_count': sequence_count + 1,  # counts from 0
            })

        # Get fresh values in sequences:
        result = {k: seq.update() for k, seq in result.items()}
        if show_progress:
            watch.add_progress_listener(job_doc, len(result))
        if block:
            result, _ = concurrent.futures.wait((seq.with_pdbs() for _, seq in result))
        return list(result.values())

    def get_jobs(self, active_only=True) -> List[Job]:
        """
        Args:
            active_only: if `True`, only ``Jobs`` that are currently running are shown

        Returns:
            a list of alphafold ``Jobs`` for the current user. Jobs are returned ordered by creation time, starting with
            the most recent one
        """
        if active_only:
            jobs_collection = self.user_doc.collection(JOBS).where('status', 'not-in', DONE_JOB_STATUS)
        else:
            jobs_collection = self.user_doc.collection(JOBS)
        jobs = [Job(job.reference) for job in jobs_collection.stream()]
        jobs.sort(key=lambda job: job.data['creation_time'], reverse=True)
        return jobs

    def get_job_by_id(self, job_id: str) -> Union[Job, None]:
        """
        Returns:
             the ``Job`` with the given id for the authenticated user
        """
        job_doc = self.client.document(f'{FIRESTORE_PREFIX}users/{self.creds.uid}/{JOBS}/{job_id}').get()
        if job_doc.exists:
            return Job(job_doc.reference)
        return None

    def search_jobs(self, keyword: str, active_only=True):
        """
        Search all ``Jobs`` that match the given keyword.

        Args:
            keyword: `string` to search for in the ``Job`` status, ``id``, ``md5_sum`` or ``creation_time``
            active_only: if `True`, only jobs that are currently active are returned
        """
        jobs = self.get_jobs(active_only)
        if not keyword:
            return jobs
        result = []
        for j in jobs:
            search_base = [j.data['status'], j.data['md5sum'], str(j.data['creation_time']), j.id]
            for s in search_base:
                if keyword in s:
                    result.append(j)
                    break
        return result

    def mark_stale_jobs(self) -> int:
        """ Check for ``Jobs`` in the state FOLDING that haven't been updated in a long time and
        mark them as failed.

        Returns:
            the number of active ``Jobs``
        """
        jobs_collection = self.user_doc.collection(JOBS).where('status', 'in', ['FOLDING', 'MSA_RUNNING'])
        return mark_stale_jobs(jobs_collection)


def mark_stale_jobs(jobs_collection: firestore.CollectionReference):
    active_jobs = 0
    for job in jobs_collection.stream():
        job_data = job.to_dict()
        if 'last_updated' in job_data:
            last_updated = job_data['last_updated']
            if (datetime.utcnow(last_updated.tzinfo) - last_updated).total_seconds() > 5 * 60 * 60:  # no update in 5 hours
                job.reference.update({'status': 'FOLDING_FAILED', 'pdb_error': 'Timeout - no update after 5 hours'})
                active_jobs -= 1
        elif 'fold_start_time' in job_data:
            last_updated = job_data['fold_start_time']
            # no update in 24 hours
            if (datetime.utcnow(last_updated.tzinfo) - last_updated.replace(tzinfo=None)).total_seconds() > 24 * 60 * 60:
                job.reference.update({'status': 'FOLDING_FAILED', 'pdb_error': 'Timeout - no update after 24 hours'})
                continue
        active_jobs += 1
    return active_jobs
