from python_helper import SettingHelper, StringHelper, Constant, log, EnvironmentHelper, ObjectHelper, Test, RandomHelper

UNMUTED_LOG_HELPER_SETTINGS = {
    log.LOG : True,
    log.SUCCESS : True,
    log.SETTING : True,
    log.DEBUG : True,
    log.WARNING : True,
    log.WRAPPER : True,
    log.FAILURE : True,
    log.ERROR : True,
    log.TEST : False
}

MUTED_LOG_HELPER_SETTINGS = {
    log.LOG : False,
    log.SUCCESS : False,
    log.SETTING : False,
    log.DEBUG : False,
    log.WARNING : False,
    log.WRAPPER : False,
    log.FAILURE : False,
    log.ERROR : False,
    log.TEST : False
}

TEST_SETTINGS = {
    'inspectGlobals' : False,
    'logResult' : True
}

@Test(
    environmentVariables = {
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withSuccess() :
    # Arrange
    def myFunction(a):
        return a
    @Test(environmentVariables={
        SettingHelper.ACTIVE_ENVIRONMENT : None,
        **MUTED_LOG_HELPER_SETTINGS
    })
    def myTest() :
        a = 'original a'
        originalA = str(a) + ''
        b = myFunction(a)
        assert originalA == b
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert myFunction('original a') == str('original a')+''
    assert exception is None

@Test(
    environmentVariables = {
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withFailure() :
    # Arrange
    def myFunction(a):
        return a
    @Test(environmentVariables={
        SettingHelper.ACTIVE_ENVIRONMENT : None,
        **MUTED_LOG_HELPER_SETTINGS
    })
    def myTest() :
        assert 'b' == 'a'
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert exception is not None

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withSuccess_ExecutingActionFirst() :
    # Arrange
    def myAction(c, d=None):
        return c+d
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callBefore=myAction,
        argsOfCallBefore='f',
        kwargsOfCallBefore={'d':'g'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        assert 'a' == myFunction('a')
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert ObjectHelper.isNone(exception)
    assert 'fg' == returns['returnOfCallBefore']

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withFailre_ExecutingActionFirst() :
    # Arrange
    def myAction(c, d=None):
        return c+d
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callBefore=myAction,
        argsOfCallBefore='f',
        kwargsOfCallBefore={'d':'g'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        assert 'a' == myFunction('b')
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert ObjectHelper.isNotNone(exception)
    assert 'fg' == returns['returnOfCallBefore']

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withSuccess_ExecutingActionFirst_withFailure() :
    # Arrange
    exceptionMessage = 'some exception'
    def myAction(c, d=None):
        raise Exception(exceptionMessage)
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callBefore=myAction,
        argsOfCallBefore='f',
        kwargsOfCallBefore={'d':'g'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        assert 'a' == myFunction('a')
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert ObjectHelper.isNotNone(exception)
    assert exceptionMessage == str(exception)

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withFailre_ExecutingActionFirst_withFailre() :
    # Arrange
    exceptionMessage = 'some exception'
    def myAction(c, d=None):
        raise Exception(exceptionMessage)
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callBefore=myAction,
        argsOfCallBefore='f',
        kwargsOfCallBefore={'d':'g'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        assert 'a' == myFunction('b')
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert ObjectHelper.isNotNone(exception)
    assert exceptionMessage == str(exception)

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withSuccess_ExecutingActionLater() :
    # Arrange
    def myAction(c, d=None):
        return c+d
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callAfter=myAction,
        argsOfCallAfter='f',
        kwargsOfCallAfter={'d':'g'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        assert 'a' == myFunction('a')
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert ObjectHelper.isNone(exception)
    assert 'fg' == returns['returnOfCallAfter']

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withFailre_ExecutingActionLater() :
    # Arrange
    def myAction(c, d=None):
        return c+d
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callAfter=myAction,
        argsOfCallAfter='f',
        kwargsOfCallAfter={'d':'g'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        assert 'a' == myFunction('b')
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert ObjectHelper.isNotNone(exception)
    assert 'fg' == returns['returnOfCallAfter']

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withSuccess_ExecutingActionLater_withFailure() :
    # Arrange
    exceptionMessage = 'some exception'
    def myAction(c, d=None):
        raise Exception(exceptionMessage)
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callAfter=myAction,
        argsOfCallAfter='f',
        kwargsOfCallAfter={'d':'g'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        assert 'a' == myFunction('a')
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert ObjectHelper.isNotNone(exception)
    assert exceptionMessage == str(exception)

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def mustRun_withFailre_ExecutingActionLater_withFailre() :
    # Arrange
    exceptionMessage = 'some exception'
    def myAction(c, d=None):
        raise Exception(exceptionMessage)
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callAfter=myAction,
        argsOfCallAfter='f',
        kwargsOfCallAfter={'d':'g'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        assert 'a' == myFunction('b')
    exception = None

    # Act
    try :
        myTest()
    except Exception as e :
        exception = e

    # Assert
    assert ObjectHelper.isNotNone(exception)
    assert not exceptionMessage == str(exception)
    assert 'AssertionError. Followed by: some exception' == str(exception)

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def handleEnvironmentChangesProperly_withSuccess() :
    beforeTestEnvironmentSettings = {**EnvironmentHelper.getSet()}
    inBetweenTestEnvironmentSettings = None
    afterTestEnvironmentSettings = None
    # Arrange
    def myBeforeAction(c, d=None):
        return d+c
    def myAfterAction(c, d=None):
        return c+d
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callBefore=myBeforeAction,
        argsOfCallBefore='f',
        kwargsOfCallBefore={'d':'g'},
        callAfter=myAfterAction,
        argsOfCallAfter='h',
        kwargsOfCallAfter={'d':'i'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        inBetweenTestEnvironmentSettings = EnvironmentHelper.getSet()
        assert ObjectHelper.isNotNone(inBetweenTestEnvironmentSettings)
        assert ObjectHelper.isDictionary(inBetweenTestEnvironmentSettings)
        assert 'a' == myFunction('a')
        return inBetweenTestEnvironmentSettings

    # Act
    inBetweenTestEnvironmentSettings = myTest()
    afterTestEnvironmentSettings = {**EnvironmentHelper.getSet()}

    # Assert
    assert 'gf' == returns['returnOfCallBefore']
    assert 'hi' == returns['returnOfCallAfter']
    assert ObjectHelper.isNotNone(beforeTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(beforeTestEnvironmentSettings)
    assert ObjectHelper.isNotNone(inBetweenTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(inBetweenTestEnvironmentSettings)
    assert ObjectHelper.isNotNone(afterTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(afterTestEnvironmentSettings)
    assert afterTestEnvironmentSettings == beforeTestEnvironmentSettings
    assert not beforeTestEnvironmentSettings == inBetweenTestEnvironmentSettings


@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def handleEnvironmentChangesProperly_withSuccess_whenActionsHaveNoArguments() :
    beforeTestEnvironmentSettings = {**EnvironmentHelper.getSet()}
    inBetweenTestEnvironmentSettings = None
    afterTestEnvironmentSettings = None
    MY_BEFORE_ACTION_RETURN = RandomHelper.string(minimum=10)
    MY_AFTER_ACTION_RETURN = RandomHelper.string(minimum=10)
    # Arrange
    def myBeforeAction():
        return MY_BEFORE_ACTION_RETURN
    def myAfterAction():
        return MY_AFTER_ACTION_RETURN
    def myFunction(a):
        return a
    returns = {}
    @Test(
        callBefore=myBeforeAction,
        callAfter=myAfterAction,
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        inBetweenTestEnvironmentSettings = EnvironmentHelper.getSet()
        assert ObjectHelper.isNotNone(inBetweenTestEnvironmentSettings)
        assert ObjectHelper.isDictionary(inBetweenTestEnvironmentSettings)
        assert 'a' == myFunction('a')
        return inBetweenTestEnvironmentSettings

    # Act
    inBetweenTestEnvironmentSettings = myTest()
    afterTestEnvironmentSettings = {**EnvironmentHelper.getSet()}

    # Assert
    assert MY_BEFORE_ACTION_RETURN == returns['returnOfCallBefore']
    assert MY_AFTER_ACTION_RETURN == returns['returnOfCallAfter']
    assert ObjectHelper.isNotNone(beforeTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(beforeTestEnvironmentSettings)
    assert ObjectHelper.isNotNone(inBetweenTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(inBetweenTestEnvironmentSettings)
    assert ObjectHelper.isNotNone(afterTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(afterTestEnvironmentSettings)
    assert afterTestEnvironmentSettings == beforeTestEnvironmentSettings
    assert not beforeTestEnvironmentSettings == inBetweenTestEnvironmentSettings


@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def handleEnvironmentChangesProperly_withErrorBefore() :
    beforeTestEnvironmentSettings = {**EnvironmentHelper.getSet()}
    inBetweenTestEnvironmentSettings = None
    afterTestEnvironmentSettings = None
    # Arrange
    exceptionMessage = 'some exception'
    def myBeforeAction(c, d=None):
        raise Exception(exceptionMessage)
    def myAfterAction(c, d=None):
        return c+d
    def myFunction(a):
        return a
    returns = {}
    exception = None
    @Test(
        callBefore=myBeforeAction,
        argsOfCallBefore='f',
        kwargsOfCallBefore={'d':'g'},
        callAfter=myAfterAction,
        argsOfCallAfter='h',
        kwargsOfCallAfter={'d':'i'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        inBetweenTestEnvironmentSettings = EnvironmentHelper.getSet()
        assert ObjectHelper.isNotNone(inBetweenTestEnvironmentSettings)
        assert ObjectHelper.isDictionary(inBetweenTestEnvironmentSettings)
        assert 'a' == myFunction('a')
        return inBetweenTestEnvironmentSettings

    # Act
    try :
        inBetweenTestEnvironmentSettings = myTest()
    except Exception as e :
        exception = e
    afterTestEnvironmentSettings = {**EnvironmentHelper.getSet()}

    assert {} == returns
    assert ObjectHelper.isNotEmpty(exception)
    assert exceptionMessage == str(exception)
    assert ObjectHelper.isNotNone(beforeTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(beforeTestEnvironmentSettings)
    assert ObjectHelper.isNone(inBetweenTestEnvironmentSettings)
    assert ObjectHelper.isNotNone(afterTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(afterTestEnvironmentSettings)
    assert afterTestEnvironmentSettings == beforeTestEnvironmentSettings
    assert not beforeTestEnvironmentSettings == inBetweenTestEnvironmentSettings

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def handleEnvironmentChangesProperly_withErrorAfter() :
    beforeTestEnvironmentSettings = {**EnvironmentHelper.getSet()}
    inBetweenTestEnvironmentSettings = None
    afterTestEnvironmentSettings = None
    # Arrange
    exceptionMessage = 'some exception'
    def myBeforeAction(c, d=None):
        return d+c
    def myAfterAction(c, d=None):
        raise Exception(exceptionMessage)
    def myFunction(a):
        return a
    returns = {}
    exception = None
    @Test(
        callBefore=myBeforeAction,
        argsOfCallBefore='f',
        kwargsOfCallBefore={'d':'g'},
        callAfter=myAfterAction,
        argsOfCallAfter='h',
        kwargsOfCallAfter={'d':'i'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        inBetweenTestEnvironmentSettings = EnvironmentHelper.getSet()
        assert ObjectHelper.isNotNone(inBetweenTestEnvironmentSettings)
        assert ObjectHelper.isDictionary(inBetweenTestEnvironmentSettings)
        assert 'a' == myFunction('a')
        return inBetweenTestEnvironmentSettings

    # Act
    try :
        inBetweenTestEnvironmentSettings = myTest()
    except Exception as e :
        exception = e
    afterTestEnvironmentSettings = {**EnvironmentHelper.getSet()}

    assert ObjectHelper.isNotEmpty(exception)
    assert exceptionMessage == str(exception)
    assert 'gf' == returns['returnOfCallBefore']
    assert {'returnOfCallBefore':'gf'} == returns
    assert ObjectHelper.isNotNone(beforeTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(beforeTestEnvironmentSettings)
    assert ObjectHelper.isNone(inBetweenTestEnvironmentSettings)
    assert ObjectHelper.isNotNone(afterTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(afterTestEnvironmentSettings)
    assert afterTestEnvironmentSettings == beforeTestEnvironmentSettings
    assert not beforeTestEnvironmentSettings == inBetweenTestEnvironmentSettings

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **UNMUTED_LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def handleEnvironmentChangesProperly_withError() :
    beforeTestEnvironmentSettings = {**EnvironmentHelper.getSet()}
    inBetweenTestEnvironmentSettings = None
    afterTestEnvironmentSettings = None
    someExceptionMessage = 'some exception message'
    # Arrange
    def myBeforeAction(c, d=None):
        return d+c
    def myAfterAction(c, d=None):
        return c+d
    def myFunction(a):
        raise Exception(someExceptionMessage)
    returns = {}
    @Test(
        callBefore=myBeforeAction,
        argsOfCallBefore='f',
        kwargsOfCallBefore={'d':'g'},
        callAfter=myAfterAction,
        argsOfCallAfter='h',
        kwargsOfCallAfter={'d':'i'},
        returns=returns,
        environmentVariables={
            SettingHelper.ACTIVE_ENVIRONMENT : None,
            **MUTED_LOG_HELPER_SETTINGS
        }
    )
    def myTest() :
        inBetweenTestEnvironmentSettings = EnvironmentHelper.getSet()
        assert ObjectHelper.isNotNone(inBetweenTestEnvironmentSettings)
        assert ObjectHelper.isDictionary(inBetweenTestEnvironmentSettings)
        assert 'a' == myFunction('a')
        return inBetweenTestEnvironmentSettings

    # Act
    try :
        inBetweenTestEnvironmentSettings = myTest()
    except Exception as e :
        exception = e
    afterTestEnvironmentSettings = {**EnvironmentHelper.getSet()}

    # Assert
    assert 'gf' == returns['returnOfCallBefore']
    assert 'hi' == returns['returnOfCallAfter']
    assert ObjectHelper.isNotEmpty(exception)
    assert someExceptionMessage == str(exception)
    assert ObjectHelper.isNotNone(beforeTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(beforeTestEnvironmentSettings)
    assert ObjectHelper.isNone(inBetweenTestEnvironmentSettings)
    assert ObjectHelper.isNotNone(afterTestEnvironmentSettings)
    assert ObjectHelper.isDictionary(afterTestEnvironmentSettings)
    assert afterTestEnvironmentSettings == beforeTestEnvironmentSettings
    assert not beforeTestEnvironmentSettings == inBetweenTestEnvironmentSettings
