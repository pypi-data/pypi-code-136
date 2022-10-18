import json
from python_helper.api.src.service import ObjectHelper
from python_helper import StringHelper, SettingHelper, Constant, log, Test, ReflectionHelper, RandomHelper

LOG_HELPER_SETTINGS = {
    log.LOG : True,
    log.SUCCESS : True,
    log.SETTING : True,
    log.DEBUG : True,
    log.WARNING : True,
    log.FAILURE : True,
    log.WRAPPER : True,
    log.ERROR : True,
    log.TEST : False,
    log.ENABLE_LOGS_WITH_COLORS : True,
    SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
}

# LOG_HELPER_SETTINGS = {
#     log.LOG : False,
#     log.SUCCESS : False,
#     log.SETTING : False,
#     log.DEBUG : False,
#     log.WARNING : False,
#     log.FAILURE : False,
#     log.WRAPPER : False,
#     log.ERROR : False,
#     log.TEST : False
# }

class MyDto:
    def __init__(self, myAttribute, myOther, myThirdList) :
        self.myAttribute = myAttribute
        self.myOther = myOther
        self.myThirdList = myThirdList

class MyOtherDto:
    def __init__(self, myAttribute) :
        self.myAttribute = myAttribute

class MyThirdDto :
    def __init__(self, my, myAttribute) :
        self.my = my
        self.myAttribute = myAttribute

DICTIONARY_INSTANCE = {
    'my_none_value' : None,
    'my_none_value-as_string' : 'None',
    'string_key_as_string' : 'value',
    'integer_key_as_string' : 12345678901,
    10987654321 : 12345678901,
    'bool_key_as_string' : True,
    False : True,
    'float_key_as_string' : 12345.678901,
    109876.54321 : 12345.678901,
    'list_key_as_string' : [
        'my',
        'list',
        'elements'
    ],
    'list_of_list_key_as_string' : [
        [
            'my',
            'first',
            'list',
            False,
            12345.678901
        ],
        [
            'my',
            'second',
            'list',
            True,
            10987654321
        ]
    ],
    'set_of_string_key_as_string' : {
        'a',
        'True',
        '2',
        '3.4',
        True,
        2,
        2.4
    }
}
JSON_INSTANCE = json.loads(StringHelper.prettyJson(DICTIONARY_INSTANCE))

TEST_SETTINGS = {}

@Test(
    environmentVariables={**{}, **LOG_HELPER_SETTINGS},
    **TEST_SETTINGS
)
def basicMethods() :
    # arrange
    def generatorInstance() :
        while True :
            yield False
            break
    STR_INSTANCE = str()
    BOOLEAN_INSTANCE = bool()
    INTEGER_INSTANCE = int()
    FLOAT_INSTANCE = float()
    DICTIONARY_INSTANCE = dict()
    LIST_INSTANCE = list()
    TUPLE_INSTANCE = tuple()
    SET_INSTANCE = set()
    GENERATOR_INSTANCE = generatorInstance()

    STR_FILLED_INSTANCE = 'str()'
    BOOLEAN_FILLED_INSTANCE = True
    INTEGER_FILLED_INSTANCE = 2
    FLOAT_FILLED_INSTANCE = 3.3
    DICTIONARY_FILLED_INSTANCE = {'dict()':dict()}
    LIST_FILLED_INSTANCE = [list(),list()]
    TUPLE_FILLED_INSTANCE = (tuple(),tuple())
    SET_FILLED_INSTANCE = {'set()',2}

    # act

    # assert
    assert ObjectHelper.isNotNone(STR_INSTANCE)
    assert ObjectHelper.isNotNone(BOOLEAN_INSTANCE)
    assert ObjectHelper.isNotNone(INTEGER_INSTANCE)
    assert ObjectHelper.isNotNone(FLOAT_INSTANCE)
    assert ObjectHelper.isNotNone(DICTIONARY_INSTANCE)
    assert ObjectHelper.isNotNone(LIST_INSTANCE)
    assert ObjectHelper.isNotNone(TUPLE_INSTANCE)
    assert ObjectHelper.isNotNone(SET_INSTANCE)
    assert ObjectHelper.isNotNone(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotNone(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotNone(SET_FILLED_INSTANCE)

    assert not ObjectHelper.isNone(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isNone(GENERATOR_INSTANCE)

    assert not ObjectHelper.isList(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isList(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isList(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isList(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isList(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isList(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isList(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isList(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isList(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotList(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isNotList(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotList(GENERATOR_INSTANCE)

    assert not ObjectHelper.isSet(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isSet(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isSet(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotSet(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isNotSet(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotSet(GENERATOR_INSTANCE)

    assert not ObjectHelper.isTuple(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isTuple(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isTuple(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotTuple(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isNotTuple(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotTuple(GENERATOR_INSTANCE)

    assert not ObjectHelper.isDictionary(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isDictionary(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionary(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotDictionary(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isNotDictionary(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionary(GENERATOR_INSTANCE)

    assert not ObjectHelper.isCollection(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isCollection(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isCollection(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isCollection(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isCollection(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isCollection(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isCollection(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isCollection(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isCollection(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotCollection(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotCollection(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotCollection(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotCollection(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isNotCollection(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isNotCollection(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isNotCollection(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isNotCollection(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotCollection(GENERATOR_INSTANCE)

    assert not ObjectHelper.isDictionaryClass(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isDictionaryClass(GENERATOR_INSTANCE)

    assert ObjectHelper.isNotDictionaryClass(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNotDictionaryClass(GENERATOR_INSTANCE)

    assert not ObjectHelper.isDictionaryClass(type(STR_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(BOOLEAN_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(INTEGER_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(FLOAT_FILLED_INSTANCE))
    assert ObjectHelper.isDictionaryClass(type(DICTIONARY_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(LIST_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(TUPLE_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(SET_FILLED_INSTANCE))
    assert not ObjectHelper.isDictionaryClass(type(GENERATOR_INSTANCE))

    assert ObjectHelper.isNotDictionaryClass(type(STR_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(BOOLEAN_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(INTEGER_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(FLOAT_FILLED_INSTANCE))
    assert not ObjectHelper.isNotDictionaryClass(type(DICTIONARY_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(LIST_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(TUPLE_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(SET_FILLED_INSTANCE))
    assert ObjectHelper.isNotDictionaryClass(type(GENERATOR_INSTANCE))

    assert ObjectHelper.isNativeClass(type(STR_FILLED_INSTANCE))
    assert ObjectHelper.isNativeClass(type(BOOLEAN_FILLED_INSTANCE))
    assert ObjectHelper.isNativeClass(type(INTEGER_FILLED_INSTANCE))
    assert ObjectHelper.isNativeClass(type(FLOAT_FILLED_INSTANCE))
    assert not ObjectHelper.isNativeClass(type(DICTIONARY_FILLED_INSTANCE))
    assert not ObjectHelper.isNativeClass(type(LIST_FILLED_INSTANCE))
    assert not ObjectHelper.isNativeClass(type(TUPLE_FILLED_INSTANCE))
    assert not ObjectHelper.isNativeClass(type(SET_FILLED_INSTANCE))
    assert ObjectHelper.isNativeClass(type(GENERATOR_INSTANCE))

    assert not ObjectHelper.isNotNativeClass(type(STR_FILLED_INSTANCE))
    assert not ObjectHelper.isNotNativeClass(type(BOOLEAN_FILLED_INSTANCE))
    assert not ObjectHelper.isNotNativeClass(type(INTEGER_FILLED_INSTANCE))
    assert not ObjectHelper.isNotNativeClass(type(FLOAT_FILLED_INSTANCE))
    assert ObjectHelper.isNotNativeClass(type(DICTIONARY_FILLED_INSTANCE))
    assert ObjectHelper.isNotNativeClass(type(LIST_FILLED_INSTANCE))
    assert ObjectHelper.isNotNativeClass(type(TUPLE_FILLED_INSTANCE))
    assert ObjectHelper.isNotNativeClass(type(SET_FILLED_INSTANCE))
    assert not ObjectHelper.isNotNativeClass(type(GENERATOR_INSTANCE))

    assert ObjectHelper.isNativeClassInstance(STR_FILLED_INSTANCE)
    assert ObjectHelper.isNativeClassInstance(BOOLEAN_FILLED_INSTANCE)
    assert ObjectHelper.isNativeClassInstance(INTEGER_FILLED_INSTANCE)
    assert ObjectHelper.isNativeClassInstance(FLOAT_FILLED_INSTANCE)
    assert not ObjectHelper.isNativeClassInstance(DICTIONARY_FILLED_INSTANCE)
    assert not ObjectHelper.isNativeClassInstance(LIST_FILLED_INSTANCE)
    assert not ObjectHelper.isNativeClassInstance(TUPLE_FILLED_INSTANCE)
    assert not ObjectHelper.isNativeClassInstance(SET_FILLED_INSTANCE)
    assert ObjectHelper.isNativeClassInstance(GENERATOR_INSTANCE)

    assert not ObjectHelper.isNotNativeClassIsntance(STR_FILLED_INSTANCE)
    assert not ObjectHelper.isNotNativeClassIsntance(BOOLEAN_FILLED_INSTANCE)
    assert not ObjectHelper.isNotNativeClassIsntance(INTEGER_FILLED_INSTANCE)
    assert not ObjectHelper.isNotNativeClassIsntance(FLOAT_FILLED_INSTANCE)
    assert ObjectHelper.isNotNativeClassIsntance(DICTIONARY_FILLED_INSTANCE)
    assert ObjectHelper.isNotNativeClassIsntance(LIST_FILLED_INSTANCE)
    assert ObjectHelper.isNotNativeClassIsntance(TUPLE_FILLED_INSTANCE)
    assert ObjectHelper.isNotNativeClassIsntance(SET_FILLED_INSTANCE)
    assert not ObjectHelper.isNotNativeClassIsntance(GENERATOR_INSTANCE)

    assert ObjectHelper.isNone(None)
    assert not ObjectHelper.isNotNone(None)
    assert not ObjectHelper.isList(None)
    assert ObjectHelper.isNotList(None)
    assert not ObjectHelper.isSet(None)
    assert ObjectHelper.isNotSet(None)
    assert not ObjectHelper.isTuple(None)
    assert ObjectHelper.isNotTuple(None)
    assert not ObjectHelper.isDictionary(None)
    assert ObjectHelper.isNotDictionary(None)
    assert not ObjectHelper.isCollection(None)
    assert ObjectHelper.isNotCollection(None)
    assert not ObjectHelper.isDictionaryClass(None)
    assert ObjectHelper.isNotDictionaryClass(None)
    assert not ObjectHelper.isNativeClass(None)
    assert ObjectHelper.isNotNativeClass(None)
    assert not ObjectHelper.isNativeClassInstance(None)
    assert ObjectHelper.isNotNativeClassIsntance(None)

    assert not ObjectHelper.isNone(type(None))
    assert ObjectHelper.isNotNone(type(None))
    assert not ObjectHelper.isList(type(None))
    assert ObjectHelper.isNotList(type(None))
    assert not ObjectHelper.isDictionary(type(None))
    assert ObjectHelper.isNotDictionary(type(None))
    assert not ObjectHelper.isCollection(type(None))
    assert ObjectHelper.isNotCollection(type(None))
    assert not ObjectHelper.isDictionaryClass(type(None))
    assert ObjectHelper.isNotDictionaryClass(type(None))
    assert not ObjectHelper.isNativeClass(type(None))
    assert ObjectHelper.isNotNativeClass(type(None))
    assert not ObjectHelper.isNativeClassInstance(type(None))
    assert ObjectHelper.isNotNativeClassIsntance(type(None))

@Test(
    environmentVariables={**{}, **LOG_HELPER_SETTINGS},
    **TEST_SETTINGS
)
def mustAssertEquals() :
    # arrange
    dictionaryInstance = {**{},**JSON_INSTANCE}
    someDictionary = {
        'a' : 'b',
        'c' : 'd',
        'e' : {
            'f' : 'g',
            't' : [
                {
                    's1',
                    's1',
                    's3',
                    1,
                    3.3,
                    False,
                    None
                },
                {
                    's1',
                    False,
                    's3',
                    3.3,
                    1,
                    None
                }
            ],
            1 : 7,
            False : 2.3
        },
        2.2 : {
            False,
            2,
            None,
            'string'
        },
        'tuple' : (
            2,
            3,
            '3',
            9
        )
    }
    someDictionaryList = [
        someDictionary,
        someDictionary
    ]
    someOtherDictionary = {
        'c' : 'd',
        'a' : 'b',
        'e' : {
            False : 2.3,
            1 : 7,
            'f' : 'g',
            't' : [
                {
                    3.3,
                    's1',
                    's3',
                    1,
                    None,
                    False
                },
                {
                    's1',
                    's1',
                    's3',
                    None,
                    1,
                    3.3,
                    False
                }
            ]
        },
        2.2 : {
            False,
            2,
            None,
            'string'
        },
        'tuple' : (
            2,
            9,
            3,
            '3'
        )
    }
    someOtherDictionaryList = [
        someOtherDictionary,
        someOtherDictionary
    ]
    differentDictionary = {
        'c' : 'd',
        'a' : 'b',
        'e' : {
            False : 2.3,
            1 : 7,
            'f' : 'g',
            't' : [
                {
                    's1',
                    's3',
                    1,
                    3.3,
                    False,
                    None
                },
                {
                    's1',
                    's1',
                    's3',
                    1,
                    3.3,
                    False,
                    None
                }
            ]
        },
        2.2 : {
            False,
            2,
            None,
            str()
        },
        'tuple' : (
            9,
            2,
            3,
            '3'
        )
    }
    differentDictionaryList = [
        differentDictionary,
        differentDictionary
    ]
    aList = [
        {
            'beginAtDate': '2021-03-11',
            'beginAtDatetime': '2021-03-11 08:30:00',
            'beginAtTime': '08:30:00',
            'endAtDate': '2021-03-11',
            'endAtDatetime': '2021-03-11 08:30:00',
            'endAtTime': '08:30:00',
            'id': None,
            'intervalTime': '2021-03-11 08:30:00',
            'timedelta': '08:30:00'
        },
        {
            'beginAtDate': '2021-03-11',
            'beginAtDatetime': '2021-03-11 08:30:00',
            'beginAtTime': '08:30:00',
            'endAtDate': '2021-03-11',
            'endAtDatetime': '2021-03-11 08:30:00',
            'endAtTime': '08:30:00',
            'id': None,
            'intervalTime': '2021-03-11 08:30:00',
            'timedelta': '08:30:00'
        }
    ]
    bList = [
        {
            'beginAtDate': '2021-03-11',
            'beginAtDatetime': '2021-03-11 08:30:00',
            'beginAtTime': '08:30:00',
            'endAtDate': '2021-03-11',
            'endAtDatetime': '2021-03-11 08:30:00',
            'endAtTime': '08:30:00',
            'id': None,
            'intervalTime': '2021-03-11 08:30:00',
            'timedelta': '8:30:00'
        },
        {
            'beginAtDate': '2021-03-11',
            'beginAtDatetime': '2021-03-11 08:30:00',
            'beginAtTime': '08:30:00',
            'endAtDate': '2021-03-11',
            'endAtDatetime': '2021-03-11 08:30:00',
            'endAtTime': '08:30:00',
            'id': None,
            'intervalTime': '2021-03-11 08:30:00',
            'timedelta': '8:30:00'
        }
    ]

    # act
    toAssert = ObjectHelper.equals(dictionaryInstance, JSON_INSTANCE, ignoreCharactereList=[Constant.NEW_LINE])
    unsortedDictionaryToAssert = ObjectHelper.equals(someDictionary, someOtherDictionary)
    unsortedDictionaryListToAssert = ObjectHelper.equals(someDictionaryList, someOtherDictionaryList)
    notEqualsToAssert = ObjectHelper.equals(someDictionary, differentDictionary)
    notEqualsListToAssert = ObjectHelper.equals(someDictionaryList, differentDictionaryList)

    # assert
    assert toAssert
    assert unsortedDictionaryToAssert
    assert not notEqualsToAssert
    assert unsortedDictionaryListToAssert
    assert not notEqualsListToAssert
    assert not ObjectHelper.equals(aList, bList)
    assert ObjectHelper.equals(aList, bList, ignoreKeyList = ['timedelta'])

@Test(
    environmentVariables={**{}, **LOG_HELPER_SETTINGS},
    **TEST_SETTINGS
)
def mustIgnoreKeyCorrectly() :
    # arrange
    expected = {**{},**DICTIONARY_INSTANCE}
    anotherDictionaryInstance = {**{},**DICTIONARY_INSTANCE}
    IGNORABLE_KEY = 'ignorableKey'
    anotherDictionaryInstance[IGNORABLE_KEY] = 'ignorableValue'

    # act
    toAssert = ObjectHelper.filterIgnoreKeyList(anotherDictionaryInstance,[IGNORABLE_KEY])

    # assert
    assert ObjectHelper.equals(expected, toAssert)

@Test(
    environmentVariables={**{}, **LOG_HELPER_SETTINGS},
    **TEST_SETTINGS
)
def equal_whenListOfDictionaries() :
    # arrange
    null = 'null'
    FIRST_DICT = {
        "myAttribute": "NW2",
        "myOther": {
            "myAttribute": "34PDZB"
        },
        "myThirdList": [
            {
                "my": {
                    "myAttribute": "X1HC",
                    "myOther": {
                        "myAttribute": "34PDZB"
                    },
                    "myThirdList": null
                },
                "myAttribute": 9
            }
        ]
    }
    SECOND_DICT = {
        "myAttribute": "",
        "myOther": null,
        "myThirdList": [
            {
                "my": {
                    "myAttribute": "U",
                    "myOther": null,
                    "myThirdList": null
                },
                "myAttribute": 3
            }
        ]
    }
    THIRD_DICT = {
        "myAttribute": "HNQ7QKW2",
        "myOther": {
            "myAttribute": "V9OXKD8"
        },
        "myThirdList": [
            {
                "my": {
                    "myAttribute": "PVYA",
                    "myOther": {
                        "myAttribute": "V9OXKD8"
                    },
                    "myThirdList": null
                },
                "myAttribute": 10
            }
        ]
    }
    LIST_OF_DICTIONARIES = [
        {**FIRST_DICT},
        {**SECOND_DICT},
        {**THIRD_DICT}
    ]
    DIFFERENT_LIST_OF_DICTIONARIES = [
        {
            "myAttribute": "NW2",
            "myOther": {
                "myAttribute": "34PDZB"
            },
            "myThirdList": [
                {
                    "my": {
                        "myAttribute": "X1HC",
                        "myOther": {
                            "myAttribute": RandomHelper.integer()
                        },
                        "myThirdList": null
                    },
                    "myAttribute": 9
                }
            ]
        },
        {**SECOND_DICT},
        {**THIRD_DICT}
    ]

    # act
    # assert
    assert ObjectHelper.equals(LIST_OF_DICTIONARIES, [
        {**FIRST_DICT},
        {**SECOND_DICT},
        {**THIRD_DICT}
    ])
    assert False == ObjectHelper.equals(LIST_OF_DICTIONARIES, [{}, {}, {}])
    assert False == ObjectHelper.equals(LIST_OF_DICTIONARIES, [SECOND_DICT, THIRD_DICT, FIRST_DICT])
    assert True == ObjectHelper.equals(LIST_OF_DICTIONARIES, [SECOND_DICT, THIRD_DICT, FIRST_DICT], ignoreCollectionOrder=True)
    assert False == ObjectHelper.equals(LIST_OF_DICTIONARIES, DIFFERENT_LIST_OF_DICTIONARIES)


@Test(
    environmentVariables={**{}, **LOG_HELPER_SETTINGS},
    **TEST_SETTINGS
)
def equal_whenObjects() :
    # arrange
    a = RandomHelper.string()
    b = RandomHelper.integer()
    c = RandomHelper.string()
    otherA = MyOtherDto(RandomHelper.string())
    otherB = MyOtherDto(RandomHelper.string())
    otherC = MyOtherDto(RandomHelper.string())
    myFirst = MyDto(None, None, None)
    mySecond = MyDto(None, None, None)
    myThird = MyDto(None, None, None)
    thirdOne = RandomHelper.integer()
    thirdTwo = RandomHelper.integer()
    thirdThree = RandomHelper.integer()
    myThirdOne = [MyThirdDto(myFirst, thirdOne)]
    myThirdTwo = [MyThirdDto(mySecond, thirdTwo)]
    myThirdThree = [MyThirdDto(myThird, thirdThree)]
    expected = [MyDto(a, otherA, myThirdOne), MyDto(b, otherB, myThirdTwo), MyDto(c, otherC, myThirdThree)]
    null = 'null'
    inspectEquals = False

    # act
    toAssert = [MyDto(a, otherA, myThirdOne), MyDto(b, otherB, myThirdTwo), MyDto(c, otherC, myThirdThree)]
    another = [MyDto(a, otherA, [MyThirdDto(myFirst, thirdOne)]), MyDto(b, otherB, myThirdTwo), MyDto(c, otherC, myThirdThree)]
    another[0].myThirdList[0].my = MyDto(
        MyDto(None, None, None),
        expected[0].myThirdList[0].my.myOther,
        expected[0].myThirdList[0].my.myThirdList
    )

    # assert
    assert False == (expected == toAssert) and isinstance(expected == toAssert, bool), f'False == ({expected} == {toAssert}): {False == (expected == toAssert)}'
    assert ObjectHelper.equals(expected, toAssert), f'ObjectHelper.equals({expected}, {toAssert}): {ObjectHelper.equals(expected, toAssert)}'
    assert ObjectHelper.equals(toAssert, expected), f'ObjectHelper.equals({toAssert}, {expected}): {ObjectHelper.equals(toAssert, expected)}'
    assert ObjectHelper.isNotNone(expected[0].myThirdList[0].my), expected[0].myThirdList[0].my
    assert expected[0].myThirdList[0].my == toAssert[0].myThirdList[0].my
    assert ObjectHelper.equals(expected[0].myThirdList[0].my, toAssert[0].myThirdList[0].my)
    assert ObjectHelper.isNone(expected[0].myThirdList[0].my.myThirdList)
    assert ObjectHelper.equals(expected[0].myThirdList[0].my.myThirdList, toAssert[0].myThirdList[0].my.myThirdList)
    assert ObjectHelper.equals(expected[1].myThirdList[0], toAssert[1].myThirdList[0])
    assert ObjectHelper.equals(toAssert[1].myThirdList[0], expected[1].myThirdList[0])
    assert False == (expected == another), f'False == ({expected} == {another}): False == {(expected == another)}'
    assert False == ObjectHelper.equals(expected, another, muteLogs=not inspectEquals)
    assert False == ObjectHelper.equals(another, expected, muteLogs=not inspectEquals)
    assert False == ObjectHelper.equals(another, toAssert, muteLogs=not inspectEquals)
    assert False == ObjectHelper.equals(toAssert, another, muteLogs=not inspectEquals)
    assert False == ObjectHelper.equals(expected, [MyDto(None, None, None), MyDto(None, None, None), MyDto(None, None, None)])
    assert ObjectHelper.equals(
        [
            MyDto(a, MyOtherDto(a), MyThirdDto(MyDto(a, MyOtherDto(a), [1, '1', 1.0]), thirdOne)),
            MyDto(b, MyOtherDto(b), MyThirdDto(MyDto(b, MyOtherDto(b), [2, '2', 2.0]), thirdTwo)),
            MyDto(c, MyOtherDto(c), MyThirdDto(MyDto(c, MyOtherDto(c), [3, '3', 3.0]), myThirdThree))
        ],
        [
            MyDto(a, MyOtherDto(a), MyThirdDto(MyDto(a, MyOtherDto(a), [1, '1', 1.0]), thirdOne)),
            MyDto(b, MyOtherDto(b), MyThirdDto(MyDto(b, MyOtherDto(b), [2, '2', 2.0]), thirdTwo)),
            MyDto(c, MyOtherDto(c), MyThirdDto(MyDto(c, MyOtherDto(c), [3, '3', 3.0]), myThirdThree))
        ]
    )
    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b)), bool)
    assert not ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b))
    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreKeyList=['myAttribute']), bool)
    assert not ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreKeyList=['myAttribute'])

    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreAttributeList=['myAttribute']), bool)
    assert ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreAttributeList=['myAttribute'])

    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[a, b]), bool)
    assert not ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[a, b])

    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[a]), bool)
    assert not ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[a])

    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[b]), bool)
    assert not ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[b])

    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreAttributeValueList=[a, b]), bool)
    assert ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreAttributeValueList=[a, b])

    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreAttributeValueList=[a]), bool)
    assert not ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreAttributeValueList=[a])

    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreAttributeValueList=[b]), bool)
    assert not ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreAttributeValueList=[b])

    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[a], ignoreAttributeValueList=[b]), bool)
    assert not ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[a], ignoreAttributeValueList=[b])

    assert isinstance(ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[b], ignoreAttributeValueList=[a]), bool)
    assert not ObjectHelper.equals(MyOtherDto(a), MyOtherDto(b), ignoreCharactereList=[b], ignoreAttributeValueList=[a])


@Test()
def equal_whenDictionary() :
    #arrange
    firstDict = {'b': 'c', 'a': 'd'}
    secondDict = {'a': 'd', 'b': 'c'}

    #act
    firstDictSorted = ObjectHelper.sortIt(firstDict)
    secondDictSorted = ObjectHelper.sortIt(secondDict)

    #assert
    assert firstDictSorted == secondDictSorted, f'{firstDictSorted} == {secondDictSorted}: {firstDictSorted == secondDictSorted}'
    assert ObjectHelper.equals(firstDictSorted, secondDictSorted), f'{firstDictSorted} == {secondDictSorted}: {firstDictSorted == secondDictSorted}'


@Test()
def equal_whenSets() :
    #arrange
    firstSet = {'b', 'c', 'a', 'd'}
    secondSet = {'a', 'd', 'b', 'c'}
    thirdSet = {'1', '2', '3', '4'}
    myFirstList = [
        firstSet,
        secondSet,
        thirdSet
    ]
    mySecondList = [
        thirdSet,
        firstSet,
        secondSet
    ]


    #act
    firstSetSorted = ObjectHelper.sortIt(firstSet)
    secondSetSorted = ObjectHelper.sortIt(secondSet)

    #assert
    assert ObjectHelper.equals(firstSetSorted, secondSetSorted), f'{firstSetSorted} == {secondSetSorted}: {firstSetSorted == secondSetSorted}'
    assert ObjectHelper.equals(firstSet, secondSet), f'{firstSetSorted} == {secondSetSorted}'
    assert not ObjectHelper.equals(myFirstList, mySecondList), f'{myFirstList} == {mySecondList}'
    assert ObjectHelper.equals(myFirstList, mySecondList, ignoreCollectionOrder=True), f'{myFirstList} == {mySecondList}'


# @Test()
# def equal_whenRecursive() :
#     #arrange
#     firstSet = {'b', 'c', 'a', 'd'}
#     secondSet = {'a', 'd', 'b', 'c'}
#     thirdSet = {'1', '2', '3', '4'}
#     myFirstList = [
#         firstSet,
#         secondSet,
#         thirdSet
#     ]
#     mySecondList = [
#         thirdSet,
#         firstSet,
#         secondSet
#     ]
#     firstInstance = {
#         1 : {str(mySecondList), str(myFirstList), str(myFirstList)},
#         2 : [myFirstList, mySecondList, myFirstList],
#         3 : {str(myFirstList), str(myFirstList), str(mySecondList)},
#         4 : [myFirstList, mySecondList, myFirstList]
#     }
#     secondInstance = {
#         1 : {str(myFirstList), str(mySecondList), str(myFirstList)},
#         2 : [myFirstList, mySecondList, myFirstList],
#         3 : {str(myFirstList), str(mySecondList), str(myFirstList)},
#         4 : [myFirstList, mySecondList, myFirstList]
#     }
#     firstInstance['a'] = firstInstance
#     firstInstance['b'] = {
#         'f': [
#             [secondInstance, secondInstance, secondInstance],
#             [secondInstance, secondInstance, secondInstance],
#             [secondInstance, secondInstance, secondInstance]
#         ]
#     }
#     secondInstance['a'] = secondInstance
#     secondInstance['b'] = {
#         'f': [
#             [firstInstance, firstInstance, firstInstance],
#             [firstInstance, firstInstance, firstInstance],
#             [firstInstance, firstInstance, firstInstance]
#         ]
#     }
#
#     #act
#     #assert
#     assert ObjectHelper.equals(firstInstance, secondInstance)
