from typing import Dict

from yelpfusion3.category.model import Categories, Category, CategoryDetails


class TestCategory:
    test_data: Dict = {
        "alias": "bicycles",
        "title": "Bicycles",
        "parent_aliases": [],
        "country_whitelist": ["CZ", "DK", "PL", "PT"],
        "country_blacklist": [],
    }

    def test_deserialization(self) -> None:
        category: Category = Category(**self.test_data)

        assert category.alias == "bicycles"
        assert category.title == "Bicycles"
        assert not category.parent_aliases
        assert set(category.country_whitelist) == {"CZ", "DK", "PL", "PT"}
        assert not category.country_blacklist


class TestCategoryDetails:
    test_data: Dict = {
        "category": {
            "alias": "bicycles",
            "title": "Bicycles",
            "parent_aliases": [],
            "country_whitelist": ["CZ", "DK", "PL", "PT"],
            "country_blacklist": [],
        }
    }

    def test_deserialization(self) -> None:
        category_details: CategoryDetails = CategoryDetails(**self.test_data)

        assert category_details.category.alias == "bicycles"
        assert category_details.category.title == "Bicycles"
        assert not category_details.category.parent_aliases
        assert set(category_details.category.country_whitelist) == {"CZ", "DK", "PL", "PT"}
        assert not category_details.category.country_blacklist


class TestCategories:
    test_data: Dict = {
        "categories": [
            {
                "alias": "3dprinting",
                "title": "3D Printing",
                "parent_aliases": ["localservices"],
                "country_whitelist": [],
                "country_blacklist": [],
            },
            {
                "alias": "abruzzese",
                "title": "Abruzzese",
                "parent_aliases": ["italian"],
                "country_whitelist": ["IT"],
                "country_blacklist": [],
            },
            {
                "alias": "absinthebars",
                "title": "Absinthe Bars",
                "parent_aliases": ["bars"],
                "country_whitelist": ["CZ"],
                "country_blacklist": [],
            },
            {
                "alias": "acaibowls",
                "title": "Acai Bowls",
                "parent_aliases": ["food"],
                "country_whitelist": [],
                "country_blacklist": ["AR", "CL", "IT", "MX", "PL", "TR"],
            },
            {
                "alias": "accessories",
                "title": "Accessories",
                "parent_aliases": ["fashion"],
                "country_whitelist": [],
                "country_blacklist": [],
            },
            {
                "alias": "accountants",
                "title": "Accountants",
                "parent_aliases": ["professional"],
                "country_whitelist": [],
                "country_blacklist": [],
            },
            {
                "alias": "acnetreatment",
                "title": "Acne Treatment",
                "parent_aliases": ["beautysvc"],
                "country_whitelist": [],
                "country_blacklist": [],
            },
            {
                "alias": "active",
                "title": "Active Life",
                "parent_aliases": [],
                "country_whitelist": [],
                "country_blacklist": [],
            },
        ]
    }

    def test_deserialization(self) -> None:
        categories: Categories = Categories(**self.test_data)

        assert len(categories.categories) == 8

        assert categories.categories[0].alias == "3dprinting"
        assert categories.categories[0].title == "3D Printing"
        assert len(categories.categories[0].parent_aliases) == 1
        assert set(categories.categories[0].parent_aliases) == {"localservices"}
        assert not categories.categories[0].country_whitelist
        assert not categories.categories[0].country_blacklist

        assert categories.categories[3].alias == "acaibowls"
        assert categories.categories[3].title == "Acai Bowls"
        assert len(categories.categories[3].parent_aliases) == 1
        assert set(categories.categories[3].parent_aliases) == {"food"}
        assert not categories.categories[3].country_whitelist
        assert len(categories.categories[3].country_blacklist) == 6
        assert set(categories.categories[3].country_blacklist) == {"AR", "CL", "IT", "MX", "PL", "TR"}
