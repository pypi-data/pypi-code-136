from python_helper import EnvironmentHelper, SettingHelper, ObjectHelper, log, Test

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

TEST_SETTINGS = {}

@Test(
    environmentVariables={
        **LOG_HELPER_SETTINGS
    },
    **TEST_SETTINGS
)
def osIdentifierTest() :
    # arrange

    # act
    isWindows = EnvironmentHelper.isWindows()
    isLinux = EnvironmentHelper.isLinux()
    isMacOs = EnvironmentHelper.isMacOs()
    isOtherOs = EnvironmentHelper.isOtherOs()

    # assert
    assert ObjectHelper.isNotNone(isWindows)
    assert ObjectHelper.isNotNone(isLinux)
    assert ObjectHelper.isNativeClassInstance(isWindows)
    assert ObjectHelper.isNativeClassInstance(isLinux)
    assert bool == type(isWindows)
    assert bool == type(isLinux)
    assert isLinux or isWindows or isMacOs or isOtherOs
