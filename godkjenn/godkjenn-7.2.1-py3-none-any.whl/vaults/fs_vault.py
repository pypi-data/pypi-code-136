"""Simple file-system based implementation of a vault.
"""

from enum import Enum
import itertools
import json
from pathlib import Path
import shutil

from godkjenn.artifact import Artifact


class _Kind(Enum):
    accepted = "accepted"
    received = "received"


class FSVault:
    """File-system implementation of a vault.

    This creates a directory for each test-id, and this directory can have either or both of a 'received' and 'accepted'
    directory containing the actual artifacts.

    This assumes it has complete control over the files under `root_directory`. You should not modify or delete files under
    `root_directory` (unless you really know what you're doing), and you should not add files or directories there either.

    The directory structure for the vault looks like this::

        <root>/
            test-id-1/
                test-metadata.json
                accepted/
                    metadata.json
                    data
                received/
                    metadata.json
                    data
            test-id-2/
                . . .

    Note that the test-id directories may not have the same name as the test-id they represent. Some test-ids
    contain characters which are not allowed in paths, so we have an algorithm that translates them into something
    acceptable.

    Args:
        root_path: The root directory under which this will store received and accepted data.
    """

    def __init__(self, root_path):
        self._root_path = Path(root_path)

    @property
    def root_path(self) -> Path:
        "Root path of the vault."
        return self._root_path

    def accepted(self, test_id) -> Artifact:
        """Get the current accepted value for `test_id`.

        Args:
            test_id: ID of the test.

        Returns: An Artifact instance.

        Raises:
            KeyError: `test_id` does not have accepted data in the vault.
        """
        return self._get(test_id, _Kind.accepted)

    def accept(self, test_id):
        """Accept the current received data for `test_id`.

        Args:
            test_id: The ID of the test to accept.

        Raises:
            KeyError: There is no received data for `test_id`.
        """
        received_dir = self._artifact_dir_path(test_id, _Kind.received)
        if not received_dir.exists():
            raise KeyError(f"No received data for {test_id}")

        accepted_dir = self._artifact_dir_path(test_id, _Kind.accepted)
        if accepted_dir.exists():
            shutil.rmtree(accepted_dir)

        shutil.move(received_dir, accepted_dir)

    def received(self, test_id) -> Artifact:
        """Get the current received value for `test_id`.

        Args:
            test_id: ID of test.

        Returns: An Artifact describing the received data `test_id`.

        Raises:
            KeyError: There is no received data for `test_id`.
        """
        return self._get(test_id, _Kind.received)

    def receive(self, test_id, data, mime_type, encoding):
        """Set new received data for a test.

        Args:
            test_id: ID of the test for which to receive data.
            artifact: Artifact describing received data for the test.
        """
        self._put(test_id, _Kind.received, data, mime_type, encoding)

    def clear_received(self, test_id):
        """Clear any received data for a test.

        If there is not received data for a test, this does nothing.

        Args:
            test_id: The ID of the test whose received data should be cleared.
        """
        self._delete(test_id, _Kind.received)

    def ids(self):
        """Get all IDs in the vault.

        This is all IDs that have either or both of accepted and received data. There is no
        order to the results. Each ID is included only once in the output, even if it has both
        received and accepted data.

        Returns: An iterable of all test IDs.
        """
        return set(metadata[FSVault.TEST_ID_KEY] for test_dirpath, metadata in self._all_test_metadata())

    TEST_METADATA_FILE_NAME = "test-metadata.json"
    ARTIFACT_METADATA_FILE_NAME = "metadata.json"
    DATA_FILE_NAME = "data"
    TEST_ID_KEY = "test-id"
    MIME_TYPE_KEY = "mime-type"
    ENCODING_KEY = "encoding"
    PATH_TRANSLATION_TABLE = {ord(char): "_" for char in ("<", ">", ":", '"', "\\", "|", "?", "*")}

    def _all_test_metadata(self):
        """Iterable of `(test-directory, metadata)` tuples for all test-ids.

        Raises:
            ValueError: Metadata file can not be parsed as JSON.
        """
        # First, look through existing paths for test_id in some metadata. If its found, then use that path.
        for metadata_path in self.root_path.rglob(FSVault.TEST_METADATA_FILE_NAME):
            try:
                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Unable to load test metadata in {metadata_path}") from exc
            yield metadata_path.parent, metadata

    def _test_dir_path(self, test_id: str) -> Path:
        """Get the directory for a test-id.

        The directory may not exist. This simply calculates where it should be.

        Args:
            test_id: The test-id of the directory to find/create.

        Returns:
            The path to the directory for test-id.
        """
        # First, look through existing paths for test_id in some metadata. If it's found, then use that path.
        for test_dirpath, metadata in self._all_test_metadata():
            try:
                stored_test_id = metadata[FSVault.TEST_ID_KEY]
            except KeyError:
                # TODO: Should we at least log an error?
                continue

            if stored_test_id == test_id:
                return test_dirpath

        # If it's not found, generate a new path name from test_id. Make sure it doesn't collide with an existing
        # path!

        # TODO: We need to replace more than just :. Any invalid path char should be replaced.
        test_id_base_dirname = test_id.translate(FSVault.PATH_TRANSLATION_TABLE)
        for suffix in itertools.count():
            test_id_dirname = test_id_base_dirname + f"-{suffix}"
            test_id_path = self.root_path / test_id_dirname
            if not test_id_path.exists():
                test_id_path.mkdir(parents=True, exist_ok=False)
                metadata_path = test_id_path / FSVault.TEST_METADATA_FILE_NAME
                metadata = {FSVault.TEST_ID_KEY: test_id}
                with metadata_path.open(mode="wt", encoding="utf-8") as handle:
                    json.dump(metadata, handle)
                return test_id_path

    def _artifact_dir_path(self, test_id, kind: _Kind) -> Path:
        """Get the path to a particular artifact directory.

        An artifact directory is a child of a test-id directory, and it's either 'accepted' or 'received'.

        The returned directory may or may not exist.

        Args:
            test_id: The test-id for the artifact.
            kind: The kind of artifact, accepted or received.

        Returns:
            The path to the directory.
        """
        return self._test_dir_path(test_id) / kind.value

    def _get(self, test_id, kind):
        """Get an artifact for a test.

        Args:
            test_id: The test-id for the artifact to be retrieved.
            kind: The kind of artifact to retrieve (accepted or received).

        Returns:
            An `Artifact` instance.

        Raises:
            KeyError: The data or metadata for the artifact can't be found.
            KeyError: The metadata doesn't contain the correct keys.
        """
        artifact_dirpath = self._artifact_dir_path(test_id, kind=kind)
        data_path = artifact_dirpath / FSVault.DATA_FILE_NAME
        metadata_path = artifact_dirpath / FSVault.ARTIFACT_METADATA_FILE_NAME

        if not data_path.exists():
            raise KeyError("no {} data: {}".format(kind.value, test_id))

        if not metadata_path.exists():
            raise KeyError("no {} metadata: {}".format(kind.value, test_id))

        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        try:
            mime_type = metadata[FSVault.MIME_TYPE_KEY]
        except KeyError as err:
            raise KeyError("No mime-type in metadata") from err

        encoding = metadata.get(FSVault.ENCODING_KEY, None)

        return Artifact(data_path, mime_type=mime_type, encoding=encoding)

    def _put(self, test_id, kind, data, mime_type, encoding):
        """Set the data for a an artifact.

        This will create any directories needed for the artifact's data.

        Args:
            test_id: The test-id of the artifact to be set.
            kind: The kind - accepted or received - of the artifact.
            data: The data for the artifact.
            mime_type: the MIME-type for the artifact's data.
            encoding: The encoding of the data (possibly `None`).
        """
        artifact_dirpath = self._artifact_dir_path(test_id, kind=kind)
        if not artifact_dirpath.exists():
            artifact_dirpath.mkdir(parents=True)

        data_path = artifact_dirpath / FSVault.DATA_FILE_NAME
        metadata_path = artifact_dirpath / FSVault.ARTIFACT_METADATA_FILE_NAME

        assert artifact_dirpath.exists()

        data_path.write_bytes(data)

        metadata = {FSVault.MIME_TYPE_KEY: mime_type, FSVault.ENCODING_KEY: encoding}
        with metadata_path.open("wt", encoding="utf-8") as handle:
            json.dump(metadata, handle)

    def _delete(self, test_id, kind):
        artifact_dirpath = self._artifact_dir_path(test_id, kind=kind)
        if artifact_dirpath.exists():
            shutil.rmtree(artifact_dirpath)
