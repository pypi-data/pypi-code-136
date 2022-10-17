"""The core approval testing algorithm.

This is where we check the latest *received* data with the latest *accepted* data.
"""


from godkjenn.artifact import Artifact


def verify(vault, comparator, test_id, data, mime_type, encoding):
    """Check if `received` matches the current accepted value for the test_id.

    If `received` doesn't match the accepted value, this will raise MismatchError§.

    Args:
        vault: A Vault instance.
        comparator: A Comparator instance.
        test_id: The ID of the test that produced `received`.
        data: The received data (bytes).
        mime_type: The mime-type of the received data.
        encoding: The encoding of the received data, if it represents encoded text.

    Raises:
        MismatchError: Received data doesn't compare as equal to the accepted data, or there
            is no accepted data.
    """
    try:
        accepted = vault.accepted(test_id)
    except KeyError:
        accepted = None
        message = "There is no accepted data"
    else:
        # If received and accepted compare as equal, we don't need to change anything.
        accepted_data = accepted.path.read_bytes()
        if comparator(accepted_data, data):
            # Clear any received data that exist from earlier.
            vault.clear_received(test_id)
            return

        message = "Received data does not match accepted"

    vault.receive(test_id, data, mime_type, encoding)
    received = vault.received(test_id)

    raise MismatchError(message, received, accepted)


class MismatchError(Exception):
    def __init__(self, message: str, received: Artifact, accepted: Artifact):
        super().__init__(message)
        self._received = received
        self._accepted = accepted

    @property
    def message(self) -> str:
        return self.args[0]

    @property
    def received(self) -> Artifact:
        "Received data (Artifact)."
        return self._received

    @property
    def accepted(self) -> Artifact:
        "Accepted data (Artifact)."
        return self._accepted
