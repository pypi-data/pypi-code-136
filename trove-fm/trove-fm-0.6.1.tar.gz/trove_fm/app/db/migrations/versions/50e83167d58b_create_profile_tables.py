
"""
>>> create profile tables <<<

TroveFM is an online store and headless CMS.

Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com


Revision ID: 50e83167d58b
Revises: 8c3423000743
Create Date: 2022-05-19 11:06:46.315800
"""


from typing import Tuple

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, text


# revision identifiers, used by Alembic
revision = '50e83167d58b'
down_revision = '8c3423000743'
branch_labels = None
depends_on = None


def create_updated_at_trigger() -> None:
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
            RETURNS TRIGGER AS
        $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        """
    )


def timestamps(indexed: bool = False) -> Tuple[sa.Column, sa.Column]:
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=indexed,
        ),
    )


def create_platform_lookup_table() -> None:
    op.create_table(
        "platform_lookup",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("platform", sa.VARCHAR(30), nullable=False, unique=True),
        sa.Column("url", sa.VARCHAR(40), nullable=False, unique=True),
    )


def create_platform_table() -> None:
    op.create_table(
        "platform",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("platform_id", sa.BigInteger, sa.ForeignKey("platform_lookup.id", ondelete="RESTRICT")),
        sa.Column("company_id", sa.BigInteger, sa.ForeignKey("company.id", ondelete="CASCADE")),
        sa.Column("person_id", sa.BigInteger, sa.ForeignKey("person.id", ondelete="CASCADE")),
        sa.Column("handle", sa.VARCHAR(30), unique=True),
        sa.schema.UniqueConstraint('platform_id', 'handle', name='platform_uc_1')
    )
    op.create_check_constraint(
        "pltfm_ck_foreign_keys",
        "platform",
        "((company_id is not null)::integer + (person_id is not null)::integer) = 1"
    )
    op.create_index(
        'pltfm_company_id_idx',
        'platform',
        ['company_id'],
        postgresql_where=text("platform.company_id != Null")
    )
    op.create_index(
        'pltfm_person_id_idx',
        'platform',
        ['person_id'],
        postgresql_where=text("platform.person_id != Null")
    )


def create_phone_table() -> None:
    """
    Store phone numbers in E.164 format.

    See: https://en.wikipedia.org/wiki/E.164
    """
    op.create_table(
        "phone",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("company_id", sa.BigInteger, sa.ForeignKey("company.id", ondelete="CASCADE")),
        sa.Column("person_id", sa.BigInteger, sa.ForeignKey("person.id", ondelete="CASCADE")),
        sa.Column("phone_label", sa.VARCHAR(12), nullable=False),
        sa.Column("phone_number", sa.VARCHAR(15), nullable=False),
        sa.Column("phone_primary", sa.Boolean, server_default="False"),
        *timestamps(),
        sa.UniqueConstraint('person_id', 'phone_number', name='uix_person_phone_number'),
        sa.UniqueConstraint('company_id', 'phone_number', name='uix_company_phone_number')
    )
    op.create_check_constraint(
        "phone_ck_foreign_keys",
        "phone",
        "((company_id is not null)::integer + (person_id is not null)::integer) = 1"
    )
    op.create_index(
        'phone_company_id_idx',
        'phone',
        ['company_id'],
        postgresql_where=text("phone.company_id != Null")
    )
    op.create_index(
        'phone_person_id_idx',
        'phone',
        ['person_id'],
        postgresql_where=text("phone.person_id != Null")
    )
    op.execute(
        """
        CREATE TRIGGER update_phone_modtime
            BEFORE UPDATE
            ON phone
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


platform_lookup = table(
    'platform_lookup',
    sa.Column("platform", sa.VARCHAR(30), nullable=False, unique=True),
    sa.Column("url", sa.VARCHAR(40), nullable=False, unique=True)
)


def add_platform_lookup_data():
    op.bulk_insert(
        platform_lookup,
        [
            {'platform': 'Apple Music', 'url': 'https://music.apple.com/'},
            {'platform': 'Caffeine', 'url': 'https://www.caffeine.tv/'},
            {'platform': 'Chess.com', 'url': 'https://www.chess.com/'},
            {'platform': 'Diaspora*', 'url': 'https://diasporafoundation.org/'},
            {'platform': 'Elpha', 'url': 'https://elpha.com/'},
            {'platform': 'Facebook', 'url': 'https://www.facebook.com/'},
            {'platform': 'Flickr', 'url': 'https://www.flickr.com/'},
            {'platform': 'Growbud', 'url': 'https://growbud.co/'},
            {'platform': 'GrowersNetwork', 'url': 'https://growersnetwork.org/'},
            {'platform': 'Instagram', 'url': 'https://www.instagram.com/'},
            {'platform': 'LinkedIn', 'url': 'https://www.linkedin.com/'},
            {'platform': 'Medium', 'url': 'https://medium.com/'},
            {'platform': 'Meetup', 'url': 'https://www.meetup.com/'},
            {'platform': 'Nextdoor', 'url': 'https://nextdoor.com/'},
            {'platform': 'Pandora', 'url': 'https://www.pandora.com/'},
            {'platform': 'Pinterest', 'url': 'https://www.pinterest.com/'},
            {'platform': 'Quora', 'url': 'https://www.quora.com/'},
            {'platform': 'Reddit', 'url': 'https://www.reddit.com/'},
            {'platform': 'Snapchat', 'url': 'https://www.snapchat.com/'},
            {'platform': 'SoundCloud', 'url': 'https://soundcloud.com/'},
            {'platform': 'Spotify', 'url': 'https://www.spotify.com/'},
            {'platform': 'Substack', 'url': 'https://substack.com/'},
            {'platform': 'TikTok', 'url': 'https://www.tiktok.com/'},
            {'platform': 'Tumblr', 'url': 'https://www.tumblr.com/'},
            {'platform': 'Twitch', 'url': 'https://www.twitch.tv/'},
            {'platform': 'Twitter', 'url': 'https://twitter.com/'},
            {'platform': 'Vimeo', 'url': 'https://vimeo.com/'},
            {'platform': 'Webex', 'url': 'https://www.webex.com/'},
            {'platform': 'WhatsApp', 'url': 'https://www.whatsapp.com/'},
            {'platform': 'Xbox', 'url': 'https://www.xbox.com/'},
            {'platform': 'Yelp', 'url': 'https://www.yelp.com/'},
            {'platform': 'YouTube', 'url': 'https://www.youtube.com/'},
            {'platform': 'Zoom', 'url': 'https://zoom.us/'}
        ]
    )


def create_url_table() -> None:
    op.create_table(
        "url",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("company_id", sa.BigInteger, sa.ForeignKey("company.id", ondelete="CASCADE")),
        sa.Column("person_id", sa.BigInteger, sa.ForeignKey("person.id", ondelete="CASCADE")),
        sa.Column("url_label", sa.VARCHAR(30), nullable=False),
        sa.Column("url", sa.VARCHAR(120), nullable=False, index=True),
        sa.Column("display_name", sa.VARCHAR(30)),
        sa.Column("description", sa.Text),
    )
    op.create_check_constraint(
        "url_ck_foreign_keys",
        "url",
        "((company_id is not null)::integer + (person_id is not null)::integer) = 1"
    )
    op.create_index(
        'url_company_id_idx',
        'url',
        ['company_id'],
        postgresql_where=text("url.company_id != Null")
    )
    op.create_index(
        'url_person_id_idx',
        'url',
        ['person_id'],
        postgresql_where=text("url.person_id != Null")
    )


def upgrade() -> None:
    create_platform_lookup_table()
    create_platform_table()
    create_phone_table()
    add_platform_lookup_data()
    create_url_table()


def downgrade() -> None:
    op.drop_table("url")
    op.drop_table("phone")
    op.drop_table("platform")
    op.drop_table("platform_lookup")
