from python_helper import log, SettingHelper, StringHelper, EnvironmentVariable, EnvironmentHelper, ObjectHelper, Test

class MyClass :
    def myMethod(self):
        self.me = 1
def myFunction(a):
    return str(a) + 'b'
OPTIONAL_EXCEPTION_LOG_TYPES = [log.log, log.debug, log.warning, log.test, log.wrapper]
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

TEST_SETTINGS = {}

@Test(
    environmentVariables={
        log.LOG : True,
        log.SUCCESS : True,
        log.SETTING : True,
        log.DEBUG : True,
        log.WARNING : True,
        log.WRAPPER : True,
        log.FAILURE : True,
        log.ERROR : True,
        log.TEST : True,
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
    },
    **TEST_SETTINGS
)
def mustLogWithColors() :
    # Arrange
    noExceptionThrown = 'exception not thrown'
    someLogMessage = 'some log message'
    someExceptionMessage = 'some exception message'
    someInnerExceptionMessage = 'some inner exception message'
    exception = None
    someExceptionMessageWithStackTrace = f'{someExceptionMessage} with stacktrace'
    someExceptionMessageWithoutStackTrace = f'{someExceptionMessage} without stacktrace'
    def controlableException(logType, muteStackTrace=False) :
        try :
            raise Exception(someExceptionMessageWithoutStackTrace if muteStackTrace else someExceptionMessageWithStackTrace)
        except Exception as exception :
            if logType in OPTIONAL_EXCEPTION_LOG_TYPES :
                logType(logType, someLogMessage, exception=exception, muteStackTrace=muteStackTrace)
            else :
                logType(logType, someLogMessage, exception, muteStackTrace=muteStackTrace)

    # Act
    log.info(log.info, someLogMessage)
    log.status(log.status, someLogMessage)
    log.success(log.success, someLogMessage)
    log.setting(log.setting, someLogMessage)
    log.debug(log.debug, someLogMessage)
    log.warning(log.warning, someLogMessage)

    controlableException(log.log)
    controlableException(log.debug)
    controlableException(log.warning)
    controlableException(log.wrapper)
    controlableException(log.failure)
    controlableException(log.error)
    controlableException(log.test)

    controlableException(log.log, muteStackTrace=True)
    controlableException(log.debug, muteStackTrace=True)
    controlableException(log.warning, muteStackTrace=True)
    controlableException(log.wrapper, muteStackTrace=True)
    controlableException(log.failure, muteStackTrace=True)
    controlableException(log.error, muteStackTrace=True)
    controlableException(log.test, muteStackTrace=True)

    log.log(log.log, someLogMessage, None)
    log.debug(log.debug, someLogMessage, None)
    log.warning(log.warning, someLogMessage, None)
    log.wrapper(log.wrapper, noExceptionThrown, None)
    log.failure(log.failure, noExceptionThrown, None)
    log.error(log.error, noExceptionThrown, None)
    log.test(log.test, someLogMessage, None)

    # Assert
    assert SettingHelper.LOCAL_ENVIRONMENT == EnvironmentHelper.get(SettingHelper.ACTIVE_ENVIRONMENT)
    assert SettingHelper.activeEnvironmentIsLocal()

@Test(
    environmentVariables={
        log.LOG : True,
        log.SUCCESS : True,
        log.SETTING : True,
        log.DEBUG : True,
        log.WARNING : True,
        log.WRAPPER : True,
        log.FAILURE : True,
        log.ERROR : True,
        log.TEST : True,
        log.ENABLE_LOGS_WITH_COLORS : False,
        SettingHelper.ACTIVE_ENVIRONMENT : 'my environment'
    },
    **TEST_SETTINGS
)
def mustLogWithoutColors() :
    # Arrange
    noExceptionThrown = 'exception not thrown'
    someLogMessage = 'some log message'
    someExceptionMessage = 'some exception message'
    someInnerExceptionMessage = 'some inner exception message'
    exception = None
    someExceptionMessageWithStackTrace = f'{someExceptionMessage} with stacktrace'
    someExceptionMessageWithoutStackTrace = f'{someExceptionMessage} without stacktrace'
    def controlableException(logType, muteStackTrace=False) :
        try :
            raise Exception(someExceptionMessageWithoutStackTrace if muteStackTrace else someExceptionMessageWithStackTrace)
        except Exception as exception :
            if logType in OPTIONAL_EXCEPTION_LOG_TYPES :
                logType(logType, someLogMessage, exception=exception, muteStackTrace=muteStackTrace)
            else :
                logType(logType, someLogMessage, exception, muteStackTrace=muteStackTrace)

    # Act
    log.info(log.info, someLogMessage)
    log.status(log.status, someLogMessage)
    log.success(log.success, someLogMessage)
    log.setting(log.setting, someLogMessage)
    log.debug(log.debug, someLogMessage)
    log.warning(log.warning, someLogMessage)

    controlableException(log.log)
    controlableException(log.debug)
    controlableException(log.warning)
    controlableException(log.wrapper)
    controlableException(log.failure)
    controlableException(log.error)
    controlableException(log.test)

    controlableException(log.log, muteStackTrace=True)
    controlableException(log.debug, muteStackTrace=True)
    controlableException(log.warning, muteStackTrace=True)
    controlableException(log.wrapper, muteStackTrace=True)
    controlableException(log.failure, muteStackTrace=True)
    controlableException(log.error, muteStackTrace=True)
    controlableException(log.test, muteStackTrace=True)

    log.log(log.log, someLogMessage, None)
    log.debug(log.debug, someLogMessage, None)
    log.warning(log.warning, someLogMessage, None)
    log.wrapper(log.wrapper, noExceptionThrown, None)
    log.failure(log.failure, noExceptionThrown, None)
    log.error(log.error, noExceptionThrown, None)
    log.test(log.test, someLogMessage, None)

    # Assert
    assert 'my environment' == EnvironmentHelper.get(SettingHelper.ACTIVE_ENVIRONMENT)

@Test(
    environmentVariables={
        log.LOG : True,
        log.SUCCESS : True,
        log.SETTING : True,
        log.DEBUG : True,
        log.WARNING : True,
        log.WRAPPER : True,
        log.FAILURE : True,
        log.ERROR : True,
        log.TEST : False,
        log.ENABLE_LOGS_WITH_COLORS : None,
        SettingHelper.ACTIVE_ENVIRONMENT : None
    },
    **TEST_SETTINGS
)
def mustLogWithoutColorsAsWell() :
    # Arrange
    noExceptionThrown = 'exception not thrown'
    someLogMessage = 'some log message'
    someExceptionMessage = 'some exception message'
    someInnerExceptionMessage = 'some inner exception message'
    exception = None
    someExceptionMessageWithStackTrace = f'{someExceptionMessage} with stacktrace'
    someExceptionMessageWithoutStackTrace = f'{someExceptionMessage} without stacktrace'
    def controlableException(logType, muteStackTrace=False) :
        try :
            raise Exception(someExceptionMessageWithoutStackTrace if muteStackTrace else someExceptionMessageWithStackTrace)
        except Exception as exception :
            if logType in OPTIONAL_EXCEPTION_LOG_TYPES :
                logType(logType, someLogMessage, exception=exception, muteStackTrace=muteStackTrace)
            else :
                logType(logType, someLogMessage, exception, muteStackTrace=muteStackTrace)

    # Act
    log.info(log.info, someLogMessage)
    log.status(log.status, someLogMessage)
    log.success(log.success, someLogMessage)
    log.setting(log.setting, someLogMessage)
    log.debug(log.debug, someLogMessage)
    log.warning(log.warning, someLogMessage)

    controlableException(log.log)
    controlableException(log.debug)
    controlableException(log.warning)
    controlableException(log.wrapper)
    controlableException(log.failure)
    controlableException(log.error)
    controlableException(log.test)

    controlableException(log.log, muteStackTrace=True)
    controlableException(log.debug, muteStackTrace=True)
    controlableException(log.warning, muteStackTrace=True)
    controlableException(log.wrapper, muteStackTrace=True)
    controlableException(log.failure, muteStackTrace=True)
    controlableException(log.error, muteStackTrace=True)
    controlableException(log.test, muteStackTrace=True)

    log.log(log.log, noExceptionThrown, None)
    log.debug(log.debug, noExceptionThrown, None)
    log.warning(log.warning, noExceptionThrown, None)
    log.wrapper(log.wrapper, noExceptionThrown, None)
    log.failure(log.failure, noExceptionThrown, None)
    log.error(log.error, noExceptionThrown, None)
    log.test(log.test, noExceptionThrown, None)

    # Assert
    assert True == SettingHelper.activeEnvironmentIsDefault()
    assert SettingHelper.DEFAULT_ENVIRONMENT == EnvironmentHelper.get(SettingHelper.ACTIVE_ENVIRONMENT)
    assert SettingHelper.DEFAULT_ENVIRONMENT == SettingHelper.getActiveEnvironment()

@Test(
    environmentVariables={
        log.LOG : False,
        log.SUCCESS : True,
        log.SETTING : True,
        log.DEBUG : False,
        log.WARNING : False,
        log.WRAPPER : False,
        log.FAILURE : True,
        log.ERROR : True,
        log.TEST : False,
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        'SOME_PARTICULAR_SETTING' : '"some value"'
    },
    **TEST_SETTINGS
)
def mustLogEnvironmentSettings() :
    # Arrange

    # Act
    SettingHelper.logEnvironmentSettings()

    # Assert
    assert SettingHelper.LOCAL_ENVIRONMENT == EnvironmentHelper.get(SettingHelper.ACTIVE_ENVIRONMENT)
    assert SettingHelper.LOCAL_ENVIRONMENT == SettingHelper.getActiveEnvironment()
    assert SettingHelper.activeEnvironmentIsLocal()
    assert "some value" == EnvironmentHelper.get('SOME_PARTICULAR_SETTING')

@Test(
    environmentVariables={
        log.LOG : True,
        log.SUCCESS : True,
        log.SETTING : True,
        log.DEBUG : True,
        log.WARNING : True,
        log.WRAPPER : True,
        log.FAILURE : True,
        log.ERROR : True,
        log.TEST : False,
        log.ENABLE_LOGS_WITH_COLORS : False,
        SettingHelper.ACTIVE_ENVIRONMENT : None
    },
    **TEST_SETTINGS
)
def mustLogPretyPythonWithoutColors() :
    # Arrange
    dictionaryInstance = {**{}, **DICTIONARY_INSTANCE}
    exception = None

    # Act
    try :
        log.prettyPython(mustLogPretyPythonWithoutColors, 'prettyPythonWithoutColors', dictionaryInstance)
    except Exception as e :
        log.failure(mustLogPretyPythonWithoutColors, 'Failed to log prety python in this method call', e)
        exception = e

    # Assert
    assert ObjectHelper.isNone(exception)

@Test(
    environmentVariables={
        log.LOG : True,
        log.SUCCESS : True,
        log.SETTING : True,
        log.DEBUG : True,
        log.WARNING : True,
        log.WRAPPER : True,
        log.FAILURE : True,
        log.ERROR : True,
        log.TEST : False,
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
    },
    **TEST_SETTINGS
)
def mustLogPretyPythonWithColors() :
    # Arrange
    # log.log(mustLogPretyPythonWithColors, f'type({MyClass}): {type(MyClass)}')
    # log.log(mustLogPretyPythonWithColors, f'type({MyClass}).__name__: {type(MyClass).__name__}')
    # log.log(mustLogPretyPythonWithColors, f'type({MyClass().myMethod}): {type(MyClass().myMethod)}')
    # log.log(mustLogPretyPythonWithColors, f'type({MyClass().myMethod}).__name__: {type(MyClass().myMethod).__name__}')
    # log.log(mustLogPretyPythonWithColors, f'type({myFunction}): {type(myFunction)}')
    # log.log(mustLogPretyPythonWithColors, f'type({myFunction}).__name__: {type(myFunction).__name__}')
    # log.log(mustLogPretyPythonWithColors, f'type({log}): {type(log)}')
    # log.log(mustLogPretyPythonWithColors, f'type({log}).__name__: {type(log).__name__}')
    dictionaryInstance = {
        **{
            'class' : MyClass,
            'method' : MyClass().myMethod,
            'value' : MyClass().myMethod(),
            'function' : myFunction,
            'otherValue' : myFunction(1.1),
            'module' : log
        },
        **DICTIONARY_INSTANCE
    }
    exception = None

    # Act
    try :
        log.prettyPython(mustLogPretyPythonWithColors, 'prettyPython', dictionaryInstance)
    except Exception as e :
        log.failure(mustLogPretyPythonWithColors, 'Failed to log prety python in this method call', e)
        exception = e

    # Assert
    assert ObjectHelper.isNone(exception)

@Test(
    environmentVariables={
        log.LOG : True,
        log.SUCCESS : True,
        log.SETTING : True,
        log.DEBUG : True,
        log.WARNING : True,
        log.WRAPPER : True,
        log.FAILURE : True,
        log.ERROR : True,
        log.TEST : False,
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
    },
    **TEST_SETTINGS
)
def mustLogPretyJsonWithColors() :
    # Arrange
    # log.log(mustLogPretyPythonWithColors, f'type({MyClass}): {type(MyClass)}')
    # log.log(mustLogPretyPythonWithColors, f'type({MyClass}).__name__: {type(MyClass).__name__}')
    # log.log(mustLogPretyPythonWithColors, f'type({MyClass().myMethod}): {type(MyClass().myMethod)}')
    # log.log(mustLogPretyPythonWithColors, f'type({MyClass().myMethod}).__name__: {type(MyClass().myMethod).__name__}')
    # log.log(mustLogPretyPythonWithColors, f'type({myFunction}): {type(myFunction)}')
    # log.log(mustLogPretyPythonWithColors, f'type({myFunction}).__name__: {type(myFunction).__name__}')
    # log.log(mustLogPretyPythonWithColors, f'type({log}): {type(log)}')
    # log.log(mustLogPretyPythonWithColors, f'type({log}).__name__: {type(log).__name__}')
    dictionaryInstance = {
        **{
            'class' : MyClass,
            'method' : MyClass().myMethod,
            'value' : MyClass().myMethod(),
            'function' : myFunction,
            'otherValue' : myFunction(1.1),
            'module' : log
        },
        **DICTIONARY_INSTANCE
    }
    exception = None

    # Act
    try :
        log.prettyJson(mustLogPretyJsonWithColors, 'prettyJson', dictionaryInstance)
    except Exception as e :
        log.failure(mustLogPretyJsonWithColors, 'Failed to log prety json in this method call', e)
        exception = e

    # Assert
    assert ObjectHelper.isNone(exception)

@Test(
    environmentVariables={
        log.LOG : True,
        log.SUCCESS : True,
        log.SETTING : True,
        log.DEBUG : True,
        log.WARNING : True,
        log.WRAPPER : True,
        log.FAILURE : True,
        log.ERROR : True,
        log.TEST : True,
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT
    },
    **TEST_SETTINGS
)
def mustPrintMessageLog_withColors() :
    # Arrange
    mustLogWithNewLine = 'must log with new line'
    mustNotLogWithNewLine = 'must not log with new line'
    mustLogWithoutNewLine = 'must log without new line'
    mustNotLogWithoutNewLine = 'must not log without new line'
    mustLogWithNewLineWithException = 'must log with new line with exception'
    mustNotLogWithNewLineWithException = 'must not log with new line with exception'
    mustLogWithoutNewLineWithException = 'must log without new line with exception'
    mustNotLogWithoutNewLineWithException = 'must not log without new line with exception'
    someExceptionMessage = 'some exception message'
    thrownException = None
    try :
        raise Exception(someExceptionMessage)
    except Exception as exception :
        thrownException = exception

    # Act
    log.printLog(mustLogWithNewLine, condition=True, newLine=True)
    log.printInfo(mustLogWithNewLine, condition=True, newLine=True)
    log.printStatus(mustLogWithNewLine, condition=True, newLine=True)
    log.printSuccess(mustLogWithNewLine, condition=True, newLine=True)
    log.printSetting(mustLogWithNewLine, condition=True, newLine=True)
    log.printDebug(mustLogWithNewLine, condition=True, newLine=True, exception=None)
    log.printWarning(mustLogWithNewLine, condition=True, newLine=True, exception=None)
    log.printWarper(mustLogWithNewLine, condition=True, newLine=True, exception=None)
    log.printFailure(mustLogWithNewLine, condition=True, newLine=True, exception=None)
    log.printError(mustLogWithNewLine, condition=True, newLine=True, exception=None)
    log.printTest(mustLogWithNewLine, condition=True, newLine=True, exception=None)

    log.printLog(mustNotLogWithNewLine, condition=False, newLine=True)
    log.printInfo(mustNotLogWithNewLine, condition=False, newLine=True)
    log.printStatus(mustNotLogWithNewLine, condition=False, newLine=True)
    log.printSuccess(mustNotLogWithNewLine, condition=False, newLine=True)
    log.printSetting(mustNotLogWithNewLine, condition=False, newLine=True)
    log.printDebug(mustNotLogWithNewLine, condition=False, newLine=True, exception=None)
    log.printWarning(mustNotLogWithNewLine, condition=False, newLine=True, exception=None)
    log.printWarper(mustNotLogWithNewLine, condition=False, newLine=True, exception=None)
    log.printFailure(mustNotLogWithNewLine, condition=False, newLine=True, exception=None)
    log.printError(mustNotLogWithNewLine, condition=False, newLine=True, exception=None)
    log.printTest(mustNotLogWithNewLine, condition=False, newLine=True, exception=None)

    log.printLog(mustLogWithoutNewLine, condition=True, newLine=False)
    log.printInfo(mustLogWithoutNewLine, condition=True, newLine=False)
    log.printStatus(mustLogWithoutNewLine, condition=True, newLine=False)
    log.printSuccess(mustLogWithoutNewLine, condition=True, newLine=False)
    log.printSetting(mustLogWithoutNewLine, condition=True, newLine=False)
    log.printDebug(mustLogWithoutNewLine, condition=True, newLine=False, exception=None)
    log.printWarning(mustLogWithoutNewLine, condition=True, newLine=False, exception=None)
    log.printWarper(mustLogWithoutNewLine, condition=True, newLine=False, exception=None)
    log.printFailure(mustLogWithoutNewLine, condition=True, newLine=False, exception=None)
    log.printError(mustLogWithoutNewLine, condition=True, newLine=False, exception=None)
    log.printTest(mustLogWithoutNewLine, condition=True, newLine=False, exception=None)

    log.printLog(mustNotLogWithoutNewLine, condition=False, newLine=False)
    log.printInfo(mustNotLogWithoutNewLine, condition=False, newLine=False)
    log.printStatus(mustNotLogWithoutNewLine, condition=False, newLine=False)
    log.printSuccess(mustNotLogWithoutNewLine, condition=False, newLine=False)
    log.printSetting(mustNotLogWithoutNewLine, condition=False, newLine=False)
    log.printDebug(mustNotLogWithoutNewLine, condition=False, newLine=False, exception=None)
    log.printWarning(mustNotLogWithoutNewLine, condition=False, newLine=False, exception=None)
    log.printWarper(mustNotLogWithoutNewLine, condition=False, newLine=False, exception=None)
    log.printFailure(mustNotLogWithoutNewLine, condition=False, newLine=False, exception=None)
    log.printError(mustNotLogWithoutNewLine, condition=False, newLine=False, exception=None)
    log.printTest(mustNotLogWithoutNewLine, condition=False, newLine=False, exception=None)

    log.printLog(mustLogWithNewLineWithException, condition=True, newLine=True, exception=thrownException)
    log.printDebug(mustLogWithNewLineWithException, condition=True, newLine=True, exception=thrownException)
    log.printWarning(mustLogWithNewLineWithException, condition=True, newLine=True, exception=thrownException)
    log.printWarper(mustLogWithNewLineWithException, condition=True, newLine=True, exception=thrownException)
    log.printFailure(mustLogWithNewLineWithException, condition=True, newLine=True, exception=thrownException)
    log.printError(mustLogWithNewLineWithException, condition=True, newLine=True, exception=thrownException)
    log.printTest(mustLogWithNewLineWithException, condition=True, newLine=True, exception=thrownException)

    log.printLog(mustLogWithoutNewLineWithException, condition=True, newLine=False, exception=thrownException)
    log.printDebug(mustLogWithoutNewLineWithException, condition=True, newLine=False, exception=thrownException)
    log.printWarning(mustLogWithoutNewLineWithException, condition=True, newLine=False, exception=thrownException)
    log.printWarper(mustLogWithoutNewLineWithException, condition=True, newLine=False, exception=thrownException)
    log.printFailure(mustLogWithoutNewLineWithException, condition=True, newLine=False, exception=thrownException)
    log.printError(mustLogWithoutNewLineWithException, condition=True, newLine=False, exception=thrownException)
    log.printTest(mustLogWithoutNewLineWithException, condition=True, newLine=False, exception=thrownException)

    log.printLog(mustNotLogWithNewLineWithException, condition=False, newLine=True, exception=thrownException)
    log.printDebug(mustNotLogWithNewLineWithException, condition=False, newLine=True, exception=thrownException)
    log.printWarning(mustNotLogWithNewLineWithException, condition=False, newLine=True, exception=thrownException)
    log.printWarper(mustNotLogWithNewLineWithException, condition=False, newLine=True, exception=thrownException)
    log.printFailure(mustNotLogWithNewLineWithException, condition=False, newLine=True, exception=thrownException)
    log.printError(mustNotLogWithNewLineWithException, condition=False, newLine=True, exception=thrownException)
    log.printTest(mustNotLogWithNewLineWithException, condition=False, newLine=True, exception=thrownException)

    log.printLog(mustNotLogWithoutNewLineWithException, condition=False, newLine=False, exception=thrownException)
    log.printDebug(mustNotLogWithoutNewLineWithException, condition=False, newLine=False, exception=thrownException)
    log.printWarning(mustNotLogWithoutNewLineWithException, condition=False, newLine=False, exception=thrownException)
    log.printWarper(mustNotLogWithoutNewLineWithException, condition=False, newLine=False, exception=thrownException)
    log.printFailure(mustNotLogWithoutNewLineWithException, condition=False, newLine=False, exception=thrownException)
    log.printError(mustNotLogWithoutNewLineWithException, condition=False, newLine=False, exception=thrownException)
    log.printTest(mustNotLogWithoutNewLineWithException, condition=False, newLine=False, exception=thrownException)

    # Assert
    assert True == SettingHelper.activeEnvironmentIsLocal()
    assert SettingHelper.LOCAL_ENVIRONMENT == EnvironmentHelper.get(SettingHelper.ACTIVE_ENVIRONMENT)
    assert SettingHelper.LOCAL_ENVIRONMENT == SettingHelper.getActiveEnvironment()
