class Graphql:
    @staticmethod
    def list() -> str:
        return """
        {
            actor {
                entitySearch(query: "domain = 'SYNTH' AND type = 'SECURE_CRED'") {
                results {
                    entities {
                    ... on SecureCredentialEntityOutline {
                        accountId
                        guid
                        name
                        tags {
                        key
                        values
                        }
                        updatedAt
                    }
                    }
                }
                }
            }
        }
        """

    @staticmethod
    def update(
        account_id: str,
        key: str,
        value: str,
        description: str,
    ) -> str:
        return """mutation {
            syntheticsUpdateSecureCredential (
                accountId: """ + account_id + """,
                description: \"""" + description + """\",
                key: \"""" + key + """\",
                value: \"""" + value + """\")  {
                createdAt
                lastUpdate
                errors {
                description
                }
            }
        }
        """

    @staticmethod
    def add(
        account_id: str,
        key: str,
        value: str,
        description: str,
    ) -> str:
        return """mutation {
            syntheticsCreateSecureCredential (
                accountId: """ + account_id + """,
                description: \"""" + description + """\",
                key: \"""" + key + """\",
                value: \"""" + value + """\") {
                errors {
                description
                }
            }
        }
        """
