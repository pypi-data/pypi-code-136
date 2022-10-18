from python_helper import SettingHelper, StringHelper, Constant, log, EnvironmentHelper, ObjectHelper, Test, TestHelper

LOG_HELPER_SETTINGS = {
    log.LOG : False,
    log.SUCCESS : True,
    log.SETTING : True,
    log.DEBUG : True,
    log.WARNING : True,
    log.WRAPPER : True,
    log.FAILURE : True,
    log.ERROR : True,
    log.TEST : False
}

@Test(
    environmentVariables={
        SettingHelper.ACTIVE_ENVIRONMENT : None,
        **LOG_HELPER_SETTINGS
    }
)
def getRaisedException_withSuccess() :
    # Arrange
    myArg = 'myArgValue'
    myKwarg = 'myKwargValue'
    expected = Exception('my exception')
    def someFunction(myArg, myKwarg='myKwargValue'):
        raise expected

    # Act
    toAssert = TestHelper.getRaisedException(someFunction, myArg, myKwarg=myKwarg)

    # Assert
    assert expected == toAssert, f'{expected} == {toAssert}: {expected == toAssert}'
