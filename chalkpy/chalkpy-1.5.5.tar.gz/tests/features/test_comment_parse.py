from datetime import datetime

import pytest

from chalk.features import feature, feature_time, features
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


def test_comment_based_owner():
    assert "elliot@chalk.ai" == unwrap_feature(CommentBaseOwner.empty).owner
    assert ["pii", "group:risk"] == unwrap_feature(CommentBaseOwner.email).tags
    assert ["pii"] == unwrap_feature(CommentBaseOwner.email_single).tags
    assert ["hello", "pii"] == unwrap_feature(CommentBaseOwner.email_all_kinds).tags
    with pytest.raises(ValueError):

        @features
        class BadFeatureClass:
            # :owner: elliot@chalk.ai
            doubly_owned: str = feature(owner="d")


def test_parse_descriptions():
    assert "bizarre" == unwrap_feature(WowFS.bizarre).description
    assert "This is a really neat description of something" == unwrap_feature(WowFS.something).description
    assert "explicit comment" == unwrap_feature(WowFS.explicit).description
    assert "This is also really neat and cool" == unwrap_feature(WowFS.something_else).description
    assert "now with feature" == unwrap_feature(WowFS.assigned_comment).description
    assert "goofy" == unwrap_feature(WowFS.goofy).description
    assert (
        """Multiline
Neat and, verily, cool

Hello"""
        == unwrap_feature(WowFS.assigned_comment_multiline).description
    )


def test_class_owner():
    assert "elliot@chalk.ai" == OwnerFeatures.__chalk_owner__
    assert "elliot@chalk.ai" == unwrap_feature(OwnerFeatures.plain).owner
    assert "elliot@chalk.ai" == unwrap_feature(OwnerFeatures.cached).owner
    assert "andy@chalk.ai" == unwrap_feature(OwnerFeatures.andy).owner


def test_class_tags():
    assert ["1", "2"] == TagFeatures.__chalk_tags__
    assert ["1", "2"] == unwrap_feature(TagFeatures.empty).tags
    assert ["one", "1", "2"] == unwrap_feature(TagFeatures.one).tags
    assert ["a", "b", "1", "2"] == unwrap_feature(TagFeatures.many).tags
    assert ["a", "t"] == unwrap_feature(WowFS.assigned).tags
    assert ["t"] == unwrap_feature(WowFS.nope).tags
    assert ["3", "4", "t"] == unwrap_feature(WowFS.assigned_comment).tags
