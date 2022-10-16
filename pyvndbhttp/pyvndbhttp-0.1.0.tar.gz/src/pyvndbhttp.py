import requests
import json
from enum import Enum
import copy

class QType(Enum):
    VN = "vn"
    RELEASE = "release"
    PRODUCER = "producer"
    CHARACTER = "character"
    STAFF = "staff"
    ULIST = "ulist"

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

class VNDBQuery():
    """
    Interracts with the vndb API via HTTP. Works like a SQL query builder
    """
    def __init__(self):
        self._api_url = "https://beta.vndb.org/api/kana/"
        self._query = {}
    

    def Get(self):
        try :
            r = requests.post(self._api_url + self._type.value, data=self.Request(), headers={"Content-Type": "application/json"})
            self._query = {}
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            pretty_print_POST(r.request)
            print(r.text)
            self._query = {}
            raise SystemExit(err)
        
        return r.json()

    def Filters(self, filters):
        """
        Filters are used to determine which database items to fetch.
        Filters can either be a JSON string representing filters, a list of Filters, or a compact filters string representation.
        """

        self._query["filters"] = filters
        return self

    def Fields(self, fields: str):
        """
        Comma-separated list of fields to fetch for each database item. 
        Dot notation can be used to select nested JSON objects, e.g. "image.url" will select the url field inside the image object. 
        Multiple nested fields can be selected with brackets, e.g. "image{id,url,dims}" is equivalent to "image.id, image.url, image.dims". 
        Every field of interest must be explicitely mentioned, there is no support for wildcard matching. 
        The same applies to nested objects, it is an error to list image without sub-fields in the example above. 
        The top-level id field is always selected by default and does not have to be mentioned in this list. 
        """

        self._query["fields"] = fields
        return self

    def Sort(self, sort: str):
        """
        Field to sort on. Supported values depend on the type of data being queried
        """

        self._query["sort"] = sort
        return self

    def Reverse(self):
        """
        Reverse sorting order
        """
        if "reverse" in self._query:
            self._query["reverse"] = not self._query["reverse"]
        else:
            self._query["reverse"] = True

        return self

    def Results(self, results: int):
        """
        Number of results per page, max 100
        """

        if type(results) is int:
            if results <= 100 and results > 0:
                self._query["results"] = results
            else:
                raise ValueError("Results must be between 1 and 100")
        else:
            raise TypeError("Results must be int type")

        return self

    def Page(self, page: int):
        """
        Page number to request, starting from 1.
        """

        if type(page) is int:
            if page >= 1:
                self._query["page"] = page
            else:
                raise ValueError("Page must be greater or equals to 1")
        else:
            raise TypeError("Page must be int type")
        
        return self
        
    def Count(self, count: bool):
        """
        Whether the response should include the count field.
        Indicates the total number of entries that matched the given filters.
        This option should be avoided when the count is not needed since it has a considerable performance impact. 
        """

        if type(count) is bool:
            self._query["count"] = count
        else:
            raise TypeError("Count must be bool type")

        return self

    def CompactFilters(self, compact_filters: bool):
        """
        Whether the response should include the compact_filters field.
        Compact Filters is a compact string representation of the filters given in the query
        """

        if type(compact_filters) is bool:
            self._query["compact_filters"] = compact_filters
        else:
            raise TypeError("compact_filters must be bool type")
        
        return self

    def NormalizedFilters(self, normalized_filters: bool):
        """
        Whether the response should include the normalized_filters field.
        Normalized Filters is a normalized JSON representation of the filters given in the query
        """

        if type(normalized_filters) is bool:
            self._query["normalized_filters"] = normalized_filters
        else:
            raise TypeError("normalized_filters must be bool type")
        
        return self

    def Type(self, qtype: QType):
        """
        Set the type of resource you want to query.
        """
        if type(qtype) is QType:
            self._type = qtype
        else:
            raise TypeError("Qtype must be Qtype type")
        return self

    def Request(self):
        """
        Return the JSON formatted request send to the API.
        """
        query = copy.deepcopy(self._query)

        if "filters" in query:
            query["filters"] = query["filters"].tolist()

        return json.dumps(query, sort_keys=True)

    def Stats(self):
        """
        Returns a few overall database statistics.
        """
        r = requests.get(self._api_url + "stats")
        return r.json()

    def List(self, userid: str):

        if type(userid) is str:
            self._query["user"] = userid
            self._type = QType.ULIST
        else:
            raise TypeError("Userid must be str")
        return self

    def __str__(self):
        return self.Request()

class And():
    def __init__(self, *args):
        self._list = []
        self._list.append("and")

        for arg in args:
            if isinstance(arg, Filter) or isinstance(arg, Or) or isinstance(arg, And):
                self._list.append(arg.tolist())
            else:
                self._list.append(arg)

    def __str__(self):
        r = "["

        for item in self._list:
            r += str(item)+","

        r = r[:-1]+"]"
        return r
    
    def tolist(self):
        return self._list

class Or():
    def __init__(self, *args):
        self._list = []
        self._list.append("or")

        for arg in args:
            if isinstance(arg, Filter) or isinstance(arg, Or) or isinstance(arg, And):
                self._list.append(arg.tolist())
            else:
                self._list.append(arg)

    def __str__(self):
        r = "["

        for item in self._list:
            r += str(item)+","

        r = r[:-1]+"]"
        return r

    def tolist(self):
        return self._list

                

class Filter():
    def __init__(self, name="", operator="", value=""):
        self._name = name
        self._operator = operator
        self._value = value

    def __str__(self):
        return str()
    
    def tolist(self):
        r = []
        r.append(self._name)
        r.append(self._operator)

        if isinstance(self._value, Filter) or isinstance(self._value, Or) or isinstance(self._value, And):
            r.append(self._value.tolist())
        else:
            r.append(self._value)

        return r
