from python_helper import SettingHelper, log, ObjectHelper, Function, Method, RandomHelper, Test

# LOG_HELPER_SETTINGS = {
#     log.LOG : True,
#     log.SUCCESS : True,
#     log.SETTING : True,
#     log.DEBUG : True,
#     log.WARNING : True,
#     log.WRAPPER : True,
#     log.FAILURE : True,
#     log.ERROR : True,
    # log.TEST : False
# }

LOG_HELPER_SETTINGS = {
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
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def Function_withSuccess() :
    # Arrange
    TEST = RandomHelper.string(minimum=10)
    @Function
    def myFunction(something) :
        return TEST, something
    @Function
    def myOtherFunction(something) :
        raise Exception(TEST)
    SOMETHING = RandomHelper.string(minimum=10)
    exception = None

    # Act
    myRestult = myFunction(SOMETHING)
    myOtherResult = None
    try :
        myOtherResult = myOtherFunction(SOMETHING)
    except Exception as ext :
        exception = ext

    # Assert
    assert (TEST, SOMETHING) == myRestult
    assert ObjectHelper.isNone(myOtherResult)
    assert ObjectHelper.isNotNone(exception)
    assert TEST == str(exception)

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS: True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def Method_withSuccess() :
    # Arrange
    TEST = RandomHelper.string(minimum=10)
    class MyClass :
        @Method
        def myMethod(self,something) :
            return TEST, something
        @Method
        def myOtherMethod(self,something) :
            raise Exception(TEST)

    @Method
    def myNotMethod(self,something) :
        raise Exception(TEST)
    SOMETHING = RandomHelper.string(minimum=10)
    methodException = None
    notMethodEception = None
    myClass = MyClass()

    # Act
    myRestult = myClass.myMethod(SOMETHING)
    myOtherResult = None
    try :
        myOtherResult = myClass.myOtherMethod(SOMETHING)
    except Exception as ext :
        methodException = ext
    myNotMethodResult = None
    try :
        myNotMethodResult = myNotMethod(None,SOMETHING)
    except Exception as ext :
        notMethodEception = ext
        # print(notMethodEception)

    # Assert
    assert (TEST, SOMETHING) == myRestult
    assert ObjectHelper.isNone(myOtherResult)
    assert ObjectHelper.isNotNone(methodException)
    assert TEST == str(methodException)
    assert ObjectHelper.isNone(myNotMethodResult)
    assert ObjectHelper.isNotNone(notMethodEception)
    assert TEST == str(notMethodEception)
