from typing import List

from pydantic import constr

from yelpfusion3.model import Model


class Category(Model):
    """
    Detailed information about a Yelp category.
    """

    alias: constr(min_length=1)
    """
    Category alias.
    """

    title: constr(min_length=1)
    """
    Title of this category.
    """

    parent_aliases: List[constr(min_length=1)] = []
    """
    List of aliases of parent categories.
    """

    country_whitelist: List[constr(min_length=1)] = []
    """
    Countries for which this category is whitelisted.
    """

    country_blacklist: List[constr(min_length=1)] = []
    """
    Countries for which this category is blacklisted.
    """


class CategoryDetails(Model):
    """
    Detailed information about the Yelp category.
    """

    category: Category
    """
    Detailed information about the Yelp category.
    """


class Categories(Model):
    """
    All Yelp business categories for a given locale.
    """

    categories: List[Category]
    """
    A list of all the categories for this locale.
    """
