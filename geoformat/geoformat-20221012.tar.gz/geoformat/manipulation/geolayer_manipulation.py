import copy

from geoformat.conf.error_messages import field_name_not_indexing
from geoformat.conf.format_data import value_to_iterable_value
from geoformat.conversion.fields_conversion import recast_field
from geoformat.manipulation.feature_manipulation import (
    rename_field_in_feature,
    drop_field_in_feature,
)
from geoformat.manipulation.metadata_manipulation import (
    drop_field_in_metadata,
    rename_field_in_metadata,
    create_field_in_metadata,
    check_if_field_exists_in_metadata,
    check_attributes_index_in_metadata,
    add_attributes_index_in_metadata,
)


def delete_feature(geolayer, i_feat_to_delete):
    """Delete given i_feat feature from geolayer

    TODO add an update for geometry_ref metadata
    """
    i_feat_to_delete_list = value_to_iterable_value(
        value=i_feat_to_delete, output_iterable_type=list
    )
    for i_feat in i_feat_to_delete_list:
        if i_feat in geolayer["features"]:
            # TODO add delete (update) index (attributes and geometry) / matrix
            del geolayer["features"][i_feat]
        else:
            raise Exception()

    if not geolayer["features"]:
        if "fields" in geolayer["metadata"]:
            del geolayer["metadata"]["fields"]

        if "geometry_ref" in geolayer["metadata"]:
            del geolayer["metadata"]["geometry_ref"]

        if "index" in geolayer["metadata"]:
            del geolayer["metadata"]["index"]

        if "matrix" in geolayer["metadata"]:
            del geolayer["metadata"]["matrix"]

    return geolayer


def drop_field(geolayer, field_name_to_drop):
    """
    This function allow to drop a field in geolayer.

    :param geolayer: input geolayer.
    :param field_name_to_drop: field name in geolayer to drop. can be a fields list
    :return: geolayer with field drop.
    """
    field_name_to_drop = value_to_iterable_value(
        value=field_name_to_drop, output_iterable_type=list
    )
    geolayer["metadata"] = drop_field_in_metadata(
        metadata=geolayer["metadata"], field_name_or_field_name_list=field_name_to_drop
    )

    # delete field in features
    delete_i_feat_list = []
    for i_feat, feature in geolayer["features"].items():
        feature = drop_field_in_feature(
            feature=feature, field_name_or_field_name_list=field_name_to_drop
        )
        geolayer["features"][i_feat] = feature

        if not feature:
            delete_i_feat_list.append(i_feat)

    # delete feature with no data in it
    if delete_i_feat_list:
        geolayer = delete_feature(
            geolayer=geolayer, i_feat_to_delete=delete_i_feat_list
        )

    return geolayer


def rename_field(geolayer, old_field_name, new_field_name):
    """
    Rename field in geolayer

    :param geolayer: input geolayer.
    :param old_field_name: actual name of field that we want to change.
    :param new_field_name: new field's name that we want to apply.
    :return: geolayer with field rename
    """
    # rename field in metadata
    geolayer["metadata"] = rename_field_in_metadata(
        metadata=geolayer["metadata"],
        old_field_name=old_field_name,
        new_field_name=new_field_name,
    )
    # rename in features
    for i_feat, feature in geolayer["features"].items():
        feature = rename_field_in_feature(
            feature=feature,
            old_field_name=old_field_name,
            new_field_name=new_field_name,
        )
        geolayer["features"][i_feat] = feature

    return geolayer


def create_field(
    geolayer,
    field_name,
    field_type,
    field_width=None,
    field_precision=None,
    field_index=None,
):
    """
    Create new field in geolayer

    :param geolayer: input geolayer
    :param field_name: new field name
    :param field_type: field type
    :param field_width: field width
    :param field_precision: field precision
    :param field_index: field index
    :return: geolayer with new field in it
    """

    output_geolayer = copy.deepcopy(geolayer)

    new_metadata = create_field_in_metadata(
        metadata=geolayer["metadata"],
        field_name=field_name,
        field_type=field_type,
        field_width=field_width,
        field_precision=field_precision,
    )

    output_geolayer["metadata"] = new_metadata
    if new_metadata["fields"][field_name]["index"] != field_index:
        output_geolayer = recast_field(
            geolayer_to_recast=output_geolayer,
            field_name_to_recast=field_name,
            reindex=field_index,
        )

    return output_geolayer


def add_attributes_index(geolayer, field_name, index):
    """Store index in geolayer

    :param geolayer: geolayer to add an attributes
    :field_name: name of field concern by index
    :index: index that we want to add to field of geolayer
    :return: geolayer with index in it
    """

    metadata = add_attributes_index_in_metadata(
        metadata=geolayer["metadata"], field_name=field_name, index=index
    )
    geolayer["metadata"] = metadata

    return geolayer


def check_attributes_index(geolayer, field_name, type=None):
    """
    Return True or False if an attributes index in found in geolayer for input field_name optionaly we can test
    type index

    :param geolayer: input geolayer
    :param field_name: field name where is the index
    :param type: type of indexing (hashtable/btree ...)
    :return: Boolean
    """

    return check_attributes_index_in_metadata(
        metadata=geolayer["metadata"], field_name=field_name, type=type
    )


def delete_attributes_index(geolayer, field_name, type=None):
    """Delete attributes index when existing in geolayer. Opionnaly you can filter on index type

    :param geolayer: input Geolayer
    :param field_name: field name where is the index
    :param type: type of indexing (hashtable/btree ...)
    :return: Geolayer without index for given field_name (and optionally index type)
    """

    if check_attributes_index(geolayer, field_name, type) is True:
        del geolayer["metadata"]["index"]["attributes"][field_name]
        if len(geolayer["metadata"]["index"]["attributes"]) == 0:
            del geolayer["metadata"]["index"]["attributes"]
        if len(geolayer["metadata"]["index"]) == 0:
            del geolayer["metadata"]["index"]
    else:
        raise Exception(field_name_not_indexing.format(field_name=field_name))

    return geolayer


def check_if_field_exists(geolayer, field_name):
    """
    Check if field exists in given Geolayer.

    :param geolayer: input geolayer where existing field name is tested.
    :param field_name: name of field.
    :return: True if field exists False if not.
    """

    return check_if_field_exists_in_metadata(
        metadata=geolayer["metadata"], field_name=field_name
    )
