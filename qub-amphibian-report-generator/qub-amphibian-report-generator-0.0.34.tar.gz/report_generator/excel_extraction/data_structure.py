"""# Data Structure.

Functions to structure data from dataset to fit into sql tables schema.

"""

# stand lib imports

# pip package imports
import pandas
from loguru import logger

# other imports


def structure_data(data_frame: pandas.DataFrame) -> dict:
    """Structures data_frame.

    Args:
        data_frame(pandas.DataFrame): Pandas DataFrame object
    Returns:
        tables_object(dict): Dict containing structured Pandas DataFrames
    """
    logger.info("Structuring data start")
    order = structure_order(data_frame)
    family = structure_family(data_frame, order)
    genus = structure_genus(data_frame, family)
    pop_trend = structure_pop_trend(data_frame)
    iucn = structure_iucn(data_frame)
    parity_mode = structure_parity_mode(data_frame)
    micro_habitat = structure_micro_habitat(data_frame)
    activity = structure_activity(data_frame)
    nesting_site = structure_nesting_site(data_frame)
    species = structure_species(data_frame, genus, parity_mode, iucn, pop_trend)
    nesting_site_species = structure_nesting_site_species(
        data_frame, species, nesting_site
    )
    activity_species = structure_activity_species(data_frame, species, activity)
    micro_habitat_species = structure_micro_habitat_species(
        data_frame, species, micro_habitat
    )
    continent, country, geo_location, geo_location_species = structure_geo_location(
        data_frame, species, genus
    )
    species.drop("sg", axis=1, inplace=True)

    tables_object = {
        "order_taxon": order,
        "family": family,
        "genus": genus,
        "pop_trend": pop_trend,
        "iucn": iucn,
        "parity_mode": parity_mode,
        "micro_habitat": micro_habitat,
        "activity": activity,
        "nesting_site": nesting_site,
        "species": species,
        "nesting_site_species": nesting_site_species,
        "activity_species": activity_species,
        "micro_habitat_species": micro_habitat_species,
        "continent": continent,
        "country": country,
        "geo_location": geo_location,
        "geo_location_species": geo_location_species,
    }
    logger.info("Structuring Data End")
    return tables_object


def structure_order(data_frame: pandas.DataFrame) -> object:
    """Structures data for Order table.

    Args:
        data_frame (pandas.DataFrame):  Pandas DataFrame object
    Returns:
        order_data_frame (pandas.DataFrame):    Pandas DataFrame object with order data
    """
    logger.debug("Order")
    order = data_frame["Order"].dropna().unique()
    df = pandas.DataFrame(order, columns=["order_taxon_name"])
    return df


def structure_family(
    data_frame: pandas.DataFrame, order: pandas.DataFrame
) -> pandas.DataFrame:
    """Structures data for Family table.

    Args:
        data_frame (pandas.DataFrame):        Dataset DataFrame
        order (pandas.DataFrame):             Order Dataframe
    Returns:
        family_data_frame (pandas.DataFrame): Pandas DataFrame object with Family data
    """
    logger.debug("Family")
    fam = data_frame[["Order", "Family"]]
    fam["Ind"] = fam["Order"].map(
        lambda x: str(order.index[order["order_taxon_name"] == x].tolist()[0] + 1)
    )

    fam["OrderFam"] = fam["Family"] + "+" + fam["Ind"]
    uni = [x.split("+") for x in fam["OrderFam"].dropna().unique()]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"family_name": a, "order_id": b})

    return df


def structure_genus(
    data_frame: pandas.DataFrame, family: pandas.DataFrame
) -> pandas.DataFrame:
    """Structures data for Genus table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
        family (pandas.DataFrame): Pandas DataFrame object
    Returns:
        genus_data_frame (pandas.DataFrame): Pandas DataFrame object with Genus data
    """
    logger.debug("Genus")

    genus = data_frame[["Family", "Genus"]]
    genus["Ind"] = genus["Family"].map(
        lambda x: str(family.index[family["family_name"] == x].tolist()[0] + 1)
    )

    genus["GenFam"] = genus["Genus"] + "+" + genus["Ind"]
    uni = [x.split("+") for x in genus["GenFam"].dropna().unique()]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"genus_name": a, "family_id": b})

    return df


def structure_pop_trend(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    """Structures data for pop_trend table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
    Returns:
        pop_trend_frame (pandas.DataFrame):Pandas DataFrame object with pop_trend data
    """
    logger.debug("PopTrend")

    pop_trend = data_frame["PopTrend"].dropna().unique()
    df = pandas.DataFrame(pop_trend, columns=["pop_trend_status"])
    return df


def structure_iucn(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    """Structures data for IUCN table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
    Returns:
        IUCN_frame (pandas.DataFrame): Pandas DataFrame object with IUCN data
    """
    logger.debug("IUCN")

    iucn = data_frame["IUCN"].dropna().unique()
    df = pandas.DataFrame(iucn, columns=["iucn_status"])
    return df


def structure_parity_mode(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    """Structures data for Parity table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
    Returns:
        IUCN_frame (pandas.DataFrame):Pandas DataFrame object with Parity data
    """
    logger.debug("Parity")

    parity_mode = data_frame["ParityMode"].dropna().unique()
    df = pandas.DataFrame(parity_mode, columns=["parity_mode_desc"])
    return df


def structure_continent(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    """Structures data for Continent table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
    Returns:
        Continent_frame (pandas.DataFrame):Pandas DataFrame object with Continent data
    """


def structure_country(
    data_frame: pandas.DataFrame, continent: pandas.DataFrame
) -> pandas.DataFrame:
    """Structures data for Country table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
        continent (pandas.DataFrame): Pandas DataFrame object

    Returns:
        Country_frame (pandas.DataFrame):Pandas DataFrame object with Country data
    """


def structure_geo_location(
    data_frame: pandas.DataFrame,
    species_df: pandas.DataFrame,
    genus_df: pandas.DataFrame,
) -> pandas.DataFrame:
    """Structures data for geo_location table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
        species (pandas.DataFrame): Pandas DataFrame object

    Returns:
        geo_location_frame (pandas.DataFrame):Pandas DataFrame object with geo_location data
    """
    logger.debug("Geo Location")

    # geo dataframe
    geolocation = data_frame[["Species", "Genus", "FormattedGeographicRegion"]]
    geolocation["spec_gen"] = geolocation["Species"] + " " + geolocation["Genus"]

    geolocation["SpecInd"] = geolocation["Species"].map(
        lambda x: str(
            species_df.index[species_df["species_name_latin"] == x].tolist()[0] + 1
        )
    )

    logger.debug("Geolocation Split Lines")
    # process lines
    results = []
    for row in geolocation.iterrows():
        vals = []
        for value in row:
            if isinstance(value, int):
                vals.append(value)
            else:
                vals = [*vals, *value.values]

        locations_strs = vals[3].split("/")
        spec_gen = vals[4]

        for location_str in locations_strs:
            parts = location_str.split("_")
            results.append([spec_gen, *parts])

    species_id = []
    continent = []
    country = []
    region = []
    latitude = []
    longitude = []
    country_code = []

    # print(results)
    species_df["sg"] = species_df["species_name_latin"] + species_df["genus_id"]

    logger.debug("Geolocation: Lines to new dataframe")
    for x in results:
        spec = x[0].split(" ")[0]
        gen = x[0].split(" ")[1]
        gen_id = genus_df.index[genus_df["genus_name"] == gen].tolist()[0] + 1
        sgval = spec + str(gen_id)
        spec_id = species_df.index[species_df["sg"] == sgval].tolist()[0] + 1
        species_id.append(spec_id)
        continent.append(x[1])
        country.append(x[2])
        region.append(x[3])
        latitude.append(x[4])
        longitude.append(x[5])
        country_code.append(x[6])

    # new base dataframe
    df = pandas.DataFrame(
        {
            "species_id": species_id,
            "continent": continent,
            "country": country,
            "region": region,
            "latitude": latitude,
            "longitude": longitude,
            "country_code": country_code,
        }
    )

    logger.debug("create continent")
    # continent dataframe
    continent_sp = df["continent"].dropna().unique()
    continent_df = pandas.DataFrame(continent_sp, columns=["continent_name"])

    df["continent_id"] = df["continent"].map(
        lambda x: continent_df.index[continent_df["continent_name"] == x].tolist()[0]
        + 1
    )

    country_df = df[["country", "continent_id"]].drop_duplicates(ignore_index=True)
    df["country_cont"] = df.agg(lambda x: f"{x['country']} {x['continent_id']}", axis=1)
    country_df["country_cont"] = country_df.agg(
        lambda x: f"{x['country']} {x['continent_id']}", axis=1
    )

    df["country_id"] = df["country_cont"].map(
        lambda x: country_df.index[country_df["country_cont"] == x].tolist()[0] + 1
    )

    # geo_location
    logger.debug("create geolocation")
    geo_sp = df[["region", "latitude", "longitude", "country_id"]].drop_duplicates(
        ignore_index=True
    )

    df["reg_count"] = df.agg(lambda x: f"{x['country_id']} {x['region']}", axis=1)
    geo_sp["reg_count"] = geo_sp.agg(
        lambda x: f"{x['country_id']} {x['region']}", axis=1
    )

    df["geo_location_id"] = df["reg_count"].map(
        lambda x: geo_sp.index[geo_sp["reg_count"] == x].tolist()[0] + 1
    )

    geolocation_species = df[
        [
            "geo_location_id",
            "species_id",
        ]
    ].drop_duplicates()
    continent = continent_df.rename(columns={"continent": "continent_name"})
    country = country_df[["country", "continent_id"]].rename(
        columns={"country": "country_name"}
    )
    geolocation = geo_sp[["region", "latitude", "longitude", "country_id"]].rename(
        columns={"region": "region_name"}
    )

    return [continent, country, geolocation, geolocation_species]


def structure_geo_location_species(
    data_frame: pandas.DataFrame,
    geo_location: pandas.DataFrame,
    country_df,
    continent_df,
) -> pandas.DataFrame:
    """Structures data for geo_location table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
        species (pandas.DataFrame): Pandas DataFrame object

    Returns:
        geo_location_frame (pandas.DataFrame) :Pandas DataFrame object with geo_location data
    """


def structure_micro_habitat(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    """Structures data for micro_habitat table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object

    Returns:
        micro_habitat_frame (pandas.DataFrame): Pandas DataFrame object with micro_habitat data
    """
    logger.debug("Habitat")

    micro = data_frame["Microhabitat"].dropna().unique()
    df = pandas.DataFrame(micro, columns=["micro_habitat_name"])
    return df


def structure_activity(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    """Structures data for activity table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object

    Returns:
        activity_frame (pandas.DataFrame): Pandas DataFrame object with activity data
    """
    logger.debug("Activity")

    activity = data_frame["Activity"].dropna().unique()
    df = pandas.DataFrame(activity, columns=["activity_kind"])
    return df


def structure_nesting_site(data_frame: pandas.DataFrame) -> pandas.DataFrame:
    """Structures data for nesting_site table.

    Args:
        data_frame(pandas.DataFrame): Pandas DataFrame object

    Returns:
        nesting_site_frame(pandas.DataFrame):Pandas DataFrame object with nesting_site data
    """
    logger.debug("Nesting")

    nesting_site = data_frame["NestingSite"].dropna().unique()
    df = pandas.DataFrame(nesting_site, columns=["nesting_site_desc"])
    return df


def structure_species(
    data_frame: pandas.DataFrame,
    genus: pandas.DataFrame,
    parity_mode: pandas.DataFrame,
    iucn: pandas.DataFrame,
    pop_trend: pandas.DataFrame,
) -> pandas.DataFrame:
    """Structures data for species table.

    Args:
        data_frame (pandas.DataFrame): Pandas DataFrame object
        genus (pandas.DataFrame): Pandas DataFrame object
        parity_mode (pandas.DataFrame): Pandas DataFrame object
        iucn (pandas.DataFrame): Pandas DataFrame object
        pop_trend (pandas.DataFrame): Pandas DataFrame object

    Returns:
        species_frame (pandas.DataFrame): Pandas DataFrame object with species data
    """
    logger.debug("Struct Spec")

    species = data_frame[
        [
            "Species",
            "SVLMMx",
            "SVLFMx",
            "SVLMx",
            "Longevity",
            "ClutchMin",
            "ClutchMax",
            "Clutch",
            "EggDiameter",
            "RangeSize",
            "ElevationMin",
            "ElevationMax",
            "Elevation",
            "ParityMode",
            "PopTrend",
            "IUCN",
            "Genus",
        ]
    ]

    species["Genus"] = species["Genus"].map(
        lambda x: str(genus.index[genus["genus_name"] == x].tolist()[0] + 1)
        if x != ""
        else x
    )

    def iucn_check(x):
        return (
            str(iucn.index[iucn["iucn_status"] == x].tolist()[0] + 1)
            if x is not None
            else x
        )

    species["IUCN"] = species["IUCN"].map(lambda x: iucn_check(x))

    species["PopTrend"] = species["PopTrend"].map(
        lambda x: str(
            pop_trend.index[pop_trend["pop_trend_status"] == x].tolist()[0] + 1
        )
        if x is not None
        else x
    )

    species["ParityMode"] = species["ParityMode"].map(
        lambda x: str(
            parity_mode.index[parity_mode["parity_mode_desc"] == x].tolist()[0] + 1
        )
        if x is not None
        else x
    )

    species.insert(13, "img_url_female", "")
    species.insert(14, "img_url_male", "")
    species.insert(15, "verif_status", True)

    species.columns = [
        "species_name_latin",
        "size_max_male",
        "size_max_female",
        "size_max_record",
        "longevity",
        "clutch_min",
        "clutch_max",
        "clutch_avg",
        "egg_diameter",
        "range_size",
        "elevation_min",
        "elevation_max",
        "elevation_avg",
        "img_uri_female",
        "img_uri_male",
        "verif_status",
        "parity_mode_id",
        "pop_trend_id",
        "iucn_id",
        "genus_id",
    ]

    return species


def structure_micro_habitat_species(
    data_frame: object, species: object, micro_habitat: object
) -> object:
    """Structures data for micro_habitiat_species table.

    Args:
        data_frame(object): Pandas DataFrame object
        species(object): Pandas DataFrame object
        micro_habitat(object): Pandas DataFrame object

    Returns:
        micro_habitat_species_frame(object):Pandas DataFrame object with m_h_s data
    """
    logger.debug("hab spec")

    micro_habitat_species = data_frame[["Species", "Microhabitat"]]
    micro_habitat_species["species_index"] = micro_habitat_species["Species"].map(
        lambda x: str(species.index[species["species_name_latin"] == x].tolist()[0] + 1)
    )

    def hab(x):
        b = (
            micro_habitat.index[micro_habitat["micro_habitat_name"] == x].tolist()
            if x is not None or x != "nan"
            else x
        )
        if len(b) > 0:
            a = str(b[0] + 1)
        else:
            a = None
        return a

    micro_habitat_species["habitat_index"] = micro_habitat_species["Microhabitat"].map(
        lambda x: hab(x)
    )

    micro_habitat_species["spec_ind_hab_ind"] = (
        micro_habitat_species["species_index"]
        + "+"
        + micro_habitat_species["habitat_index"].dropna()
    )

    uni = [
        x.split("+")
        for x in micro_habitat_species["spec_ind_hab_ind"].dropna().unique()
    ]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"species_id": a, "micro_habitat_id": b})

    return df


def structure_nesting_site_species(
    data_frame: object, species: object, nesting_site: object
) -> object:
    """Structures data for nesting_site_species table.

    Args:
        data_frame(object): Pandas DataFrame object
        species(object): Pandas DataFrame object
        nesting_site(object): Pandas DataFrame object

    Returns:
        nesting_site_species_frame(object):Pandas DataFrame object with data
    """
    logger.debug("nest spec")

    nesting_site_species = data_frame[["Species", "NestingSite"]]

    nesting_site_species["species_index"] = nesting_site_species["Species"].map(
        lambda x: str(species.index[species["species_name_latin"] == x].tolist()[0] + 1)
    )

    nesting_site_species["nesting_site_index"] = nesting_site_species[
        "NestingSite"
    ].map(
        lambda x: str(
            nesting_site.index[nesting_site["nesting_site_desc"] == x].tolist()[0] + 1
        )
        if x is not None
        else x
    )

    nesting_site_species["spec_ind_hab_ind"] = (
        nesting_site_species["species_index"]
        + "+"
        + nesting_site_species["nesting_site_index"].dropna()
    )

    uni = [
        x.split("+") for x in nesting_site_species["spec_ind_hab_ind"].dropna().unique()
    ]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"species_id": a, "nesting_site_id": b})

    return df


def structure_activity_species(
    data_frame: object, species: object, nesting_site: object
) -> object:
    """Structures data for activity_species table.

    Args:
        data_frame(object): Pandas DataFrame object
        species(object): Pandas DataFrame object
        nesting_site(object): Pandas DataFrame object

    Returns:
        activity_species_frame(object):Pandas DataFrame object with data
    """
    logger.debug("act spec")

    activity_species = data_frame[["Species", "Activity"]]

    activity_species["species_index"] = activity_species["Species"].map(
        lambda x: str(species.index[species["species_name_latin"] == x].tolist()[0] + 1)
    )

    activity_species["activity_index"] = activity_species["Activity"].map(
        lambda x: str(
            nesting_site.index[nesting_site["activity_kind"] == x].tolist()[0] + 1
        )
        if x is not None
        else x
    )

    activity_species["spec_ind_hab_ind"] = (
        activity_species["species_index"]
        + "+"
        + activity_species["activity_index"].dropna()
    )

    uni = [x.split("+") for x in activity_species["spec_ind_hab_ind"].dropna().unique()]

    a = []
    b = []

    for x in uni:
        a.append(x[0])
        b.append(x[1])

    df = pandas.DataFrame({"species_id": a, "activity_id": b})

    return df
