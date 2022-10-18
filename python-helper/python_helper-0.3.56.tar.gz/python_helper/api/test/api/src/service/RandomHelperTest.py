from python_helper import RandomHelper
from python_helper import SettingHelper, log, Test

# LOG_HELPER_SETTINGS = {
#     log.LOG : True,
#     log.SUCCESS : True,
#     log.SETTING : True,
#     log.DEBUG : True,
#     log.WARNING : True,
#     log.FAILURE : True,
#     log.WRAPPER : True,
#     log.ERROR : True,
    # log.TEST : False,
    # log.ENABLE_LOGS_WITH_COLORS : True,
#     SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
# }

LOG_HELPER_SETTINGS = {
    log.LOG : False,
    log.SUCCESS : False,
    log.SETTING : False,
    log.DEBUG : False,
    log.WARNING : False,
    log.FAILURE : False,
    log.WRAPPER : False,
    log.ERROR : False,
    log.TEST : False
}

TEST_SETTINGS = {}

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def sample_withSuccess() :
    # Arrange
    SAMPLE_SIZE = 2
    listColletcion = [
        RandomHelper.string(),
        RandomHelper.string(),
        RandomHelper.string(),
        RandomHelper.string(),
        RandomHelper.string()
    ]
    tupleColletcion = (
        RandomHelper.string(),
        RandomHelper.string(),
        RandomHelper.string(),
        RandomHelper.string(),
        RandomHelper.string()
    )
    setColletcion = {
        RandomHelper.string(minimum=1),
        RandomHelper.string(minimum=1),
        RandomHelper.string(minimum=1),
        RandomHelper.string(minimum=1),
        RandomHelper.string(minimum=1)
    }
    dictionaryColletcion = {
        RandomHelper.string(minimum=1) : RandomHelper.string(),
        RandomHelper.string(minimum=1) : RandomHelper.string(),
        RandomHelper.string(minimum=1) : RandomHelper.string(),
        RandomHelper.string(minimum=1) : RandomHelper.string(),
        RandomHelper.string(minimum=1) : RandomHelper.string(),
    }

    # Act
    listElement = RandomHelper.sample(listColletcion)
    listSample = RandomHelper.sample(listColletcion, length=SAMPLE_SIZE)
    tupleElement = RandomHelper.sample(tupleColletcion)
    tupleSample = RandomHelper.sample(tupleColletcion, length=SAMPLE_SIZE)
    setElement = RandomHelper.sample(setColletcion)
    setSample = RandomHelper.sample(setColletcion, length=SAMPLE_SIZE)
    dictionaryElement = RandomHelper.sample(dictionaryColletcion)
    dictionarySample = RandomHelper.sample(dictionaryColletcion, length=SAMPLE_SIZE)

    # Assert
    assert listElement in listColletcion
    assert list == type(listSample)
    assert SAMPLE_SIZE == len(listSample)
    for element in listSample :
        assert element in listColletcion
    assert tupleElement in tupleColletcion
    assert tuple == type(tupleSample)
    assert SAMPLE_SIZE == len(tupleSample)
    for element in tupleSample :
        assert element in tupleColletcion
    assert setElement in setColletcion
    assert set == type(setSample)
    assert SAMPLE_SIZE == len(setSample)
    for element in setSample :
        assert element in setColletcion
    assert 1 == len(dictionaryElement.keys())
    assert list(dictionaryElement.keys())[0] in dictionaryColletcion
    assert dict == type(dictionarySample)
    assert SAMPLE_SIZE == len(dictionarySample)
    for key in dictionarySample :
        assert key in dictionaryColletcion
        assert dictionarySample[key] == dictionaryColletcion[key]

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def randomValues() :
    # Arrange
    MINIMUM_CUSTOM_RANGE = 30
    MAXIMUM_CUSTOM_RANGE = 10
    OTHER_MINIMUM_CUSTOM_RANGE = 100
    OTHER_MAXIMUM_CUSTOM_RANGE = 200
    MINIMUM_CUSTOM_FLOAT_RANGE = 400.33
    MAXIMUM_CUSTOM_FLOAT_RANGE = 500.55

    # Act
    stringValueInDefaultRange = RandomHelper.string()
    stringValueInCustomRange = RandomHelper.string(minimum=MINIMUM_CUSTOM_RANGE, maximum=MAXIMUM_CUSTOM_RANGE)
    stringValueInOtherCustomRange = RandomHelper.string(minimum=OTHER_MINIMUM_CUSTOM_RANGE, maximum=OTHER_MAXIMUM_CUSTOM_RANGE)
    integerValueInDefaultRange = RandomHelper.integer()
    integerValueInCustomRange = RandomHelper.integer(minimum=MINIMUM_CUSTOM_RANGE, maximum=MAXIMUM_CUSTOM_RANGE)
    integerValueInOtherCustomRange = RandomHelper.integer(minimum=OTHER_MINIMUM_CUSTOM_RANGE, maximum=OTHER_MAXIMUM_CUSTOM_RANGE)
    floatValueInDefaultRange = RandomHelper.float()
    floatValueInCustomRange = RandomHelper.float(minimum=MINIMUM_CUSTOM_RANGE, maximum=MAXIMUM_CUSTOM_RANGE)
    floatValueInOtherCustomRange = RandomHelper.float(minimum=OTHER_MINIMUM_CUSTOM_RANGE, maximum=OTHER_MAXIMUM_CUSTOM_RANGE)
    floatValueInOtherCustomFloatRange = RandomHelper.float(minimum=MINIMUM_CUSTOM_FLOAT_RANGE, maximum=MAXIMUM_CUSTOM_FLOAT_RANGE)

    # Assert
    assert RandomHelper.DEFAULT_MINIMUM_LENGHT <= len(stringValueInDefaultRange) <= RandomHelper.DEFAULT_MAXIMUM_LENGHT
    assert MINIMUM_CUSTOM_RANGE == len(stringValueInCustomRange)
    assert OTHER_MINIMUM_CUSTOM_RANGE <= len(stringValueInOtherCustomRange) <= OTHER_MAXIMUM_CUSTOM_RANGE
    assert RandomHelper.DEFAULT_MINIMUM_LENGHT <= integerValueInDefaultRange <= RandomHelper.DEFAULT_MAXIMUM_LENGHT
    assert MINIMUM_CUSTOM_RANGE == integerValueInCustomRange
    assert OTHER_MINIMUM_CUSTOM_RANGE <= integerValueInOtherCustomRange <= OTHER_MAXIMUM_CUSTOM_RANGE
    assert RandomHelper.DEFAULT_MINIMUM_LENGHT <= floatValueInDefaultRange <= RandomHelper.DEFAULT_MAXIMUM_LENGHT
    assert MINIMUM_CUSTOM_RANGE == floatValueInCustomRange
    assert OTHER_MINIMUM_CUSTOM_RANGE <= floatValueInOtherCustomRange < OTHER_MAXIMUM_CUSTOM_RANGE
    assert MINIMUM_CUSTOM_FLOAT_RANGE <= floatValueInOtherCustomFloatRange <= MAXIMUM_CUSTOM_FLOAT_RANGE
