max_tags = 5  # Maximum number of tags.


class Properties:
    """A class for storing and retrieving properties."""

    def __init__(self):
        self.properties = {}

    def get_properties(self):
        """Method to retrieve the properties.

        Returns:
            :obj:`dict`: The dictionary of current properties.

        """

        return self.properties

    def update_properties(self, properties):
        """Method to update the properties.

        Args:
            ``properties`` (:obj:`dict`):  A dictionary of properties.
            New properties are added.  Old properties are updated.  The
            keys for the dictionary entries are `name` and up to five
            optional tags labeled `tag1`, `tag2`, ..., `tag5`.

        Returns:
            On successful return, the properties have been updated.

        """

        for prop in properties:
            if isinstance(prop, tuple):
                assert len(prop) <= max_tags + 1

        self.properties = {**self.properties, **properties}
