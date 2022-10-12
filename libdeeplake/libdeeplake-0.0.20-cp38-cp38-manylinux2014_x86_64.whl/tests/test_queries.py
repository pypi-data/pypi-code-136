from indra import api
from .constants import (
    COCO_DS_NAME,
    MNIST_DS_NAME,
    IMAGENET_DS_NAME,
    LAION_400_M_DS_NAME,
)

from time import time

queries = {
    COCO_DS_NAME: [
        ("SELECT * WHERE categories[0] == 'person'", 22706, None),
        ("SELECT * WHERE shape(categories)[0] == 0", 1021, None),
        ("SELECT * WHERE shape(boxes)[0] == 5", 7712, None),
        ("SELECT * WHERE shape(images)[0] > 200", 118078, None),
        ("SELECT * WHERE shape(images)[1] > 200", 118219, None),
        ("SELECT * WHERE shape(images)[2] == 3", 118060, None),
        ("SELECT * WHERE shape(images)[2] == 2", 0, None),
        ("SELECT * WHERE shape(images)[999] > 200", 0, None),
        (
            "SELECT * WHERE ALL_STRICT(categories == 'person') or shape(categories)[0] == 0",
            1375,
            None
        ),
        ("SELECT * WHERE ALL(categories == 'person')", 1375, None),
        ("select * where ALL_STRICT(categories == 'person')", 354, None),
        ("select * where ALL_STRICT(\"pose/categories\" == 'person')", 64115, None),
        ("select * where any(categories == 'banana')", 2243, None),
        ("select * where any(categories == 'person')", 64115, None),
        (
            "select * where all_strict(logical_and(categories == 'car', boxes[:,3] > 200))",
            5,
            None
        ),
        (
            "select * where any(logical_and(categories == 'car', boxes[:,3] > 200))",
            1242,
            None
        ),
        (
            "select * where all_strict(logical_or(categories == 'person', categories == 'banana'))",
            873,
            None
        ),
        (
            "select * where logical_and(categories == 'person', categories == 'person')",
            208,
            None
        ),
        ("SELECT * where images_meta['license'] == 3", 32184, None),
        ("SELECT * where images_meta['id'] > 285529", 60365, None),
        ("SELECT * where contains(categories, '*ers*')", 64115, None),
        ("SELECT * where contains(categories, '?ers*')", 64115, None),
        ("SELECT * order by images_meta['license']", 118287, None),
    ],
    MNIST_DS_NAME: [
        ("SELECT * WHERE labels == 0", 5923, None),
        ("SELECT * WHERE SHAPE(images)[0] == 28", 60000, None),
        ("SELECT * WHERE SHAPE(images)[0] == 29", 0, None),
        (
            "(select * where labels == 4 limit 10) union (select * where labels == 5 limit 10) order by labels",
            20,
            [2, 9, 20, 26, 53, 58, 60, 61, 64, 89, 0, 11, 35, 47, 65, 100, 132, 138, 145, 173]
        )
    ],
    IMAGENET_DS_NAME: [
        ("SELECT * WHERE labels == 'bikini'", 1300, None),
        ("SELECT * WHERE contains(labels, '*iki*')", 2600, None),
        ("SELECT * WHERE contains(labels, '?iki*')", 1300, None),
        ("SELECT * WHERE SHAPE(boxes)[0] > 15", 2, None),
        (
            "(SELECT * WHERE labels == 'bikini' LIMIT 10) UNION (SELECT * WHERE labels == 1 LIMIT 10) UNION (SELECT * WHERE labels == 43 LIMIT 10)",
            30,
            None
        ),
    ],
    # LAION_400_M_DS_NAME: [
    #    ("SELECT * WHERE CONTAINS(caption, 'blue')", 2783, None),
    #    ("SELECT * WHERE caption[0] == 'A'", 28904, None),
    #    ("SELECT * WHERE SHAPE(image)[0] == 256", 512993, None),
    # ],
    "hub://davitbun/places365-train-challenge": [
        ("SELECT * WHERE labels == 'hotel_room'", 32947, None),
        ("SELECT * ORDER by random()", 8026628, None),
    ],
}


def test_dataset_query_results():
    global queries
    for ds_name in queries:
        ds = api.dataset(ds_name)
        for (query, result_size, result_indices) in queries[ds_name]:
            print(f"\tRunning query: {query}")
            start = time()
            result = ds.query(query)
            print("\tQuery time: ", time() - start)
            assert len(result) == result_size
            assert result_indices is None or result.indexes == result_indices
            start = time()
            result = ds.query(query)
            print("\tSecond Query time: ", time() - start)
