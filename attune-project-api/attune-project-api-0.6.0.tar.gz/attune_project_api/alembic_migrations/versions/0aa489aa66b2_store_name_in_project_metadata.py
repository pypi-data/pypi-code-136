"""Store name in project metadata

Revision ID: 0aa489aa66b2
Revises: 58b1656aac40
Create Date: 2022-06-27 13:56:12.316172

"""

# revision identifiers, used by Alembic.
from attune_project_api import ObjectStorageContext

revision = "0aa489aa66b2"
down_revision = "58b1656aac40"
branch_labels = None
depends_on = None


def upgrade(storageContext: ObjectStorageContext):
    metadata = storageContext.metadata
    projectInfo = storageContext.project

    metadata["name"] = projectInfo.name
    storageContext.writeMetadata(metadata)
    storageContext.commit("Store project name in metadata.json")


def downgrade(storageContext: ObjectStorageContext):
    pass
