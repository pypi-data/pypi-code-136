import copy
import datetime

from geoformat.conf.error_messages import (
    field_exists,
    field_missing,
    field_name_still_indexing,
    field_name_not_indexing,
)
from geoformat.manipulation.geolayer_manipulation import (
    delete_feature,
    drop_field,
    rename_field,
    create_field,
    add_attributes_index,
    check_attributes_index,
    delete_attributes_index,
    check_if_field_exists,
)
from tests.utils.tests_utils import test_function
from tests.data.geolayers import (
    geolayer_attributes_to_force_in_str,
    feature_list_data_and_geometry_geolayer,
    geolayer_attributes_only,
    geolayer_attributes_only_rename,
    geolayer_fr_dept_population,
    geolayer_geometry_only_all_geometries_type,
)
from tests.data.index import geolayer_fr_dept_population_CODE_DEPT_hash_index

delete_feature_parameters = {
    0: {
        "geolayer": copy.deepcopy(geolayer_attributes_to_force_in_str),
        "i_feat_to_delete": 0,
        "return_value": {
            "metadata": {
                "name": "attributes_to_force_only_forced",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                1: {
                    "attributes": {
                        "field_integer": "1466",
                        "field_integer_list": "[987, 2345]",
                        "field_real": "8789.0",
                        "field_real_list": "[2.0, 5.0]",
                        "field_string": "salut",
                        "field_date": "",
                        "field_time": "11:22:10.000999",
                        "field_binary": "000000000140eff36b0a3d70a440bde68b020c49ba",
                        "field_boolean": "False",
                        "field_string_list": "['hi', 'mister']",
                        "field_datetime": "2020-03-31 11:22:10.000999",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": "149",
                        "field_integer_list": "[987, 2345]",
                        "field_real": "8789.0",
                        "field_real_list": "[2.0, 5.0]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_date": "",
                        "field_time": "11:22:10.000999",
                        "field_binary": "000000000140eff36b0a3d70a440bde68b020c49ba",
                        "field_boolean": "True",
                        "field_string_list": "['hi', 'mister']",
                        "field_datetime": "2020-03-31 11:22:10.000999",
                    }
                },
            },
        },
    },
    1: {
        "geolayer": copy.deepcopy(geolayer_attributes_to_force_in_str),
        "i_feat_to_delete": [0, 1, 2],
        "return_value": {
            "metadata": {"name": "attributes_to_force_only_forced"},
            "features": {},
        },
    },
    2: {
        "geolayer": copy.deepcopy(feature_list_data_and_geometry_geolayer),
        "i_feat_to_delete": [0, 1, 2, 3],
        "return_value": {
            "metadata": {"name": "data_and_geometries"},
            "features": {},
        },
    },
}

drop_field_parameters = {
    0: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": "field_integer",
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer_list": {"type": "String", "width": 13, "index": 0},
                    "field_real": {"type": "String", "width": 7, "index": 1},
                    "field_real_list": {"type": "String", "width": 19, "index": 2},
                    "field_string": {"type": "String", "width": 26, "index": 3},
                    "field_date": {"type": "Date", "index": 4},
                    "field_time": {"type": "String", "width": 15, "index": 5},
                    "field_binary": {"type": "String", "width": 201, "index": 6},
                    "field_boolean": {"type": "String", "width": 5, "index": 7},
                    "field_string_list": {"type": "String", "width": 16, "index": 8},
                    "field_datetime": {"type": "DateTime", "index": 9},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
    },
    1: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": "field_datetime",
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
    },
    2: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": "field_string",
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_date": {"type": "Date", "index": 4},
                    "field_time": {"type": "String", "width": 15, "index": 5},
                    "field_binary": {"type": "String", "width": 201, "index": 6},
                    "field_boolean": {"type": "String", "width": 5, "index": 7},
                    "field_string_list": {"type": "String", "width": 16, "index": 8},
                    "field_datetime": {"type": "DateTime", "index": 9},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
    },
    3: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": ["field_string", "field_integer", "field_datetime"],
        "return_value": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer_list": {"type": "String", "width": 13, "index": 0},
                    "field_real": {"type": "String", "width": 7, "index": 1},
                    "field_real_list": {"type": "String", "width": 19, "index": 2},
                    "field_date": {"type": "Date", "index": 3},
                    "field_time": {"type": "String", "width": 15, "index": 4},
                    "field_binary": {"type": "String", "width": 201, "index": 5},
                    "field_boolean": {"type": "String", "width": 5, "index": 6},
                    "field_string_list": {"type": "String", "width": 16, "index": 7},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
    },
    4: {
        "geolayer": {
            "metadata": {
                "name": "new_geolayer",
                "fields": {
                    "field_integer": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 0,
                    },
                    "field_integer_list": {"type": "String", "width": 13, "index": 1},
                    "field_real": {"type": "String", "width": 7, "index": 2},
                    "field_real_list": {"type": "String", "width": 19, "index": 3},
                    "field_string": {"type": "String", "width": 26, "index": 4},
                    "field_date": {"type": "Date", "index": 5},
                    "field_time": {"type": "String", "width": 15, "index": 6},
                    "field_binary": {"type": "String", "width": 201, "index": 7},
                    "field_boolean": {"type": "String", "width": 5, "index": 8},
                    "field_string_list": {"type": "String", "width": 16, "index": 9},
                    "field_datetime": {"type": "DateTime", "index": 10},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586.0,
                        "field_integer_list": "[5879, 8557]",
                        "field_real": "8789.98",
                        "field_real_list": "[89798.3654, 8757.]",
                        "field_string": None,
                        "field_date": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ).date(),  # 5
                        "field_time": "18:41:04",
                        "field_binary": "b'\\x00\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x02\\x00\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00?\\xf0\\x00\\x00\\x00\\x00\\x00\\x00'",
                        "field_boolean": "True",
                    }
                },
                1: {
                    "attributes": {
                        "field_integer": 1466.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]",
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "salut",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": str(
                            b"\x00\x00\x00\x00\x01@\xef\xf3k\n=p\xa4@\xbd\xe6\x8b\x02\x0cI\xba"
                        ),
                        "field_boolean": "False",
                    }
                },
                2: {
                    "attributes": {
                        "field_integer": 149.0,
                        "field_integer_list": "[987, 2345.0]",  # good value "[987, 2345.0]"
                        "field_real": "8789",
                        "field_real_list": "[2, 5]",
                        "field_string": "2020-03-31 11:22:10.000999",
                        "field_string_list": "['hi', 'mister']",
                        "field_time": "11:22:10.000999",
                        "field_datetime": datetime.datetime(
                            year=2020,
                            month=3,
                            day=31,
                            hour=11,
                            minute=22,
                            second=10,
                            microsecond=999,
                        ),
                        "field_binary": None,
                        "field_boolean": "1",
                    }
                },
            },
        },
        "field_name_to_drop": [
            "field_string_list",
            "field_binary",
            "field_time",
            "field_boolean",
            "field_integer_list",
            "field_datetime",
            "field_real",
            "field_string",
            "field_integer",
            "field_real_list",
            "field_date",
        ],
        "return_value": {"metadata": {"name": "new_geolayer"}, "features": {}},
    },
}

rename_field_parameters = {
    0: {
        "geolayer": geolayer_attributes_only,
        "old_field_name": "field_integer",
        "new_field_name": "field_integer_rename",
        "return_value": geolayer_attributes_only_rename,
    },
    1: {
        "geolayer": geolayer_attributes_only,
        "old_field_name": "foo",
        "new_field_name": "field_integer_rename",
        "return_value": field_missing.format(field_name="foo"),
    },
    2: {
        "geolayer": geolayer_attributes_only,
        "old_field_name": "field_string_list",
        "new_field_name": "field_string",
        "return_value": field_exists.format(field_name="field_string"),
    },
}

create_field_parameters = {
    0: {
        "geolayer": copy.deepcopy(geolayer_attributes_only),
        "field_name": "foo",
        "field_type": "Date",
        "field_width": None,
        "field_precision": None,
        "field_index": None,
        "return_value": {
            "metadata": {
                "name": "attributes_only",
                "fields": {
                    "field_integer": {"type": "Integer", "index": 0},
                    "field_integer_list": {"type": "IntegerList", "index": 1},
                    "field_real": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 2,
                    },
                    "field_real_list": {
                        "type": "RealList",
                        "width": 10,
                        "precision": 5,
                        "index": 3,
                    },
                    "field_string": {"type": "String", "width": 5, "index": 4},
                    "field_string_list": {"type": "StringList", "width": 8, "index": 5},
                    "field_date": {"type": "Date", "index": 6},
                    "field_time": {"type": "Time", "index": 7},
                    "field_datetime": {"type": "DateTime", "index": 8},
                    "field_binary": {"type": "Binary", "index": 9},
                    "field_boolean": {"type": "Boolean", "index": 10},
                    "foo": {"type": "Date", "index": 11},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586,
                        "field_integer_list": [5879, 8557],
                        "field_real": 8789.97568,
                        "field_real_list": [89798.3654, 8757.97568],
                        "field_string": "salut",
                        "field_string_list": ["bonjour", "monsieur"],
                        "field_none": None,
                        "field_date": datetime.date(2020, 3, 31),
                        "field_time": datetime.time(11, 22, 10, 999),
                        "field_datetime": datetime.datetime(
                            2020, 3, 31, 11, 22, 10, 999
                        ),
                        "field_binary": b"\x00\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01?\xf0\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00",
                        "field_boolean": True,
                    }
                }
            },
        },
    },
    1: {
        "geolayer": copy.deepcopy(geolayer_attributes_only),
        "field_name": "foo",
        "field_type": "Binary",
        "field_width": None,
        "field_precision": None,
        "field_index": 0,
        "return_value": {
            "metadata": {
                "name": "attributes_only",
                "fields": {
                    "field_integer": {"type": "Integer", "index": 1},
                    "field_integer_list": {"type": "IntegerList", "index": 2},
                    "field_real": {
                        "type": "Real",
                        "width": 9,
                        "precision": 5,
                        "index": 3,
                    },
                    "field_real_list": {
                        "type": "RealList",
                        "width": 10,
                        "precision": 5,
                        "index": 4,
                    },
                    "field_string": {"type": "String", "width": 5, "index": 5},
                    "field_string_list": {"type": "StringList", "width": 8, "index": 6},
                    "field_date": {"type": "Date", "index": 7},
                    "field_time": {"type": "Time", "index": 8},
                    "field_datetime": {"type": "DateTime", "index": 9},
                    "field_binary": {"type": "Binary", "index": 10},
                    "field_boolean": {"type": "Boolean", "index": 11},
                    "foo": {"type": "Binary", "index": 0},
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "field_integer": 586,
                        "field_integer_list": [5879, 8557],
                        "field_real": 8789.97568,
                        "field_real_list": [89798.3654, 8757.97568],
                        "field_string": "salut",
                        "field_string_list": ["bonjour", "monsieur"],
                        "field_none": None,
                        "field_date": datetime.date(2020, 3, 31),
                        "field_time": datetime.time(11, 22, 10, 999),
                        "field_datetime": datetime.datetime(
                            2020, 3, 31, 11, 22, 10, 999
                        ),
                        "field_binary": b"\x00\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01?\xf0\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00",
                        "field_boolean": True,
                    }
                }
            },
        },
    },
}

add_attributes_index_parameters = {
    0: {
        "geolayer": copy.deepcopy(geolayer_fr_dept_population),
        "field_name": "CODE_DEPT",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": {
            "metadata": {
                "name": "dept_population",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "INSEE_REG": {"type": "String", "width": 2, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "AREA": {"type": "Real", "width": 7, "precision": 2, "index": 3},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 4},
                },
                "index": {
                    "attributes": {
                        "CODE_DEPT": {
                            "type": "hashtable",
                            "index": {
                                "32": [0],
                                "47": [1],
                                "38": [2],
                                "62": [3],
                                "08": [4],
                                "10": [5],
                                "42": [6],
                                "06": [7],
                                "31": [8],
                                "71": [9],
                                "53": [10],
                                "78": [11],
                                "50": [12],
                                "16": [13],
                                "25": [14],
                                "55": [15],
                                "33": [16],
                                "14": [17],
                                "88": [18],
                                "18": [19],
                                "07": [20],
                                "02": [21],
                                "64": [22],
                                "41": [23],
                                "57": [24],
                                "86": [25],
                                "24": [26],
                                "39": [27],
                                "82": [28],
                                "49": [29],
                                "69": [30],
                                "12": [31],
                                "23": [32],
                                "45": [33],
                                "70": [34],
                                "63": [35],
                                "81": [36],
                                "27": [37],
                                "76": [38],
                                "52": [39],
                                "30": [40],
                                "67": [41],
                                "11": [42],
                                "77": [43],
                                "43": [44],
                                "51": [45],
                                "80": [46],
                                "46": [47],
                                "65": [48],
                                "04": [49],
                                "72": [50],
                                "56": [51],
                                "2A": [52],
                                "28": [53],
                                "54": [54],
                                "01": [55],
                                "19": [56],
                                "09": [57],
                                "68": [58],
                                "59": [59],
                                "90": [60],
                                "44": [61],
                                "89": [62],
                                "35": [63],
                                "40": [64],
                                "29": [65],
                                "74": [66],
                                "60": [67],
                                "95": [68],
                                "58": [69],
                                "61": [70],
                                "91": [71],
                                "21": [72],
                                "22": [73],
                                "03": [74],
                                "17": [75],
                                "15": [76],
                                "34": [77],
                                "26": [78],
                                "66": [79],
                                "73": [80],
                                "37": [81],
                                "05": [82],
                                "79": [83],
                                "84": [84],
                                "36": [85],
                                "2B": [86],
                                "87": [87],
                                "85": [88],
                                "83": [89],
                                "94": [90],
                                "92": [91],
                                "48": [92],
                                "13": [93],
                                "93": [94],
                                "75": [95],
                            },
                        }
                    }
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                    }
                },
                10: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "INSEE_REG": "52",
                        "POPULATION": 307445,
                        "AREA": 5208.37,
                        "DENSITY": 59.03,
                    }
                },
                11: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                    }
                },
            },
        },
    },
    1: {
        "geolayer": {
            "metadata": {
                "name": "dept_population",
                "fields": {
                    "CODE_DEPT": {"type": "String", "width": 2, "index": 0},
                    "INSEE_REG": {"type": "String", "width": 2, "index": 1},
                    "POPULATION": {"type": "Integer", "index": 2},
                    "AREA": {"type": "Real", "width": 7, "precision": 2, "index": 3},
                    "DENSITY": {"type": "Real", "width": 7, "precision": 2, "index": 4},
                },
                "index": {
                    "attributes": {
                        "CODE_DEPT": {
                            "type": "hashtable",
                            "index": {
                                "32": [0],
                                "47": [1],
                                "38": [2],
                                "62": [3],
                                "08": [4],
                                "10": [5],
                                "42": [6],
                                "06": [7],
                                "31": [8],
                                "71": [9],
                                "53": [10],
                                "78": [11],
                                "50": [12],
                                "16": [13],
                                "25": [14],
                                "55": [15],
                                "33": [16],
                                "14": [17],
                                "88": [18],
                                "18": [19],
                                "07": [20],
                                "02": [21],
                                "64": [22],
                                "41": [23],
                                "57": [24],
                                "86": [25],
                                "24": [26],
                                "39": [27],
                                "82": [28],
                                "49": [29],
                                "69": [30],
                                "12": [31],
                                "23": [32],
                                "45": [33],
                                "70": [34],
                                "63": [35],
                                "81": [36],
                                "27": [37],
                                "76": [38],
                                "52": [39],
                                "30": [40],
                                "67": [41],
                                "11": [42],
                                "77": [43],
                                "43": [44],
                                "51": [45],
                                "80": [46],
                                "46": [47],
                                "65": [48],
                                "04": [49],
                                "72": [50],
                                "56": [51],
                                "2A": [52],
                                "28": [53],
                                "54": [54],
                                "01": [55],
                                "19": [56],
                                "09": [57],
                                "68": [58],
                                "59": [59],
                                "90": [60],
                                "44": [61],
                                "89": [62],
                                "35": [63],
                                "40": [64],
                                "29": [65],
                                "74": [66],
                                "60": [67],
                                "95": [68],
                                "58": [69],
                                "61": [70],
                                "91": [71],
                                "21": [72],
                                "22": [73],
                                "03": [74],
                                "17": [75],
                                "15": [76],
                                "34": [77],
                                "26": [78],
                                "66": [79],
                                "73": [80],
                                "37": [81],
                                "05": [82],
                                "79": [83],
                                "84": [84],
                                "36": [85],
                                "2B": [86],
                                "87": [87],
                                "85": [88],
                                "83": [89],
                                "94": [90],
                                "92": [91],
                                "48": [92],
                                "13": [93],
                                "93": [94],
                                "75": [95],
                            },
                        }
                    }
                },
            },
            "features": {
                0: {
                    "attributes": {
                        "CODE_DEPT": "32",
                        "INSEE_REG": "76",
                        "POPULATION": 191091,
                        "AREA": 6304.33,
                        "DENSITY": 30.31,
                    }
                },
                1: {
                    "attributes": {
                        "CODE_DEPT": "47",
                        "INSEE_REG": "75",
                        "POPULATION": 332842,
                        "AREA": 5382.87,
                        "DENSITY": 61.83,
                    }
                },
                2: {
                    "attributes": {
                        "CODE_DEPT": "38",
                        "INSEE_REG": "84",
                        "POPULATION": 1258722,
                        "AREA": 7868.79,
                        "DENSITY": 159.96,
                    }
                },
                3: {
                    "attributes": {
                        "CODE_DEPT": "62",
                        "INSEE_REG": "32",
                        "POPULATION": 1468018,
                        "AREA": 6714.14,
                        "DENSITY": 218.65,
                    }
                },
                4: {
                    "attributes": {
                        "CODE_DEPT": "08",
                        "INSEE_REG": "44",
                        "POPULATION": 273579,
                        "AREA": 5253.13,
                        "DENSITY": 52.08,
                    }
                },
                5: {
                    "attributes": {
                        "CODE_DEPT": "10",
                        "INSEE_REG": "44",
                        "POPULATION": 310020,
                        "AREA": 6021.83,
                        "DENSITY": 51.48,
                    }
                },
                6: {
                    "attributes": {
                        "CODE_DEPT": "42",
                        "INSEE_REG": "84",
                        "POPULATION": 762941,
                        "AREA": 4795.85,
                        "DENSITY": 159.08,
                    }
                },
                7: {
                    "attributes": {
                        "CODE_DEPT": "06",
                        "INSEE_REG": "93",
                        "POPULATION": 1083310,
                        "AREA": 4291.62,
                        "DENSITY": 252.42,
                    }
                },
                8: {
                    "attributes": {
                        "CODE_DEPT": "31",
                        "INSEE_REG": "76",
                        "POPULATION": 1362672,
                        "AREA": 6364.82,
                        "DENSITY": 214.09,
                    }
                },
                9: {
                    "attributes": {
                        "CODE_DEPT": "71",
                        "INSEE_REG": "27",
                        "POPULATION": 553595,
                        "AREA": 8598.33,
                        "DENSITY": 64.38,
                    }
                },
                10: {
                    "attributes": {
                        "CODE_DEPT": "53",
                        "INSEE_REG": "52",
                        "POPULATION": 307445,
                        "AREA": 5208.37,
                        "DENSITY": 59.03,
                    }
                },
                11: {
                    "attributes": {
                        "CODE_DEPT": "78",
                        "INSEE_REG": "11",
                        "POPULATION": 1438266,
                        "AREA": 2305.64,
                        "DENSITY": 623.8,
                    }
                },
                12: {
                    "attributes": {
                        "CODE_DEPT": "50",
                        "INSEE_REG": "28",
                        "POPULATION": 496883,
                        "AREA": 6015.07,
                        "DENSITY": 82.61,
                    }
                },
                13: {
                    "attributes": {
                        "CODE_DEPT": "16",
                        "INSEE_REG": "75",
                        "POPULATION": 352335,
                        "AREA": 5963.54,
                        "DENSITY": 59.08,
                    }
                },
                14: {
                    "attributes": {
                        "CODE_DEPT": "25",
                        "INSEE_REG": "27",
                        "POPULATION": 539067,
                        "AREA": 5248.31,
                        "DENSITY": 102.71,
                    }
                },
                15: {
                    "attributes": {
                        "CODE_DEPT": "55",
                        "INSEE_REG": "44",
                        "POPULATION": 187187,
                        "AREA": 6233.18,
                        "DENSITY": 30.03,
                    }
                },
                16: {
                    "attributes": {
                        "CODE_DEPT": "33",
                        "INSEE_REG": "75",
                        "POPULATION": 1583384,
                        "AREA": 10068.74,
                        "DENSITY": 157.26,
                    }
                },
                17: {
                    "attributes": {
                        "CODE_DEPT": "14",
                        "INSEE_REG": "28",
                        "POPULATION": 694002,
                        "AREA": 5588.48,
                        "DENSITY": 124.18,
                    }
                },
                18: {
                    "attributes": {
                        "CODE_DEPT": "88",
                        "INSEE_REG": "44",
                        "POPULATION": 367673,
                        "AREA": 5891.56,
                        "DENSITY": 62.41,
                    }
                },
                19: {
                    "attributes": {
                        "CODE_DEPT": "18",
                        "INSEE_REG": "24",
                        "POPULATION": 304256,
                        "AREA": 7292.67,
                        "DENSITY": 41.72,
                    }
                },
                20: {
                    "attributes": {
                        "CODE_DEPT": "07",
                        "INSEE_REG": "84",
                        "POPULATION": 325712,
                        "AREA": 5562.05,
                        "DENSITY": 58.56,
                    }
                },
                21: {
                    "attributes": {
                        "CODE_DEPT": "02",
                        "INSEE_REG": "32",
                        "POPULATION": 534490,
                        "AREA": 7418.97,
                        "DENSITY": 72.04,
                    }
                },
                22: {
                    "attributes": {
                        "CODE_DEPT": "64",
                        "INSEE_REG": "75",
                        "POPULATION": 677309,
                        "AREA": 7691.6,
                        "DENSITY": 88.06,
                    }
                },
                23: {
                    "attributes": {
                        "CODE_DEPT": "41",
                        "INSEE_REG": "24",
                        "POPULATION": 331915,
                        "AREA": 6412.3,
                        "DENSITY": 51.76,
                    }
                },
                24: {
                    "attributes": {
                        "CODE_DEPT": "57",
                        "INSEE_REG": "44",
                        "POPULATION": 1043522,
                        "AREA": 6252.63,
                        "DENSITY": 166.89,
                    }
                },
                25: {
                    "attributes": {
                        "CODE_DEPT": "86",
                        "INSEE_REG": "75",
                        "POPULATION": 436876,
                        "AREA": 7025.24,
                        "DENSITY": 62.19,
                    }
                },
                26: {
                    "attributes": {
                        "CODE_DEPT": "24",
                        "INSEE_REG": "75",
                        "POPULATION": 413606,
                        "AREA": 9209.9,
                        "DENSITY": 44.91,
                    }
                },
                27: {
                    "attributes": {
                        "CODE_DEPT": "39",
                        "INSEE_REG": "27",
                        "POPULATION": 260188,
                        "AREA": 5040.63,
                        "DENSITY": 51.62,
                    }
                },
                28: {
                    "attributes": {
                        "CODE_DEPT": "82",
                        "INSEE_REG": "76",
                        "POPULATION": 258349,
                        "AREA": 3731.0,
                        "DENSITY": 69.24,
                    }
                },
                29: {
                    "attributes": {
                        "CODE_DEPT": "49",
                        "INSEE_REG": "52",
                        "POPULATION": 813493,
                        "AREA": 7161.34,
                        "DENSITY": 113.6,
                    }
                },
                30: {
                    "attributes": {
                        "CODE_DEPT": "69",
                        "INSEE_REG": "84",
                        "POPULATION": 1843319,
                        "AREA": 3253.11,
                        "DENSITY": 566.63,
                    }
                },
                31: {
                    "attributes": {
                        "CODE_DEPT": "12",
                        "INSEE_REG": "76",
                        "POPULATION": 279206,
                        "AREA": 8770.69,
                        "DENSITY": 31.83,
                    }
                },
                32: {
                    "attributes": {
                        "CODE_DEPT": "23",
                        "INSEE_REG": "75",
                        "POPULATION": 118638,
                        "AREA": 5589.16,
                        "DENSITY": 21.23,
                    }
                },
                33: {
                    "attributes": {
                        "CODE_DEPT": "45",
                        "INSEE_REG": "24",
                        "POPULATION": 678008,
                        "AREA": 6804.01,
                        "DENSITY": 99.65,
                    }
                },
                34: {
                    "attributes": {
                        "CODE_DEPT": "70",
                        "INSEE_REG": "27",
                        "POPULATION": 236659,
                        "AREA": 5382.37,
                        "DENSITY": 43.97,
                    }
                },
                35: {
                    "attributes": {
                        "CODE_DEPT": "63",
                        "INSEE_REG": "84",
                        "POPULATION": 653742,
                        "AREA": 8003.1,
                        "DENSITY": 81.69,
                    }
                },
                36: {
                    "attributes": {
                        "CODE_DEPT": "81",
                        "INSEE_REG": "76",
                        "POPULATION": 387890,
                        "AREA": 5785.79,
                        "DENSITY": 67.04,
                    }
                },
                37: {
                    "attributes": {
                        "CODE_DEPT": "27",
                        "INSEE_REG": "28",
                        "POPULATION": 601843,
                        "AREA": 6035.85,
                        "DENSITY": 99.71,
                    }
                },
                38: {
                    "attributes": {
                        "CODE_DEPT": "76",
                        "INSEE_REG": "28",
                        "POPULATION": 1254378,
                        "AREA": 6318.26,
                        "DENSITY": 198.53,
                    }
                },
                39: {
                    "attributes": {
                        "CODE_DEPT": "52",
                        "INSEE_REG": "44",
                        "POPULATION": 175640,
                        "AREA": 6249.91,
                        "DENSITY": 28.1,
                    }
                },
                40: {
                    "attributes": {
                        "CODE_DEPT": "30",
                        "INSEE_REG": "76",
                        "POPULATION": 744178,
                        "AREA": 5874.71,
                        "DENSITY": 126.67,
                    }
                },
                41: {
                    "attributes": {
                        "CODE_DEPT": "67",
                        "INSEE_REG": "44",
                        "POPULATION": 1125559,
                        "AREA": 4796.37,
                        "DENSITY": 234.67,
                    }
                },
                42: {
                    "attributes": {
                        "CODE_DEPT": "11",
                        "INSEE_REG": "76",
                        "POPULATION": 370260,
                        "AREA": 6351.35,
                        "DENSITY": 58.3,
                    }
                },
                43: {
                    "attributes": {
                        "CODE_DEPT": "77",
                        "INSEE_REG": "11",
                        "POPULATION": 1403997,
                        "AREA": 5924.64,
                        "DENSITY": 236.98,
                    }
                },
                44: {
                    "attributes": {
                        "CODE_DEPT": "43",
                        "INSEE_REG": "84",
                        "POPULATION": 227283,
                        "AREA": 4996.58,
                        "DENSITY": 45.49,
                    }
                },
                45: {
                    "attributes": {
                        "CODE_DEPT": "51",
                        "INSEE_REG": "44",
                        "POPULATION": 568895,
                        "AREA": 8195.78,
                        "DENSITY": 69.41,
                    }
                },
                46: {
                    "attributes": {
                        "CODE_DEPT": "80",
                        "INSEE_REG": "32",
                        "POPULATION": 572443,
                        "AREA": 6206.58,
                        "DENSITY": 92.23,
                    }
                },
                47: {
                    "attributes": {
                        "CODE_DEPT": "46",
                        "INSEE_REG": "76",
                        "POPULATION": 173828,
                        "AREA": 5221.64,
                        "DENSITY": 33.29,
                    }
                },
                48: {
                    "attributes": {
                        "CODE_DEPT": "65",
                        "INSEE_REG": "76",
                        "POPULATION": 228530,
                        "AREA": 4527.89,
                        "DENSITY": 50.47,
                    }
                },
                49: {
                    "attributes": {
                        "CODE_DEPT": "04",
                        "INSEE_REG": "93",
                        "POPULATION": 163915,
                        "AREA": 6993.79,
                        "DENSITY": 23.44,
                    }
                },
                50: {
                    "attributes": {
                        "CODE_DEPT": "72",
                        "INSEE_REG": "52",
                        "POPULATION": 566506,
                        "AREA": 6236.75,
                        "DENSITY": 90.83,
                    }
                },
                51: {
                    "attributes": {
                        "CODE_DEPT": "56",
                        "INSEE_REG": "53",
                        "POPULATION": 750863,
                        "AREA": 6864.07,
                        "DENSITY": 109.39,
                    }
                },
                52: {
                    "attributes": {
                        "CODE_DEPT": "2A",
                        "INSEE_REG": "94",
                        "POPULATION": 157249,
                        "AREA": 4028.53,
                        "DENSITY": 39.03,
                    }
                },
                53: {
                    "attributes": {
                        "CODE_DEPT": "28",
                        "INSEE_REG": "24",
                        "POPULATION": 433233,
                        "AREA": 5927.23,
                        "DENSITY": 73.09,
                    }
                },
                54: {
                    "attributes": {
                        "CODE_DEPT": "54",
                        "INSEE_REG": "44",
                        "POPULATION": 733481,
                        "AREA": 5283.29,
                        "DENSITY": 138.83,
                    }
                },
                55: {
                    "attributes": {
                        "CODE_DEPT": "01",
                        "INSEE_REG": "84",
                        "POPULATION": 643350,
                        "AREA": 5773.77,
                        "DENSITY": 111.43,
                    }
                },
                56: {
                    "attributes": {
                        "CODE_DEPT": "19",
                        "INSEE_REG": "75",
                        "POPULATION": 241464,
                        "AREA": 5888.93,
                        "DENSITY": 41.0,
                    }
                },
                57: {
                    "attributes": {
                        "CODE_DEPT": "09",
                        "INSEE_REG": "76",
                        "POPULATION": 153153,
                        "AREA": 4921.75,
                        "DENSITY": 31.12,
                    }
                },
                58: {
                    "attributes": {
                        "CODE_DEPT": "68",
                        "INSEE_REG": "44",
                        "POPULATION": 764030,
                        "AREA": 3526.37,
                        "DENSITY": 216.66,
                    }
                },
                59: {
                    "attributes": {
                        "CODE_DEPT": "59",
                        "INSEE_REG": "32",
                        "POPULATION": 2604361,
                        "AREA": 5774.99,
                        "DENSITY": 450.97,
                    }
                },
                60: {
                    "attributes": {
                        "CODE_DEPT": "90",
                        "INSEE_REG": "27",
                        "POPULATION": 142622,
                        "AREA": 609.64,
                        "DENSITY": 233.94,
                    }
                },
                61: {
                    "attributes": {
                        "CODE_DEPT": "44",
                        "INSEE_REG": "52",
                        "POPULATION": 1394909,
                        "AREA": 6992.78,
                        "DENSITY": 199.48,
                    }
                },
                62: {
                    "attributes": {
                        "CODE_DEPT": "89",
                        "INSEE_REG": "27",
                        "POPULATION": 338291,
                        "AREA": 7450.97,
                        "DENSITY": 45.4,
                    }
                },
                63: {
                    "attributes": {
                        "CODE_DEPT": "35",
                        "INSEE_REG": "53",
                        "POPULATION": 1060199,
                        "AREA": 6830.2,
                        "DENSITY": 155.22,
                    }
                },
                64: {
                    "attributes": {
                        "CODE_DEPT": "40",
                        "INSEE_REG": "75",
                        "POPULATION": 407444,
                        "AREA": 9353.03,
                        "DENSITY": 43.56,
                    }
                },
                65: {
                    "attributes": {
                        "CODE_DEPT": "29",
                        "INSEE_REG": "53",
                        "POPULATION": 909028,
                        "AREA": 6756.76,
                        "DENSITY": 134.54,
                    }
                },
                66: {
                    "attributes": {
                        "CODE_DEPT": "74",
                        "INSEE_REG": "84",
                        "POPULATION": 807360,
                        "AREA": 4596.53,
                        "DENSITY": 175.65,
                    }
                },
                67: {
                    "attributes": {
                        "CODE_DEPT": "60",
                        "INSEE_REG": "32",
                        "POPULATION": 824503,
                        "AREA": 5893.6,
                        "DENSITY": 139.9,
                    }
                },
                68: {
                    "attributes": {
                        "CODE_DEPT": "95",
                        "INSEE_REG": "11",
                        "POPULATION": 1228618,
                        "AREA": 1254.18,
                        "DENSITY": 979.62,
                    }
                },
                69: {
                    "attributes": {
                        "CODE_DEPT": "58",
                        "INSEE_REG": "27",
                        "POPULATION": 207182,
                        "AREA": 6862.87,
                        "DENSITY": 30.19,
                    }
                },
                70: {
                    "attributes": {
                        "CODE_DEPT": "61",
                        "INSEE_REG": "28",
                        "POPULATION": 283372,
                        "AREA": 6142.73,
                        "DENSITY": 46.13,
                    }
                },
                71: {
                    "attributes": {
                        "CODE_DEPT": "91",
                        "INSEE_REG": "11",
                        "POPULATION": 1296130,
                        "AREA": 1818.35,
                        "DENSITY": 712.81,
                    }
                },
                72: {
                    "attributes": {
                        "CODE_DEPT": "21",
                        "INSEE_REG": "27",
                        "POPULATION": 532871,
                        "AREA": 8787.51,
                        "DENSITY": 60.64,
                    }
                },
                73: {
                    "attributes": {
                        "CODE_DEPT": "22",
                        "INSEE_REG": "53",
                        "POPULATION": 598814,
                        "AREA": 6963.26,
                        "DENSITY": 86.0,
                    }
                },
                74: {
                    "attributes": {
                        "CODE_DEPT": "03",
                        "INSEE_REG": "84",
                        "POPULATION": 337988,
                        "AREA": 7365.26,
                        "DENSITY": 45.89,
                    }
                },
                75: {
                    "attributes": {
                        "CODE_DEPT": "17",
                        "INSEE_REG": "75",
                        "POPULATION": 644303,
                        "AREA": 6913.03,
                        "DENSITY": 93.2,
                    }
                },
                76: {
                    "attributes": {
                        "CODE_DEPT": "15",
                        "INSEE_REG": "84",
                        "POPULATION": 145143,
                        "AREA": 5767.47,
                        "DENSITY": 25.17,
                    }
                },
                77: {
                    "attributes": {
                        "CODE_DEPT": "34",
                        "INSEE_REG": "76",
                        "POPULATION": 1144892,
                        "AREA": 6231.05,
                        "DENSITY": 183.74,
                    }
                },
                78: {
                    "attributes": {
                        "CODE_DEPT": "26",
                        "INSEE_REG": "84",
                        "POPULATION": 511553,
                        "AREA": 6553.53,
                        "DENSITY": 78.06,
                    }
                },
                79: {
                    "attributes": {
                        "CODE_DEPT": "66",
                        "INSEE_REG": "76",
                        "POPULATION": 474452,
                        "AREA": 4147.76,
                        "DENSITY": 114.39,
                    }
                },
                80: {
                    "attributes": {
                        "CODE_DEPT": "73",
                        "INSEE_REG": "84",
                        "POPULATION": 431174,
                        "AREA": 6260.4,
                        "DENSITY": 68.87,
                    }
                },
                81: {
                    "attributes": {
                        "CODE_DEPT": "37",
                        "INSEE_REG": "24",
                        "POPULATION": 606511,
                        "AREA": 6147.6,
                        "DENSITY": 98.66,
                    }
                },
                82: {
                    "attributes": {
                        "CODE_DEPT": "05",
                        "INSEE_REG": "93",
                        "POPULATION": 141284,
                        "AREA": 5685.31,
                        "DENSITY": 24.85,
                    }
                },
                83: {
                    "attributes": {
                        "CODE_DEPT": "79",
                        "INSEE_REG": "75",
                        "POPULATION": 374351,
                        "AREA": 6029.06,
                        "DENSITY": 62.09,
                    }
                },
                84: {
                    "attributes": {
                        "CODE_DEPT": "84",
                        "INSEE_REG": "93",
                        "POPULATION": 559479,
                        "AREA": 3577.19,
                        "DENSITY": 156.4,
                    }
                },
                85: {
                    "attributes": {
                        "CODE_DEPT": "36",
                        "INSEE_REG": "24",
                        "POPULATION": 222232,
                        "AREA": 6887.38,
                        "DENSITY": 32.27,
                    }
                },
                86: {
                    "attributes": {
                        "CODE_DEPT": "2B",
                        "INSEE_REG": "94",
                        "POPULATION": 177689,
                        "AREA": 4719.71,
                        "DENSITY": 37.65,
                    }
                },
                87: {
                    "attributes": {
                        "CODE_DEPT": "87",
                        "INSEE_REG": "75",
                        "POPULATION": 374426,
                        "AREA": 5549.31,
                        "DENSITY": 67.47,
                    }
                },
                88: {
                    "attributes": {
                        "CODE_DEPT": "85",
                        "INSEE_REG": "52",
                        "POPULATION": 675247,
                        "AREA": 6758.23,
                        "DENSITY": 99.91,
                    }
                },
                89: {
                    "attributes": {
                        "CODE_DEPT": "83",
                        "INSEE_REG": "93",
                        "POPULATION": 1058740,
                        "AREA": 6002.84,
                        "DENSITY": 176.37,
                    }
                },
                90: {
                    "attributes": {
                        "CODE_DEPT": "94",
                        "INSEE_REG": "11",
                        "POPULATION": 1387926,
                        "AREA": 244.7,
                        "DENSITY": 5671.95,
                    }
                },
                91: {
                    "attributes": {
                        "CODE_DEPT": "92",
                        "INSEE_REG": "11",
                        "POPULATION": 1609306,
                        "AREA": 175.63,
                        "DENSITY": 9163.05,
                    }
                },
                92: {
                    "attributes": {
                        "CODE_DEPT": "48",
                        "INSEE_REG": "76",
                        "POPULATION": 76601,
                        "AREA": 5172.02,
                        "DENSITY": 14.81,
                    }
                },
                93: {
                    "attributes": {
                        "CODE_DEPT": "13",
                        "INSEE_REG": "93",
                        "POPULATION": 2024162,
                        "AREA": 5082.57,
                        "DENSITY": 398.26,
                    }
                },
                94: {
                    "attributes": {
                        "CODE_DEPT": "93",
                        "INSEE_REG": "11",
                        "POPULATION": 1623111,
                        "AREA": 236.96,
                        "DENSITY": 6849.73,
                    }
                },
                95: {
                    "attributes": {
                        "CODE_DEPT": "75",
                        "INSEE_REG": "11",
                        "POPULATION": 2187526,
                        "AREA": 105.44,
                        "DENSITY": 20746.64,
                    }
                },
            },
        },
        "field_name": "CODE_DEPT",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": field_name_still_indexing.format(field_name="CODE_DEPT"),
    },
    2: {
        "geolayer": geolayer_fr_dept_population,
        "field_name": "CODE",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": field_missing.format(field_name="CODE"),
    },
    3: {
        "geolayer": geolayer_geometry_only_all_geometries_type,
        "field_name": "CODE_DEPT",
        "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
        "return_value": field_missing.format(field_name="CODE_DEPT"),
    },
}

check_attributes_index_parameters = {
    0: {
        "geolayer": geolayer_fr_dept_population,
        "field_name": "CODE_DEPT",
        "type": "hashtable",
        "return_value": False,
    },
    1: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": "hashtable",
        "return_value": True,
    },
    2: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": "btree",
        "return_value": False,
    },
    3: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "FOO",
        "type": "hashtable",
        "return_value": field_missing.format(field_name="FOO"),
    },
    4: {
        "geolayer": geolayer_geometry_only_all_geometries_type,
        "field_name": "FOO",
        "type": "hashtable",
        "return_value": field_missing.format(field_name="FOO"),
    },
}

delete_attributes_index_parameters = {
    0: {
        "geolayer": geolayer_fr_dept_population,
        "field_name": "CODE_DEPT",
        "type": None,
        "return_value": field_name_not_indexing.format(field_name="CODE_DEPT"),
    },
    1: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": None,
        "return_value": geolayer_fr_dept_population,
    },
    2: {
        "geolayer": add_attributes_index(
            **{
                "geolayer": copy.deepcopy(geolayer_fr_dept_population),
                "field_name": "CODE_DEPT",
                "index": geolayer_fr_dept_population_CODE_DEPT_hash_index,
            }
        ),
        "field_name": "CODE_DEPT",
        "type": "btree",
        "return_value": field_name_not_indexing.format(field_name="CODE_DEPT"),
    },
}

check_if_field_exists_parameters = {
    0: {
        "geolayer": geolayer_attributes_only,
        "field_name": "field_integer",
        "return_value": True,
    },
    1: {
        "geolayer": geolayer_attributes_only,
        "field_name": "foo",
        "return_value": False,
    },
    2: {
        "geolayer": geolayer_geometry_only_all_geometries_type,
        "field_name": "bar",
        "return_value": False,
    },
}


def test_all():

    # delete feature
    print(test_function(delete_feature, delete_feature_parameters))

    # drop_field
    print(test_function(drop_field, drop_field_parameters))

    # rename_field
    print(test_function(rename_field, rename_field_parameters))

    # create field
    print(test_function(create_field, create_field_parameters))

    # add_attributes_index
    print(test_function(add_attributes_index, add_attributes_index_parameters))

    # check_attributes_index
    print(test_function(check_attributes_index, check_attributes_index_parameters))

    # delete_attributes_index
    print(test_function(delete_attributes_index, delete_attributes_index_parameters))

    # check_if_field_exists
    print(test_function(check_if_field_exists, check_if_field_exists_parameters))


if __name__ == "__main__":
    test_all()
