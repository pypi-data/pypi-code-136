from datetime import datetime

import pytest

from chalk.features import feature, feature_time, features, owner, tags, description, is_primary
from chalk.features.feature import unwrap_feature


@features(tags="t", owner="andy@chalk.ai")
class WowFS:
    # This is a really neat description of something
    something: str

    # This is also really neat and cool
    something_else: str
    nocomment: str

    nope: str

    assigned: str = feature(tags="a")

    # bizarre
    bizarre: str

    # goofy
    goofy: str = feature(owner="yo")

    # now with feature
    assigned_comment: str = feature(tags=["3", "4"])

    # implicit comment
    explicit: str = feature(description="explicit comment")

    # Multiline
    # Neat and, verily, cool
    #
    # Hello
    assigned_comment_multiline: str = feature()

    # now with feature time
    time: datetime = feature_time()

    nope_nope: datetime  # Datetime field that is not feature time


@features(owner="elliot@chalk.ai")
class OwnerFeatures:
    plain: str
    cached: str = feature(max_staleness="3d")
    andy: str = feature(owner="andy@chalk.ai")

    ft: datetime = feature_time()


@features(tags=["1", "2"])
class TagFeatures:
    empty: str
    one: str = feature(tags="one")
    many: str = feature(tags=["a", "b"])

    ft: datetime = feature_time()


@features
class CommentBaseOwner:
    id: str
    # I'm a cool comment!
    # :owner: elliot@chalk.ai
    empty: str

    # I'm a cool comment!
    # :tags: pii group:risk
    email: str

    # :tags: pii, group:risk
    email_commas: str
    # :tags: pii
    email_single: str

    # :tags: pii
    email_all_kinds: str = feature(tags=["hello"])


def test_primary():
    assert is_primary(CommentBaseOwner.id)
    assert not is_primary(CommentBaseOwner.email)


def test_comment_based_owner():
    assert "elliot@chalk.ai" == unwrap_feature(CommentBaseOwner.empty).owner == owner(CommentBaseOwner.empty)
    assert ["pii", "group:risk"] == unwrap_feature(CommentBaseOwner.email).tags == tags(CommentBaseOwner.email)
    assert ["pii"] == unwrap_feature(CommentBaseOwner.email_single).tags == tags(CommentBaseOwner.email_single)
    assert (
        ["hello", "pii"]
        == unwrap_feature(CommentBaseOwner.email_all_kinds).tags
        == tags(CommentBaseOwner.email_all_kinds)
    )
    with pytest.raises(ValueError):

        @features
        class BadFeatureClass:
            # :owner: elliot@chalk.ai
            doubly_owned: str = feature(owner="d")


def test_parse_descriptions():
    assert "bizarre" == unwrap_feature(WowFS.bizarre).description == description(WowFS.bizarre)
    assert (
        "This is a really neat description of something"
        == unwrap_feature(WowFS.something).description
        == description(WowFS.something)
    )
    assert "explicit comment" == unwrap_feature(WowFS.explicit).description == description(WowFS.explicit)
    assert (
        "This is also really neat and cool"
        == unwrap_feature(WowFS.something_else).description
        == description(WowFS.something_else)
    )
    assert (
        "now with feature" == unwrap_feature(WowFS.assigned_comment).description == description(WowFS.assigned_comment)
    )
    assert "goofy" == unwrap_feature(WowFS.goofy).description == description(WowFS.goofy)
    assert (
        """Multiline
Neat and, verily, cool

Hello"""
        == unwrap_feature(WowFS.assigned_comment_multiline).description
        == description(WowFS.assigned_comment_multiline)
    )


def test_class_owner():
    assert "elliot@chalk.ai" == OwnerFeatures.__chalk_owner__ == owner(OwnerFeatures)
    assert "elliot@chalk.ai" == unwrap_feature(OwnerFeatures.plain).owner == owner(OwnerFeatures.plain)
    assert "elliot@chalk.ai" == unwrap_feature(OwnerFeatures.cached).owner == owner(OwnerFeatures.cached)
    assert "andy@chalk.ai" == unwrap_feature(OwnerFeatures.andy).owner == owner(OwnerFeatures.andy)


def test_class_tags():
    assert [] == tags(OwnerFeatures) == OwnerFeatures.__chalk_tags__
    assert ["1", "2"] == TagFeatures.__chalk_tags__ == tags(TagFeatures)
    assert ["1", "2"] == unwrap_feature(TagFeatures.empty).tags == tags(TagFeatures.empty)
    assert ["one", "1", "2"] == unwrap_feature(TagFeatures.one).tags == tags(TagFeatures.one)
    assert ["a", "b", "1", "2"] == unwrap_feature(TagFeatures.many).tags == tags(TagFeatures.many)
    assert ["a", "t"] == unwrap_feature(WowFS.assigned).tags == tags(WowFS.assigned)
    assert ["t"] == unwrap_feature(WowFS.nope).tags == tags(WowFS.nope)
    assert ["3", "4", "t"] == unwrap_feature(WowFS.assigned_comment).tags == tags(WowFS.assigned_comment)
