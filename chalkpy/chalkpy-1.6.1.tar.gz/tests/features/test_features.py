from datetime import datetime

from chalk.features import DataFrame, Feature, Features, features, has_many, has_one, online
from chalk.features.feature import unwrap_feature
from chalk.features.feature_set import feature_time


@features
class ChildFS:
    parent_id: str
    parents: "DataFrame[ParentFS]"
    single_parent: "SingleParentFS"


@features
class SingleChildFS:
    parent_id: str
    parent: "DataFrame[ParentFS]"


@features
class SingleParentFS:
    id: str
    children: DataFrame[ChildFS] = has_many(lambda: ChildFS.parent_id == SingleParentFS.id)


@features
class ParentFS:
    id: str
    children: "DataFrame[ChildFS]" = has_many(lambda: ChildFS.parent_id == ParentFS.id)
    single_child: "SingleChildFS" = has_one(lambda: ParentFS.id == SingleChildFS.parent_id)
    ts: datetime = feature_time()


@online
def get_parent_time(p: ParentFS.id) -> Features[ParentFS.ts]:
    thing = ParentFS(ts=datetime.now())
    return thing


def test_one_to_one():
    """
    FeatureSet              -> FeatureSet
    SingleParentFS.children -> ChildFS.single_parent
    """
    parent_from_features: Feature = next((x for x in ChildFS.features if x.is_has_one))
    parent_from_attr = unwrap_feature(ChildFS.single_parent)
    assert parent_from_features == parent_from_attr
    assert parent_from_features.name == "single_parent"
    assert parent_from_features.namespace == "child_fs"
    assert parent_from_features.is_has_one
    assert parent_from_features.typ is not None
    assert parent_from_features.typ.underlying == SingleParentFS
    assert parent_from_features.join == unwrap_feature(SingleParentFS.children).join
    assert len(unwrap_feature(SingleParentFS.children).typ.parsed_annotation.columns) == 1


def test_one_to_many():
    """
    FeatureSet            -> DataFrame
    ParentFS.single_child -> SingleChildFS.parent
    """
    parent_from_features: Feature = next((x for x in SingleChildFS.features if x.is_has_many))
    parent_from_attr = unwrap_feature(SingleChildFS.parent)
    assert parent_from_features == parent_from_attr
    assert parent_from_features.name == "parent"
    assert parent_from_features.namespace == "single_child_fs"
    assert parent_from_features.is_has_many
    assert parent_from_features.typ is not None
    assert issubclass(parent_from_features.typ.parsed_annotation, DataFrame)
    assert issubclass(parent_from_features.typ.parsed_annotation, DataFrame)  # for pylance
    assert parent_from_features.typ.parsed_annotation.references_feature_set == ParentFS
    assert parent_from_features.join == unwrap_feature(ParentFS.single_child).join


def test_many_to_one():
    """
    DataFrame               -> FeatureSet
    SingleParentFS.children -> ChildFS.single_parent
    """
    parent_from_features = next((x for x in ChildFS.features if x.is_has_one))
    parent_from_attr = unwrap_feature(ChildFS.single_parent)
    assert parent_from_features == parent_from_attr
    assert parent_from_features.name == "single_parent"
    assert parent_from_features.namespace == "child_fs"
    assert parent_from_features.is_has_one
    assert parent_from_features.typ.underlying == SingleParentFS
    assert parent_from_features.join == unwrap_feature(SingleParentFS.children).join


def test_many_to_many():
    """
    DataFrame         -> DataFrame
    ParentFS.children -> ChildFS.parents
    """
    parents_from_features: Feature = next((x for x in ChildFS.features if x.is_has_many))
    parents_from_attr = unwrap_feature(ChildFS.parents)
    assert parents_from_features == parents_from_attr
    assert parents_from_features.name == "parents"
    assert parents_from_features.namespace == "child_fs"
    assert parents_from_features.is_has_many
    assert parents_from_features.typ is not None
    assert isinstance(parents_from_features.typ.parsed_annotation, type)  # for pylance
    assert issubclass(parents_from_features.typ.parsed_annotation, DataFrame)
    assert issubclass(parents_from_features.typ.parsed_annotation, DataFrame)  # for pylance
    assert parents_from_features.typ.parsed_annotation.references_feature_set == ParentFS
    assert parents_from_features.join == unwrap_feature(ParentFS.children).join
