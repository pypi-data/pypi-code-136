import json


class ListDefaultNone(list):
    def __init__(self, *args, **kwargs):
        super(ListDefaultNone, self).__init__(*args, **kwargs)

    def __getitem__(self, y):
        return self._get(y)

    def _get(self, y):
        try:
            res = list(self or [])[y]
            if isinstance(res, (ListDefaultNone, list)):
                res = ListDefaultNone(res)
            elif isinstance(res, (DictDefaultNone, dict, type(None))):
                res = DictDefaultNone(res or {})
            return res
        except IndexError:
            return DictDefaultNone({})


class DictDefaultNone(dict):
    def __init__(self, *args, **kwargs):
        super(DictDefaultNone, self).__init__(*args, **kwargs)

    def __getitem__(self, y):
        return self._get(y)

    def get(self, k, default=None):
        return self._get(k)

    def _get(self, y):
        res = dict(self or {}).get(y)
        if isinstance(res, (ListDefaultNone, list)):
            res = ListDefaultNone(res)
        elif isinstance(res, (DictDefaultNone, dict, type(None))):
            res = DictDefaultNone(res or {})
        return res

    def split(self, x):
        return ListDefaultNone([''])


DDN = DictDefaultNone
LDN = ListDefaultNone

if __name__ == '__main__':
    data = json.loads(r"""{
    "data": [
        {
            "key1": "123",
            "key2": {
                "kkey1": {
                    "kkkey1": "1234",
                    "kkkey2": 12345
                }
            }
        },
        {
            "key1": "'1234'",
            "key3": {
                "kkey1": {
                    "kkkey1": "1234",
                    "kkkey2": true
                }
            }
        }
    ]
}""")
    data1 = DictDefaultNone(data)
    date2 = ListDefaultNone(data)
    date3 = ListDefaultNone([''])
    print(date3[-1])
    # print(data1['data'][1]["key3"])
    # print(data1['data'][1]["key2"]["url"])
    # print(data1['data'][1]["key3"]["kkey1"])
    # print(data1['data'][1]["key3"]["kkey1"]['kkkey2'])
    print(data1['data'][1]["key265"]['151'])


