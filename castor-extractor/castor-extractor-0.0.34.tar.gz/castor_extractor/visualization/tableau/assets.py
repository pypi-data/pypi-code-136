from enum import Enum
from typing import Dict


class TableauAsset(Enum):
    """
    Tableau assets
    """

    WORKBOOK = "workbooks"
    USER = "users"
    PROJECT = "projects"
    USAGE = "views"
    WORKBOOK_TO_DATASOURCE = "workbooks_to_datasource"
    DATASOURCE = "datasources"
    CUSTOM_SQL_TABLE = "custom_sql_tables"
    CUSTOM_SQL_QUERY = "custom_sql_queries"


EXPORTED_FIELDS = {
    TableauAsset.WORKBOOK: (
        "id",
        "name",
        "description",
        "tags",
        "project_id",
        "created_at",
        "updated_at",
        "owner_id",
        "webpage_url",
    ),
    TableauAsset.PROJECT: (
        "id",
        "name",
        "description",
        "parent_id",
    ),
    TableauAsset.USER: (
        "id",
        "name",
        "email",
        "fullname",
        "site_role",
    ),
    TableauAsset.USAGE: (
        "workbook_id",
        "total_views",
    ),
}


class TableauGraphqlAsset(Enum):
    """
    Assets which can be fetched from Tableau
    """

    WORKBOOK_TO_DATASOURCE = "workbooks"
    DATASOURCE = "datasources"
    CUSTOM_SQL = "customSQLTables"

    """
    Fields which will be use for Tableau GraphQL API
    """

    FIELDS_WORKBOOK_TO_DATASOURCE = """
        luid
        id
        embeddedDatasources {
            id
            name
        }
    """

    FIELDS_DATASOURCE = """
        id
        name
        hasExtracts
        upstreamTables {
            id
            schema
            name
            fullName
            database {
                id
                name
                connectionType
            }
        }
    """

    FIELDS_CUSTOM_SQL_TABLE = """
        id
        name
        columns {
            referencedByFields {
                datasource {
                    ... on PublishedDatasource {
                        id
                    }

                    ... on EmbeddedDatasource {
                        id
                    }
                }
            }
        }
        """

    FIELDS_CUSTOM_SQL_QUERY = """
        id
        name
        query
        database {
            name
            connectionType
        }
        tables {
            name
        }
    """


QUERY_FIELDS: Dict[TableauAsset, Dict[str, TableauGraphqlAsset]] = {
    TableauAsset.WORKBOOK_TO_DATASOURCE: {
        "object_type": TableauGraphqlAsset.WORKBOOK_TO_DATASOURCE,
        "fields": TableauGraphqlAsset.FIELDS_WORKBOOK_TO_DATASOURCE,
    },
    TableauAsset.DATASOURCE: {
        "object_type": TableauGraphqlAsset.DATASOURCE,
        "fields": TableauGraphqlAsset.FIELDS_DATASOURCE,
    },
    TableauAsset.CUSTOM_SQL_TABLE: {
        "object_type": TableauGraphqlAsset.CUSTOM_SQL,
        "fields": TableauGraphqlAsset.FIELDS_CUSTOM_SQL_TABLE,
    },
    TableauAsset.CUSTOM_SQL_QUERY: {
        "object_type": TableauGraphqlAsset.CUSTOM_SQL,
        "fields": TableauGraphqlAsset.FIELDS_CUSTOM_SQL_QUERY,
    },
}
