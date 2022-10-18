
"""
>>> create initial tables <<<

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

Revision ID: f989260ff4b2
Revises:
Create Date: 2022-04-21 19:19:35.189301
"""


from typing import Tuple

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.sql import text

# revision identifiers, used by Alembic
revision = 'f989260ff4b2'
down_revision = None
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


def create_company_table() -> None:
    op.create_table(
        "company",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("company_id", sa.BigInteger, sa.ForeignKey("company.id", ondelete="CASCADE")),
        sa.Column("active", sa.Boolean, server_default="True"),
        sa.Column("company_name", sa.VARCHAR(100), nullable=False),
        sa.Column("office", sa.VARCHAR(40), nullable=False),
        sa.Column("relationship", sa.VARCHAR(20)),
        sa.Column("logo_file", sa.VARCHAR(40)),
        *timestamps(),
        sa.schema.UniqueConstraint('company_name', 'office', name='company_uc_1')
    )
    op.create_index(
        'co_company_id_idx',
        'company',
        ['company_id'],
        postgresql_where=text("company.company_id != Null")
    )
    op.execute(
        """
        CREATE TRIGGER update_company_modtime
            BEFORE UPDATE
            ON company
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_referral_code_lookup_table() -> None:
    op.create_table(
        "referral_code_lookup",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("employee_id", sa.BigInteger, nullable=False),
        sa.Column("referral_code", sa.VARCHAR(30), nullable=False, unique=True),
        sa.Column("code_type", sa.Enum('b2b', 'promo', 'tradeshow', 'vip', name="code_type_enum"), nullable=False),
        sa.Column("discount", sa.Float),
        sa.Column("note", sa.Text),
        *timestamps()
    )
    op.execute(
        """
        CREATE TRIGGER update_ref_code_lu_modtime
            BEFORE UPDATE
            ON referral_code_lookup
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_referral_code_table() -> None:
    op.create_table(
        "referral_code",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("person_id", sa.BigInteger, nullable=False),
        sa.Column(
            "referral_code",
            sa.VARCHAR(30),
            sa.ForeignKey("referral_code_lookup.referral_code", ondelete="RESTRICT"),
        ),
        sa.Column("redeemed", sa.Boolean, server_default="True"),
        *timestamps()
    )
    op.execute(
        """
        CREATE TRIGGER update_ref_code_modtime
            BEFORE UPDATE
            ON referral_code
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_person_table() -> None:
    op.create_table(
        "person",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("active", sa.Boolean, server_default="True"),
        sa.Column("employee", sa.Boolean, server_default="False"),
        sa.Column("app_role", sa.Integer, nullable=False, server_default=text("0")),
        sa.Column("name_prefix", sa.VARCHAR(8)),
        sa.Column("name_first", sa.VARCHAR(30)),
        sa.Column("name_last", sa.VARCHAR(30)),
        sa.Column("name_suffix", sa.VARCHAR(8)),
        sa.Column("dob", sa.Date),
        sa.Column("occupation", sa.VARCHAR(50)),
        sa.Column("title", sa.VARCHAR(30)),
        sa.Column("company_id", sa.BigInteger, sa.ForeignKey("company.id", ondelete="SET NULL"), index=True),
        sa.Column("image_file", sa.VARCHAR(40)),
        sa.Column("bio", sa.Text),
        sa.Column("password", sa.Text),
        sa.Column("salt", sa.Text),
        sa.Column("verified_date", sa.TIMESTAMP(timezone=True)),
        sa.Column("change_pw", sa.Boolean, server_default="False"),
        sa.Column("temp_pw_used", sa.Boolean, server_default="True"),
        *timestamps()
    )
    op.create_check_constraint(
        "person_ck_names",
        "person",
        "name_first is not null or name_last is not null",
    )
    op.execute(
        """
        CREATE TRIGGER update_person_modtime
            BEFORE UPDATE
            ON person
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_rcl_person_fk():
    op.create_foreign_key("rcl_person_fk", "referral_code_lookup", "person", ["employee_id"], ["id"])


def create_rc_person_fk():
    op.create_foreign_key("rc_person_fk", "referral_code", "person", ["person_id"], ["id"])


def create_zip_lookup_table() -> None:
    op.create_table(
        "zip_lookup",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("country_code", sa.VARCHAR(2)),
        sa.Column("zip_code", sa.VARCHAR(5), unique=True),
        sa.Column("place_name", sa.VARCHAR(180)),
        sa.Column("state", sa.VARCHAR(100)),
        sa.Column("state_ab", sa.VARCHAR(2)),
        sa.Column("county", sa.VARCHAR(50)),
        sa.Column("locality_code", sa.VARCHAR(5)),
        sa.Column("latitude", DOUBLE_PRECISION(asdecimal=True)),
        sa.Column("longitude", DOUBLE_PRECISION(asdecimal=True)),
        sa.Column("accuracy", sa.Integer),
    )
    op.execute(
        """
        CREATE TRIGGER update_zip_lookup_modtime
            BEFORE UPDATE
            ON zip_lookup
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_address_table() -> None:
    op.create_table(
        "address",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("company_id", sa.BigInteger, sa.ForeignKey("company.id", ondelete="CASCADE")),
        sa.Column("person_id", sa.BigInteger, sa.ForeignKey("person.id", ondelete="CASCADE")),
        sa.Column("addr_label", sa.VARCHAR(20), nullable=False),
        sa.Column("addr_primary", sa.Boolean, server_default="False"),
        sa.Column("addr_bill_to", sa.Boolean, server_default="False"),
        sa.Column("addr_ship_to", sa.Boolean, server_default="False"),
        sa.Column("addr1", sa.VARCHAR(100)),
        sa.Column("addr2", sa.VARCHAR(100)),
        sa.Column("city", sa.VARCHAR(50)),
        sa.Column("state", sa.VARCHAR(2)),
        sa.Column("zip_code", sa.VARCHAR(5), sa.ForeignKey("zip_lookup.zip_code", ondelete="SET NULL")),
        *timestamps(),
        sa.UniqueConstraint('person_id', 'addr1', name='uix_person_addr1'),
        sa.UniqueConstraint('company_id', 'addr1', name='uix_company_addr1')
    )
    op.create_check_constraint(
        "addr_ck_foreign_keys",
        "address",
        "((company_id is not null)::integer + (person_id is not null)::integer) = 1"
    )
    op.create_index(
        'addr_company_id_idx',
        'address',
        ['company_id'],
        postgresql_where=text("address.company_id != Null")
    )
    op.create_index(
        'addr_person_id_idx',
        'address',
        ['person_id'],
        postgresql_where=text("address.person_id != Null")
    )
    op.execute(
        """
        CREATE TRIGGER update_address_modtime
            BEFORE UPDATE
            ON address
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_email_address_table() -> None:
    """
    We've set up the UniqueConstraint on email address in such a way that it MUST be unique for
    a person or a company.  However, multiple people (or companies) may have the same email address.
    This is a somewhat odd circumstance, but not out of the realm of validity.
    """
    op.create_table(
        "email_address",
        sa.Column("id", sa.BigInteger, nullable=False, unique=True, primary_key=True),
        sa.Column("company_id", sa.BigInteger, sa.ForeignKey("company.id", ondelete="CASCADE")),
        sa.Column("person_id", sa.BigInteger, sa.ForeignKey("person.id", ondelete="CASCADE")),
        sa.Column("email_label", sa.VARCHAR(12)),
        sa.Column("email", sa.Text),
        sa.Column("verified", sa.Boolean, server_default="False"),
        sa.Column("email_primary", sa.Boolean, server_default="False"),
        sa.Column("email_login", sa.Boolean, server_default="False"),
        *timestamps(),
        sa.UniqueConstraint('person_id', 'email', name='uix_person_email'),
        sa.UniqueConstraint('company_id', 'email', name='uix_company_email')
    )
    op.create_check_constraint(
        "email_addr_ck_foreign_keys",
        "email_address",
        "((company_id is not null)::integer + (person_id is not null)::integer) = 1"
    )
    op.create_index(
        'email_addr_company_id_idx',
        'email_address',
        ['company_id'],
        postgresql_where=text("email_address.company_id != Null")
    )
    op.create_index(
        'email_addr_person_id_idx',
        'email_address',
        ['person_id'],
        postgresql_where=text("email_address.person_id != Null")
    )
    op.execute(
        """
        CREATE TRIGGER update_email_address_modtime
            BEFORE UPDATE
            ON email_address
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def upgrade() -> None:
    create_updated_at_trigger()
    create_company_table()
    create_referral_code_lookup_table()
    create_referral_code_table()
    create_person_table()
    create_rcl_person_fk()
    create_rc_person_fk()
    create_zip_lookup_table()
    create_address_table()
    create_email_address_table()


def downgrade() -> None:
    op.drop_table("email_address")
    op.drop_table("address")
    op.drop_table("zip_lookup")
    op.drop_constraint("rcl_person_fk", "referral_code_lookup")
    op.drop_constraint("rc_person_fk", "referral_code")
    op.drop_table("person")
    op.drop_table("referral_code")
    op.drop_table("referral_code_lookup")
    op.drop_table("company")
    op.execute("DROP TYPE code_type_enum")
    op.execute("DROP FUNCTION update_updated_at_column")
