import logging
from typing import Dict, List, NamedTuple, Optional

from cradlebio import watch

from google.cloud import firestore


class CachedData(NamedTuple):
    user_id: str  # the firebase user id of the user who owns the data
    # the location of the cached data in Firebase
    location: str


class Cache:
    """
    Caches already folded proteins.
    The cache contains AFAAS's previously folded proteins.
    Caching assumes all folding happens with default parameters, i.e. no parameter-specific caching is supported (yet).
    """

    def __init__(self, db_client: firestore.Client, sequence_collection_id='sequences'):
        """
        Creates a new cache instance and loads the data from the given Firestore database.
        Parameters:
            db_client: Firestore client, authenticated with a privileged service account
            sequence_collection_id: the Firestore collection id where sequences are cached
        """

        self.cache: Dict[str:CachedData] = {}
        self.db_client = db_client
        self.sequence_collection = db_client.collection(sequence_collection_id)
        self.sequence_collection.on_snapshot(self._get_snapshot())

    def _get_snapshot(self):
        def on_snapshot(col_snapshot: List[firestore.DocumentSnapshot], changes: List[watch.DocumentChange], _):
            try:
                for document, change in zip(col_snapshot, changes):
                    if change.type in {watch.ChangeType.ADDED}:
                        seq = document.get('seq')
                        if isinstance(seq, list):
                            seq = ':'.join(seq)
                        user_id = document.get('user')
                        if seq in self.cache and self.cache[seq].user_id == user_id:
                            logging.info(f'Sequence {seq} already in cache for user {user_id}')
                            continue
                        self.cache[seq] = CachedData(user_id, document.get('location'))
                        logging.info(f'Sequence {seq} added to cache')
            except Exception as e:
                logging.error(str(e))
                raise

        return on_snapshot

    def get(self, user_id: str, proteins: List[str]) -> Dict[str, CachedData]:
        """ Looks up the list of proteins in the cache, and returns the folding, if available. """
        result = {}
        for protein in proteins:
            # make sure we only return the protein if it's owned by the user or if it has no owner
            if protein in self.cache and (self.cache[protein].user_id == user_id or self.cache[protein].user_id == ''):
                result[protein] = self.cache[protein]
        return result

    def get_single(self, user_id: str, protein: str) -> Optional[CachedData]:
        """ Looks up a single protein in the cache, and returns the folding, if available. """
        if protein not in self.cache:
            return

        # make sure we only return the protein if it's owned by the user or if it has no owner
        if self.cache[protein].user_id not in {user_id, ''}:
            return

        return self.cache[protein]

    def __len__(self):
        return len(self.cache)
