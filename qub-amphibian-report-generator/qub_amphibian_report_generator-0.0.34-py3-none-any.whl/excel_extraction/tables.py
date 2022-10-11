"""# Tables module.

Functions to create sql table strings and return in loading/creation order.
"""


def get_tables_sql() -> list:
    """Generate sql string.

    Calls tables functions in order and joins them to create one large sql query string list

    Returns:
        sql_create_tables_str (list): list of strings to create all tables
    """
    tables_list = [
        order_table(),
        family_table(),
        genus_table(),
        pop_trend_table(),
        iucn_table(),
        parity_mode_table(),
        continent_table(),
        country_table(),
        geo_location_table(),
        micro_habitat_table(),
        activity_table(),
        nesting_site_table(),
        species_table(),
        nesting_site_species_table(),
        activity_species_table(),
        micro_habitat_species_table(),
        geo_location_species_table(),
        site_user_table(),
        admin_user_table(),
    ]

    return tables_list


def admin_user_table() -> str:
    """Generate admin sql string.

    Returns table based on species ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS admin_user (
        admin_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        admin_name TEXT NOT NULL,
        admin_password TEXT NOT NULL
    )
    """

    return sql_str


def site_user_table() -> str:
    """Generate site_user sql string.

    Returns table based on species ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS site_user (
      "user_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
      "first_name" varchar(200) NOT NULL,
      "last_name" varchar(200) NOT NULL,
      "educational_inst" varchar(200) NOT NULL,
      "user_name" varchar(200) NOT NULL,
      "email_address" varchar(254) NOT NULL,
      "password" varchar(200) NOT NULL
    )
    """
    return sql_str


def species_table() -> str:
    """Generate species sql string.

    Returns table based on species ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS species(
        species_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        species_name_common TEXT,
        species_name_latin TEXT,
        size_max_male REAL,
        size_max_female REAL,
        size_max_record REAL,
        longevity REAL,
        clutch_min INTEGER,
        clutch_max INTEGER,
        clutch_avg REAL,
        egg_diameter REAL,
        range_size REAL,
        elevation_min INTEGER,
        elevation_max REAL,
        elevation_avg REAL,
        img_uri_female TEXT,
        img_uri_male TEXT,
        verif_status BOOL,
        parity_mode_id INTEGER,
        pop_trend_id INTEGER,
        iucn_id INTEGER,
        genus_id INTEGER,
        FOREIGN KEY (parity_mode_id)
            REFERENCES parity_mode(parity_mode_id),
        FOREIGN KEY (pop_trend_id)
            REFERENCES pop_trend(pop_trend_id),
        FOREIGN KEY (iucn_id)
            REFERENCES iucn(iucn_id),
        FOREIGN KEY (genus_id)
            REFERENCES genus (genus_id)
    )
    """

    return sql_str


def nesting_site_species_table() -> str:
    """Generate nesting site species sql string.

    Returns table based on nesting site species ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """

    CREATE TABLE IF NOT EXISTS nesting_site_species (
        nesting_site_species_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        species_id INTEGER NOT NULL,
        nesting_site_id INTEGER NOT NULL,
        -- PRIMARY KEY (species_id, nesting_site_id),
        FOREIGN KEY (species_id)
            REFERENCES species (species_id),
        FOREIGN KEY (nesting_site_id)
            REFERENCES nesting_site (nesting_site_id)
    )

    """

    return sql_str


def nesting_site_table() -> str:
    """Generate nesting_site sql string.

    Returns table based on nesting_site ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS nesting_site(
        nesting_site_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nesting_site_desc TEXT
    )

    """

    return sql_str


def activity_species_table() -> str:
    """Generate activity_species sql string.

    Returns table based on activity_species ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS activity_species(
        activity_species_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        species_id INTEGER NOT NULL,
        activity_id INTEGER NOT NULL,
        -- PRIMARY KEY (species_id, activity_id),
        FOREIGN KEY (species_id)
            REFERENCES species (species_id),
        FOREIGN KEY (activity_id)
            REFERENCES activity (activity_id)
    )

    """

    return sql_str


def activity_table() -> str:
    """Generate activity sql string.

    Returns table based on activity ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS activity(
        activity_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        activity_kind TEXT
    )

    """

    return sql_str


def micro_habitat_species_table() -> str:
    """Generate micro_habitat_species sql string.

    Returns table based on micro_habitat_species ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS micro_habitat_species(
        micro_habitat_species_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        species_id INTEGER,
        micro_habitat_id INTEGER,
        micro_habitat_pref_rank INTEGER,
        -- PRIMARY KEY (species_id, micro_habitat_id),
        FOREIGN KEY (species_id)
            REFERENCES species (species_id),
        FOREIGN KEY (micro_habitat_id)
            REFERENCES micro_habitat (micro_habitat_id)
    )

    """

    return sql_str


def micro_habitat_table() -> str:
    """Generate micro_habitat sql string.

    Returns table based on micro_habitat ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS micro_habitat(
        micro_habitat_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        micro_habitat_name TEXT
    )

    """

    return sql_str


def geo_location_species_table() -> str:
    """Generate geo_location_species sql string.

    Returns table based on geo_location_species ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS geo_location_species(
        geo_location_species_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        geo_location_id INTEGER,
        species_id INTEGER,
        -- PRIMARY KEY (species_id, geo_location_id),
        FOREIGN KEY (species_id)
            REFERENCES species (species_id),
        FOREIGN KEY (geo_location_id)
            REFERENCES geo_location (geo_location_id)
    )

    """

    return sql_str


def geo_location_table() -> str:
    """Generate geo_location sql string.

    Returns table based on geo_location ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS geo_location(
        geo_location_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        region_name TEXT,
        latitude REAL,
        longitude REAL,
        country_id INTEGER,
        FOREIGN KEY (country_id)
            REFERENCES country (country_id)
        UNIQUE(region_name, country_id)
    )

    """

    return sql_str


def country_table() -> str:
    """Generate country sql string.

    Returns table based on country ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS country (
        country_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        country_name TEXT,
        continent_id INTEGER,
        FOREIGN KEY (continent_id)
            REFERENCES continent (continent_id)
        UNIQUE(country_name, continent_id)
    )


    """

    return sql_str


def continent_table() -> str:
    """Generate continent sql string.

    Returns table based on continent ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS continent(
        continent_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        continent_name TEXT NOT NULL
    )

    """

    return sql_str


def parity_mode_table() -> str:
    """Generate parity_mode sql string.

    Returns table based on parity_mode ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS parity_mode(
        parity_mode_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        parity_mode_desc TEXT NOT NULL
    )

    """

    return sql_str


def iucn_table() -> str:
    """Generate iucn sql string.

    Returns table based on iucn ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS iucn (
        iucn_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        iucn_status TEXT NOT NULL
    )

    """

    return sql_str


def pop_trend_table() -> str:
    """Generate pop_trend sql string.

    Returns table based on pop_trend ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS pop_trend(
        pop_trend_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        pop_trend_status TEXT NOT NULL
    )

    """

    return sql_str


def genus_table() -> str:
    """Generate genus sql string.

    Returns table based on genus ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS genus(
        genus_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        genus_name  TEXT NOT NULL,
        family_id INTEGER NOT NULL,
        FOREIGN KEY (family_id)
            REFERENCES family (family_id)
    )

    """

    return sql_str


def family_table() -> str:
    """Generate family sql string.

    Returns table based on family ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS family(
        family_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        family_name TEXT NOT NULL,
        order_id INTEGER NOT NULL,
        FOREIGN KEY (order_id)
            REFERENCES order_taxon (order_id)

    )

    """

    return sql_str


def order_table() -> str:
    """Generate order sql string.

    Returns table based on order ERD diagram

    Returns:
        sql_str: returns string of sql code
    """
    sql_str = """
    CREATE TABLE IF NOT EXISTS order_taxon(
        order_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        order_taxon_name TEXT NOT NULL
    )

    """

    return sql_str
