from python_helper import SettingHelper, StringHelper, Constant, log, EnvironmentHelper, ObjectHelper, Test

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
def updateActiveEnvironment_withSuccess() :
    # Arrange
    originalACTIVE_ENVIRONMENT_VALUE = SettingHelper.ACTIVE_ENVIRONMENT_VALUE
    originalGottenActiveEnvironment = SettingHelper.getActiveEnvironment()
    originalActiveEnvironmentIsDefault = SettingHelper.activeEnvironmentIsDefault()
    originalActiveEnvironment = EnvironmentHelper.get(SettingHelper.ACTIVE_ENVIRONMENT)
    originalACTIVE_ENVIRONMENT_VALUEAfterSettingAnotherOne = SettingHelper.ACTIVE_ENVIRONMENT_VALUE
    myNewActiveEnvironment = 'my new artive environment'

    # Act
    myGottenNewActiveEnvironment = SettingHelper.updateActiveEnvironment(myNewActiveEnvironment)

    # Assert
    assert SettingHelper.DEFAULT_ENVIRONMENT == originalGottenActiveEnvironment
    assert SettingHelper.DEFAULT_ENVIRONMENT == originalActiveEnvironment
    assert True == originalActiveEnvironmentIsDefault
    assert myNewActiveEnvironment == EnvironmentHelper.get(SettingHelper.ACTIVE_ENVIRONMENT)
    assert False == SettingHelper.activeEnvironmentIsDefault()
    assert myNewActiveEnvironment == SettingHelper.getActiveEnvironment()
    assert ObjectHelper.isNotEmpty(myGottenNewActiveEnvironment)
    assert myGottenNewActiveEnvironment == myNewActiveEnvironment
    assert SettingHelper.DEFAULT_ENVIRONMENT == originalACTIVE_ENVIRONMENT_VALUE
    assert SettingHelper.DEFAULT_ENVIRONMENT == originalACTIVE_ENVIRONMENT_VALUEAfterSettingAnotherOne
    assert SettingHelper.ACTIVE_ENVIRONMENT_VALUE == myNewActiveEnvironment

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        'MY_COMPLEX_ENV' : ' -- my complex value -- ',
        'LATE_VALUE' : '-- late environment value --',
        'ONLY_ENVIRONMENT_VARIABLE' : 'only environment variable value',
        **LOG_HELPER_SETTINGS
    }
)
def mustReadSettingFile() :
    # Arrange
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','application.yml'])

    # Act
    readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True)
    # log.prettyPython(mustReadSettingFile, 'readdedSettingTree', readdedSettingTree)

    # Assert
    assert 'self reference value' == SettingHelper.getSetting('my.self-reference-key', readdedSettingTree)
    assert 'other self reference value as well' == SettingHelper.getSetting('my.other.self-reference-key.as-well', readdedSettingTree)
    assert 'other repeated self reference value as well' == SettingHelper.getSetting('my.other.repeated.self-reference-key.as-well', readdedSettingTree)
    assert 'my default value' == SettingHelper.getSetting('my.configuration-without-environment-variable-key', readdedSettingTree)
    assert "my default value" == SettingHelper.getSetting('my.configuration-without-environment-variable-key-with-value-surrounded-by-single-quotes', readdedSettingTree)
    assert 'my default value' == SettingHelper.getSetting('my.configuration-without-environment-variable-key-and-space-after-colon', readdedSettingTree)
    assert 'self reference value' == SettingHelper.getSetting('my.configuration', readdedSettingTree)
    assert 'self reference value' == SettingHelper.getSetting('my.own.configuration', readdedSettingTree)
    assert 'other root value' == SettingHelper.getSetting('other.root.key', readdedSettingTree)
    assert 'other root value' == SettingHelper.getSetting('my.own.very.deep.configuration', readdedSettingTree)
    assert 'other self reference value as well' == SettingHelper.getSetting('my.other-with-other-name.self-reference-key.as-well', readdedSettingTree)
    assert 'self reference value' == SettingHelper.getSetting('my.other-with-other-name.configuration', readdedSettingTree)
    assert 'other self reference value as well' == SettingHelper.getSetting('my.other-with-other-name.configuration-as-well', readdedSettingTree)
    assert 'other repeated self reference value as well' == SettingHelper.getSetting('my.other-with-other-name.configuration-repeated-as-well', readdedSettingTree)
    assert SettingHelper.getSetting('my.override-case.overridden', readdedSettingTree) is None
    assert 'overrider configuration' == SettingHelper.getSetting('my.override-case.overrider', readdedSettingTree)

    assert 'delayed assignment value' == SettingHelper.getSetting('some-reference.before-its-assignment', readdedSettingTree)
    assert 'delayed assignment value' == SettingHelper.getSetting('some-reference.much.before-its-assignment', readdedSettingTree)
    assert "'''  value  ''' with spaces" == SettingHelper.getSetting('some-key.with-an-enter-in-between-the-previous-one', readdedSettingTree)
    assert f'''Hi
                every
            one''' == SettingHelper.getSetting('long.string', readdedSettingTree)
    assert f'''Hi
                            every
                            one
                            this
                            is
                            the
                            deepest
                            long
                                        string
                            here''' == SettingHelper.getSetting('deepest.long.string.ever.long.string', readdedSettingTree)
    assert f'''me
                    being
        not
                    fshds''' == SettingHelper.getSetting('not.idented.long.string', readdedSettingTree)
    assert 'abcdefg' == SettingHelper.getSetting('it.contains.one-setting-injection', readdedSettingTree)
    assert 'abcdefghijklm' == SettingHelper.getSetting('it.contains.two-consecutive-setting-injection', readdedSettingTree)
    assert 'abcdefghijklm' == SettingHelper.getSetting('it.contains.one-inside-of-the-other-setting-injection', readdedSettingTree)
    assert 'ABCD-- my complex value --EFG' == SettingHelper.getSetting('it.contains.one-setting-injection-with-environment-variable', readdedSettingTree)
    assert 'ABCDEFGEFG-- my complex value --HIJKLMNOP' == SettingHelper.getSetting('it.contains.one-inside-of-the-other-setting-injection-with-environment-variable', readdedSettingTree)
    assert 'abcdefghijklm' == SettingHelper.getSetting('it.contains.two-consecutive-setting-injection-with-missing-environment-variable', readdedSettingTree)
    assert 'abcd-- late value ----abcd---- late value ----abcd--efg' == SettingHelper.getSetting('it.contains.some-composed-key.pointing-to.a-late-value', readdedSettingTree)
    assert 'abcd-- late environment value ----abcd--it.contains.late-value--abcd--efg' == SettingHelper.getSetting('it.contains.some-composed-key.pointing-to.a-late-value-with-an-environment-variable-in-between', readdedSettingTree)
    assert '-- late value --' == SettingHelper.getSetting('it.contains.late-value', readdedSettingTree)
    assert 'only environment variable value' == SettingHelper.getSetting('it.contains.environment-variable.only', readdedSettingTree)
    assert 'ABCD -- only environment variable value -- EFGH' == SettingHelper.getSetting('it.contains.environment-variable.surrounded-by-default-values', readdedSettingTree)
    assert 'ABCD -- "some value followed by: "only environment variable value\' and some following default value\' -- EFGH' == SettingHelper.getSetting('it.contains.environment-variable.in-between-default-values', readdedSettingTree)
    assert 'ABCD -- very late definiton value -- EFGH' == SettingHelper.getSetting('it.contains.refference.to-a-late-definition', readdedSettingTree)
    assert 222233444 == SettingHelper.getSetting('handle.integer', readdedSettingTree)
    assert 2.3 == SettingHelper.getSetting('handle.float', readdedSettingTree)
    assert True == SettingHelper.getSetting('handle.boolean', readdedSettingTree)
    assert 222233444 == SettingHelper.getSetting('handle.late.integer', readdedSettingTree)
    assert 2.3 == SettingHelper.getSetting('handle.late.float', readdedSettingTree)
    assert True == SettingHelper.getSetting('handle.late.boolean', readdedSettingTree)
    assert [] == SettingHelper.getSetting('handle.empty.list', readdedSettingTree)
    assert {} == SettingHelper.getSetting('handle.empty.dictionary-or-set', readdedSettingTree)
    assert (()) == SettingHelper.getSetting('handle.empty.tuple', readdedSettingTree)
    assert 'ABCD -- 222233444 -- EFGH' == SettingHelper.getSetting('some-not-string-selfreference.integer', readdedSettingTree)
    assert 'ABCD -- 2.3 -- EFGH' == SettingHelper.getSetting('some-not-string-selfreference.float', readdedSettingTree)
    assert 'ABCD -- True -- EFGH' == SettingHelper.getSetting('some-not-string-selfreference.boolean', readdedSettingTree)

@Test(
    environmentVariables={
        **{},
        **LOG_HELPER_SETTINGS
    }
)
def mustNotReadSettingFile() :
    # Arrange
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','application-circular-reference.yml'])
    circularReferenceSettingInjectionDictionary = {
        'circular.reference.on.key': {
            'SETTING_KEY': 'key',
            'SETTING_VALUE': '${circular.reference.on.other-key}',
            'SETTING_NODE_KEY': 'circular.reference.on'
        },
        'circular.reference.on.other-key': {
            'SETTING_KEY': 'other-key',
            'SETTING_VALUE': '${circular.reference.on.key}',
            'SETTING_NODE_KEY': 'circular.reference.on'
        },
        'circular.key': {
            'SETTING_KEY': 'key',
            'SETTING_VALUE': '${circular.other-key}',
            'SETTING_NODE_KEY': 'circular'
        },
        'circular.other-key': {
            'SETTING_KEY': 'other-key',
            'SETTING_VALUE': '${circular.key}',
            'SETTING_NODE_KEY': 'circular'
        }
    }
    fallbackSettingTree = None
    settingTree = {
        'circular': {
            'reference': {
                'on': {}
            }
        }
    }
    exceptionMessage = f'Circular reference detected in following setting injections: {StringHelper.prettyPython(circularReferenceSettingInjectionDictionary)}{Constant.NEW_LINE}FallbackSettingTree: {StringHelper.prettyPython(fallbackSettingTree)}{Constant.NEW_LINE}SettingTree: {StringHelper.prettyPython(settingTree)}'

    # Act
    readdedSettingTree = {}
    exception = None
    try :
        readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True)
    except Exception as ext :
        exception = ext

    # Assert
    assert {} == readdedSettingTree
    assert exceptionMessage == str(exception), f'assert {exceptionMessage} == {str(exception)}'

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    }
)
def mustPrintSettingTree() :
    # Arrange
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','application.yml'])
    readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True)

    # Act
    SettingHelper.printSettings(readdedSettingTree,'some name')

    # Assert
    assert ObjectHelper.isNotNone(readdedSettingTree)

def querySetting_withSuccess() :
    # Arrange
    tree = {
        'key' : {
            'key' : {
                'some-query-key' : {
                    'key' : {
                        'key' : {
                            'some-query-key' : 'value',
                            'key' : 'value'
                        }
                    },
                    'other-key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : 'value'
                        }
                    }
                },
                'key' : {
                    'key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : 'value'
                        }
                    },
                    'other-key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : 'value'
                        }
                    }
                },
                'other-key' : {
                    'key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : 'value'
                        }
                    },
                    'other-key' : {
                        'key' : {
                            'other-key' : 'value',
                            'key' : {
                                'some-query-key' : 'value',
                                'key' : 'value'
                            }
                        }
                    }
                }
            }
        },
        'other-key' : 'value'
    }

    # Act
    queryTree = SettingHelper.querySetting('some-query-key',tree)

    # Assert
    assert {
        'key.key.some-query-key': {
            'key': {
                'key': {
                    'some-query-key': 'value',
                    'key': 'value'
                }
            },
            'other-key': {
                'key': {
                    'other-key': 'value',
                    'key': 'value'
                }
            }
        },
        'key.key.some-query-key.key.key.some-query-key': 'value',
        'key.key.other-key.other-key.key.key.some-query-key': 'value'
    } == queryTree

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    }
)
def mustHandleSettingValueInFallbackSettingTree() :
    # Arrange
    settingFallbackFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','fallback-application.yml'])
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','referencing-fallback-application.yml'])
    FIRST_LONG_STRING = '''"""Hi
                every
            one
            """'''
    SECOND_LONG_STRING = '''"""Hi
                            every
                            one
                            this
                            is
                            the
                            deepest
                            long
                                        string
                            here
                            """'''
    THIRD_LONG_STRING = '''"""
                    me
                    being
        not
                    fshds
                    """'''

    # Act
    readdedSettingFallbackFilePath = SettingHelper.getSettingTree(settingFallbackFilePath)
    readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True, fallbackSettingTree=readdedSettingFallbackFilePath)
    # log.prettyPython(mustHandleSettingValueInFallbackSettingTree, 'readdedSettingTree', readdedSettingTree, logLevel=log.SETTING)

    # Assert
    assert [] == SettingHelper.getSetting('reffer-to.fallback-settings.empty.list', readdedSettingTree)
    assert 'ABCD -- [] -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.empty.list-in-between', readdedSettingTree)
    assert (()) == SettingHelper.getSetting('reffer-to.fallback-settings.empty.tuple', readdedSettingTree)
    assert 'ABCD -- () -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.empty.tuple-in-between', readdedSettingTree)
    assert {} == SettingHelper.getSetting('reffer-to.fallback-settings.empty.set-or-dictionary', readdedSettingTree)
    assert 'ABCD -- {} -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.empty.set-or-dictionary-in-between', readdedSettingTree)
    assert [
        'a',
        'b',
        'c'
    ] == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.list', readdedSettingTree)
    assert "ABCD -- ['a', 'b', 'c'] -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.list-in-between', readdedSettingTree)
    assert (
        True,
        False,
        'None'
    ) == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.tuple', readdedSettingTree)
    assert "ABCD -- (True, False, 'None') -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.tuple-in-between', readdedSettingTree)
    assert {} == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.set', readdedSettingTree)
    assert 'ABCD -- {} -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.set-in-between', readdedSettingTree)
    assert {
        '1': 20,
        '2': 10,
        '3': 30
    } == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.dictionary', readdedSettingTree)
    assert "ABCD -- {'1': 20, '2': 10, '3': 30} -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.dictionary-in-between', readdedSettingTree)
    assert "fallback value" == SettingHelper.getSetting('reffer-to.fallback-settings.string', readdedSettingTree)
    assert "ABCD -- fallback value -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.string-in-between', readdedSettingTree)
    assert 222233444 == SettingHelper.getSetting('reffer-to.fallback-settings.integer', readdedSettingTree)
    assert "ABCD -- 222233444 -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.integer-in-between', readdedSettingTree)
    assert 2.3 == SettingHelper.getSetting('reffer-to.fallback-settings.float', readdedSettingTree)
    assert "ABCD -- 2.3 -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.float-in-between', readdedSettingTree)
    assert True == SettingHelper.getSetting('reffer-to.fallback-settings.boolean', readdedSettingTree)
    assert "ABCD -- True -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.boolean-in-between', readdedSettingTree)
    assert 'None' == SettingHelper.getSetting('reffer-to.fallback-settings.none', readdedSettingTree)
    assert "ABCD -- None -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.none-in-between', readdedSettingTree)
    assert ObjectHelper.equals({
        'some-reference': {
            'much': {
                'before-its-assignment': 'delayed assignment value'
            },
            'before-its-assignment': 'delayed assignment value'
        },
        'other': {
            'root': {
                'key': 'other root value'
            }
        },
        'my': {
            'self-reference-key': 'self reference value',
            'other': {
                'self-reference-key': {
                    'as-well': 'other self reference value as well'
                },
                'repeated': {
                    'self-reference-key': {
                        'as-well': 'other repeated self reference value as well'
                    }
                }
            },
            'configuration-without-environment-variable-key': 'my default value',
            'configuration-without-environment-variable-key-with-value-surrounded-by-single-quotes': 'my default value',
            'configuration-without-environment-variable-key-and-space-after-colon': 'my default value',
            'configuration': 'self reference value',
            'own': {
                'configuration': 'self reference value',
                'very': {
                    'deep': {
                        'configuration': 'other root value'
                    }
                }
            },
            'other-with-other-name': {
                'self-reference-key': {
                    'as-well': 'other self reference value as well'
                },
                'configuration': 'self reference value',
                'configuration-as-well': 'other self reference value as well',
                'configuration-repeated-as-well': 'other repeated self reference value as well'
            },
            'override-case': {
                'overrider': 'overrider configuration'
            }
        },
        'long': {
            'string': FIRST_LONG_STRING
        },
        'deepest': {
            'long': {
                'string': {
                    'ever': {
                        'long': {
                            'string': SECOND_LONG_STRING
                        }
                    }
                }
            }
        },
        'not': {
            'idented': {
                'long': {
                    'string': THIRD_LONG_STRING
                }
            }
        },
        'new-key': 'new value',
        'my-list': {
            'numbers': [
                1,
                2,
                3,
                4
            ],
            'simple-strings': [
                'a',
                'b',
                'c',
                'd'
            ],
            'complex': [
                2,
                'b',
                'c',
                'd',
                1,
                2,
                True,
                True
            ],
            'with-elemets-surrounded-by-all-sorts-of-quotes': [
                'a',
                'b',
                'c',
                'd',
                'e',
                'f'
            ]
        },
        'specific-for': {
            'previous-assignment': 'delayed assignment value'
        },
        'some-key': {
            'with-an-enter-in-between-the-previous-one': f'{Constant.TRIPLE_SINGLE_QUOTE}  value  {Constant.TRIPLE_SINGLE_QUOTE} with spaces'
        },
        'it': {
            'contains': {
                'some-composed-key': {
                    'pointing-to': {
                        'a-late-value': 'abcd-- late value ----abcd---- late value ----abcd--efg',
                        'a-late-value-with-an-environment-variable-in-between': 'abcdit.contains.late-value--abcd--it.contains.late-value--abcd--efg'
                    }
                },
                'late-value': '-- late value --',
                'environment-variable': {
                    'only': {
                        'surrounded-by-default-values': 'ABCD --  -- EFGH',
                        'in-between-default-values': '''ABCD -- "some value followed by: "' and some following default value' -- EFGH'''
                    }
                },
                'refference': {
                    'to-a-late-definition': 'ABCD -- very late definiton value -- EFGH'
                },
                'one-setting-injection': 'abcdefg',
                'two-consecutive-setting-injection': 'abcdefghijklm',
                'one-inside-of-the-other-setting-injection': 'abcdefghijklm',
                'one-setting-injection-with-environment-variable': 'ABCDefgEFG',
                'one-inside-of-the-other-setting-injection-with-environment-variable': 'ABCDEFGEFGHIJKLMNOP',
                'two-consecutive-setting-injection-with-missing-environment-variable': 'abcdefghijklm'
            }
        },
        'very-late': {
            'definition': 'very late definiton value'
        },
        'handle': {
            'late': {
                'integer': 222233444,
                'float': 2.3,
                'boolean': True
            },
            'integer': 222233444,
            'float': 2.3,
            'boolean': True,
            'empty': {
                'list': [],
                'dictionary-or-set': {},
                'tuple': ()
            }
        },
        'some-not-string-selfreference': {
            'integer': 'ABCD -- 222233444 -- EFGH',
            'float': 'ABCD -- 2.3 -- EFGH',
            'boolean': 'ABCD -- True -- EFGH'
        },
        'reffer-to': {
            'fallback-settings': {
                'empty': {
                    'list': [],
                    'list-in-between': 'ABCD -- [] -- EFGH',
                    'tuple': (),
                    'tuple-in-between': 'ABCD -- () -- EFGH',
                    'set-or-dictionary': {},
                    'set-or-dictionary-in-between': 'ABCD -- {} -- EFGH'
                },
                'not-empty': {
                    'list': [
                        'a',
                        'b',
                        'c'
                    ],
                    'list-in-between': "ABCD -- ['a', 'b', 'c'] -- EFGH",
                    'tuple': (
                        True,
                        False,
                        'None'
                    ),
                    'tuple-in-between': "ABCD -- (True, False, 'None') -- EFGH",
                    'set': {},
                    'set-in-between': 'ABCD -- {} -- EFGH',
                    'dictionary': {
                        '1': 20,
                        '2': 10,
                        '3': 30
                    },
                    'dictionary-in-between': "ABCD -- {'1': 20, '2': 10, '3': 30} -- EFGH"
                },
                'string': 'fallback value',
                'string-in-between': 'ABCD -- fallback value -- EFGH',
                'integer': 222233444,
                'integer-in-between': 'ABCD -- 222233444 -- EFGH',
                'float': 2.3,
                'float-in-between': 'ABCD -- 2.3 -- EFGH',
                'boolean': True,
                'boolean-in-between': 'ABCD -- True -- EFGH',
                'none': 'None',
                'none-in-between': 'ABCD -- None -- EFGH'
            }
        },
        'some': {
            'key': 'value',
            'very': {
                'key': 'value',
                'similar': {
                    'key': 'value',
                    'tree': {
                        'key': 'value',
                        'with': {
                            'key': 'value',
                            'a': {
                                'key': 'value',
                                'slight': {
                                    'key': 'value',
                                    'difference': {
                                        'key': 'value',
                                        'right': {
                                            'here': 'anoter value'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        'print-status': True,
        'server': {
            'scheme': 'http',
            'port': 5001,
            'servlet': {
                'context-path': '/test-api'
            }
        },
        'swagger': {
            'schemes': [
                'http'
            ],
            'host': 'localhost:5001',
            'info': {
                'title': 'TestApi',
                'version': '0.0.1',
                'description': 'description',
                'terms-of-service': 'http://swagger.io/terms/',
                'contact': {
                    'name': 'Samuel Jansen',
                    'email': 'samuel.jansenn@gmail.com'
                },
                'license': {
                    'name': 'Apache 2.0 / MIT License',
                    'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
                }
            }
        },
        'fallback': {
            'string': 'fallback value',
            'integer': 222233444,
            'float': 2.3,
            'boolean': True,
            'none': 'None',
            'empty': {
                'list': [],
                'set-or-dictionary': {},
                'tuple': ()
            },
            'not-empty': {
                'list': [
                    'a',
                    'b',
                    'c'
                ],
                'dictionary': {
                    '1': 20,
                    '2': 10,
                    '3': 30
                },
                'set': {},
                'tuple': (
                    True,
                    False,
                    'None'
                )
            }
        },
        'flask-specific-port': 'flask run --host=0.0.0.0 --port=5001',
        'api': {
            'name': 'TestApi',
            'extension': 'yml',
            'dependency': {
                'update': False,
                'list': {
                    'web': [
                        'globals',
                        'python_helper',
                        'Popen',
                        'Path',
                        'numpy',
                        'pywin32',
                        'sqlalchemy'
                    ]
                }
            },
            'git': {
                'force-upgrade-command': 'pip install --upgrade --force python_framework'
            },
            'static-package': 'AppData\Local\Programs\Python\Python38-32\statics'
        }
    },
    readdedSettingTree, ignoreKeyList=['it'])

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    }
)
def mustHandleSettingValueInFallbackSettingTree_whenFallbackSettingFilePathIsPassedInsted() :
    # Arrange
    settingFallbackFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','fallback-application.yml'])
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','referencing-fallback-application.yml'])
    FIRST_LONG_STRING = '''"""Hi
                every
            one
            """'''
    SECOND_LONG_STRING = '''"""Hi
                            every
                            one
                            this
                            is
                            the
                            deepest
                            long
                                        string
                            here
                            """'''
    THIRD_LONG_STRING = '''"""
                    me
                    being
        not
                    fshds
                    """'''

    # Act
    readdedSettingTree = SettingHelper.getSettingTree(settingFilePath, keepDepthInLongString=True, fallbackSettingFilePath=settingFallbackFilePath)
    # log.prettyPython(mustHandleSettingValueInFallbackSettingTree_whenFallbackSettingFilePathIsPassedInsted, 'readdedSettingTree', readdedSettingTree, logLevel=log.SETTING)

    # Assert
    assert [] == SettingHelper.getSetting('reffer-to.fallback-settings.empty.list', readdedSettingTree)
    assert 'ABCD -- [] -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.empty.list-in-between', readdedSettingTree)
    assert (()) == SettingHelper.getSetting('reffer-to.fallback-settings.empty.tuple', readdedSettingTree)
    assert 'ABCD -- () -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.empty.tuple-in-between', readdedSettingTree)
    assert {} == SettingHelper.getSetting('reffer-to.fallback-settings.empty.set-or-dictionary', readdedSettingTree)
    assert 'ABCD -- {} -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.empty.set-or-dictionary-in-between', readdedSettingTree)
    assert [
        'a',
        'b',
        'c'
    ] == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.list', readdedSettingTree)
    assert "ABCD -- ['a', 'b', 'c'] -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.list-in-between', readdedSettingTree)
    assert (
        True,
        False,
        'None'
    ) == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.tuple', readdedSettingTree)
    assert "ABCD -- (True, False, 'None') -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.tuple-in-between', readdedSettingTree)
    assert {} == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.set', readdedSettingTree)
    assert 'ABCD -- {} -- EFGH' == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.set-in-between', readdedSettingTree)
    assert {
        '1': 20,
        '2': 10,
        '3': 30
    } == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.dictionary', readdedSettingTree)
    assert "ABCD -- {'1': 20, '2': 10, '3': 30} -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.not-empty.dictionary-in-between', readdedSettingTree)
    assert "fallback value" == SettingHelper.getSetting('reffer-to.fallback-settings.string', readdedSettingTree)
    assert "ABCD -- fallback value -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.string-in-between', readdedSettingTree)
    assert 222233444 == SettingHelper.getSetting('reffer-to.fallback-settings.integer', readdedSettingTree)
    assert "ABCD -- 222233444 -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.integer-in-between', readdedSettingTree)
    assert 2.3 == SettingHelper.getSetting('reffer-to.fallback-settings.float', readdedSettingTree)
    assert "ABCD -- 2.3 -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.float-in-between', readdedSettingTree)
    assert True == SettingHelper.getSetting('reffer-to.fallback-settings.boolean', readdedSettingTree)
    assert "ABCD -- True -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.boolean-in-between', readdedSettingTree)
    assert 'None' == SettingHelper.getSetting('reffer-to.fallback-settings.none', readdedSettingTree)
    assert "ABCD -- None -- EFGH" == SettingHelper.getSetting('reffer-to.fallback-settings.none-in-between', readdedSettingTree)
    assert ObjectHelper.equals({
        'some-reference': {
            'much': {
                'before-its-assignment': 'delayed assignment value'
            },
            'before-its-assignment': 'delayed assignment value'
        },
        'other': {
            'root': {
                'key': 'other root value'
            }
        },
        'my': {
            'self-reference-key': 'self reference value',
            'other': {
                'self-reference-key': {
                    'as-well': 'other self reference value as well'
                },
                'repeated': {
                    'self-reference-key': {
                        'as-well': 'other repeated self reference value as well'
                    }
                }
            },
            'configuration-without-environment-variable-key': 'my default value',
            'configuration-without-environment-variable-key-with-value-surrounded-by-single-quotes': 'my default value',
            'configuration-without-environment-variable-key-and-space-after-colon': 'my default value',
            'configuration': 'self reference value',
            'own': {
                'configuration': 'self reference value',
                'very': {
                    'deep': {
                        'configuration': 'other root value'
                    }
                }
            },
            'other-with-other-name': {
                'self-reference-key': {
                    'as-well': 'other self reference value as well'
                },
                'configuration': 'self reference value',
                'configuration-as-well': 'other self reference value as well',
                'configuration-repeated-as-well': 'other repeated self reference value as well'
            },
            'override-case': {
                'overrider': 'overrider configuration'
            }
        },
        'long': {
            'string': FIRST_LONG_STRING
        },
        'deepest': {
            'long': {
                'string': {
                    'ever': {
                        'long': {
                            'string': SECOND_LONG_STRING
                        }
                    }
                }
            }
        },
        'not': {
            'idented': {
                'long': {
                    'string': THIRD_LONG_STRING
                }
            }
        },
        'new-key': 'new value',
        'my-list': {
            'numbers': [
                1,
                2,
                3,
                4
            ],
            'simple-strings': [
                'a',
                'b',
                'c',
                'd'
            ],
            'complex': [
                2,
                'b',
                'c',
                'd',
                1,
                2,
                True,
                True
            ],
            'with-elemets-surrounded-by-all-sorts-of-quotes': [
                'a',
                'b',
                'c',
                'd',
                'e',
                'f'
            ]
        },
        'specific-for': {
            'previous-assignment': 'delayed assignment value'
        },
        'some-key': {
            'with-an-enter-in-between-the-previous-one': '\'\'\'  value  \'\'\' with spaces'
        },
        'it': {
            'contains': {
                'some-composed-key': {
                    'pointing-to': {
                        'a-late-value': 'abcd-- late value ----abcd---- late value ----abcd--efg',
                        'a-late-value-with-an-environment-variable-in-between': 'abcdit.contains.late-value--abcd--it.contains.late-value--abcd--efg'
                    }
                },
                'late-value': '-- late value --',
                'environment-variable': {
                    'only': {
                        'surrounded-by-default-values': 'ABCD --  -- EFGH',
                        'in-between-default-values': '''ABCD -- "some value followed by: "\' and some following default value\' -- EFGH'''
                    }
                },
                'refference': {
                    'to-a-late-definition': 'ABCD -- very late definiton value -- EFGH'
                },
                'one-setting-injection': 'abcdefg',
                'two-consecutive-setting-injection': 'abcdefghijklm',
                'one-inside-of-the-other-setting-injection': 'abcdefghijklm',
                'one-setting-injection-with-environment-variable': 'ABCDefgEFG',
                'one-inside-of-the-other-setting-injection-with-environment-variable': 'ABCDEFGEFGHIJKLMNOP',
                'two-consecutive-setting-injection-with-missing-environment-variable': 'abcdefghijklm'
            }
        },
        'very-late': {
            'definition': 'very late definiton value'
        },
        'handle': {
            'late': {
                'integer': 222233444,
                'float': 2.3,
                'boolean': True
            },
            'integer': 222233444,
            'float': 2.3,
            'boolean': True,
            'empty': {
                'list': [],
                'dictionary-or-set': {},
                'tuple': ()
            }
        },
        'some-not-string-selfreference': {
            'integer': 'ABCD -- 222233444 -- EFGH',
            'float': 'ABCD -- 2.3 -- EFGH',
            'boolean': 'ABCD -- True -- EFGH'
        },
        'reffer-to': {
            'fallback-settings': {
                'empty': {
                    'list': [],
                    'list-in-between': 'ABCD -- [] -- EFGH',
                    'tuple': (),
                    'tuple-in-between': 'ABCD -- () -- EFGH',
                    'set-or-dictionary': {},
                    'set-or-dictionary-in-between': 'ABCD -- {} -- EFGH'
                },
                'not-empty': {
                    'list': [
                        'a',
                        'b',
                        'c'
                    ],
                    'list-in-between': "ABCD -- ['a', 'b', 'c'] -- EFGH",
                    'tuple': (
                        True,
                        False,
                        'None'
                    ),
                    'tuple-in-between': "ABCD -- (True, False, 'None') -- EFGH",
                    'set': {},
                    'set-in-between': 'ABCD -- {} -- EFGH',
                    'dictionary': {
                        '1': 20,
                        '2': 10,
                        '3': 30
                    },
                    'dictionary-in-between': "ABCD -- {'1': 20, '2': 10, '3': 30} -- EFGH"
                },
                'string': 'fallback value',
                'string-in-between': 'ABCD -- fallback value -- EFGH',
                'integer': 222233444,
                'integer-in-between': 'ABCD -- 222233444 -- EFGH',
                'float': 2.3,
                'float-in-between': 'ABCD -- 2.3 -- EFGH',
                'boolean': True,
                'boolean-in-between': 'ABCD -- True -- EFGH',
                'none': 'None',
                'none-in-between': 'ABCD -- None -- EFGH'
            }
        },
        'some': {
            'key': 'value',
            'very': {
                'key': 'value',
                'similar': {
                    'key': 'value',
                    'tree': {
                        'key': 'value',
                        'with': {
                            'key': 'value',
                            'a': {
                                'key': 'value',
                                'slight': {
                                    'key': 'value',
                                    'difference': {
                                        'key': 'value',
                                        'right': {
                                            'here': 'anoter value'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        'print-status': True,
        'server': {
            'scheme': 'http',
            'port': 5001,
            'servlet': {
                'context-path': '/test-api'
            }
        },
        'swagger': {
            'schemes': [
                'http'
            ],
            'host': 'localhost:5001',
            'info': {
                'title': 'TestApi',
                'version': '0.0.1',
                'description': 'description',
                'terms-of-service': 'http://swagger.io/terms/',
                'contact': {
                    'name': 'Samuel Jansen',
                    'email': 'samuel.jansenn@gmail.com'
                },
                'license': {
                    'name': 'Apache 2.0 / MIT License',
                    'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
                }
            }
        },
        'fallback': {
            'string': 'fallback value',
            'integer': 222233444,
            'float': 2.3,
            'boolean': True,
            'none': 'None',
            'empty': {
                'list': [],
                'set-or-dictionary': {},
                'tuple': ()
            },
            'not-empty': {
                'list': [
                    'a',
                    'b',
                    'c'
                ],
                'dictionary': {
                    '1': 20,
                    '2': 10,
                    '3': 30
                },
                'set': {},
                'tuple': (
                    True,
                    False,
                    'None'
                )
            }
        },
        'flask-specific-port': 'flask run --host=0.0.0.0 --port=5001',
        'api': {
            'name': 'TestApi',
            'extension': 'yml',
            'dependency': {
                'update': False,
                'list': {
                    'web': [
                        'globals',
                        'python_helper',
                        'Popen',
                        'Path',
                        'numpy',
                        'pywin32',
                        'sqlalchemy'
                    ]
                }
            },
            'git': {
                'force-upgrade-command': 'pip install --upgrade --force python_framework'
            },
            'static-package': 'AppData\Local\Programs\Python\Python38-32\statics'
        }
    },
    readdedSettingTree, ignoreKeyList=['it'])

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    }
)
def getSettingTree_whenIsSettingKeyActuallyContainsSettingKey() :
    # Arrange
    settingFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','framework.yml'])
    expected = {
        'database': {
            'dialect': 'a:b$c:d',
            'username': 'e:f?g:h',
            'password': 'i:j!k:l',
            'host': 'm:n*o:p',
            'port': '[q:r:s:t]',
            'schema': '(u:v:w:x)'
        },
        'environment': {
            'database': {
                'key': 'DATABASE_URL',
                'value': 'a:b$c:d://e:f?g:h:i:j!k:l@m:n*o:p:[q:r:s:t]/(u:v:w:x)'
            }
        },
        'server': {
            'scheme': 'https',
            'host': 'host',
            'servlet': {
                'context-path': '/test-api'
            },
            'port': 5050
        },
        'api': {
            'name': 'TestApi',
            'host-0': 'https://host',
            'host-1': 'https://host/test-api',
            'host-2': 'https://host:5050/test-api'
        },
        'swagger': {
            'host': 'host',
            'info': {
                'title': 'TestApi',
                'version': '0.0.1',
                'description': 'description',
                'terms-of-service': 'http://swagger.io/terms/',
                'contact': {
                    'name': 'Samuel Jansen',
                    'email': 'samuel.jansenn@gmail.com'
                },
                'license': {
                    'name': 'Apache 2.0 / MIT License',
                    'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
                }
            },
            'schemes': [
                'https'
            ]
        },
        'some': {
            'dictionary': {
                'yolo': 'yes',
                'another-yolo': 'no',
                'another-yolo-again': '',
                "{ 'again?'": "'yes' }"
            }
        }
    }

    # Act
    readdedSettingTree = SettingHelper.getSettingTree(settingFilePath)
    # log.prettyPython(getSettingTree_whenIsSettingKeyActuallyContainsSettingKey, 'readdedSettingTree', readdedSettingTree)

    # Assert
    assert "a:b$c:d://e:f?g:h:i:j!k:l@m:n*o:p:[q:r:s:t]/(u:v:w:x)" == SettingHelper.getSetting('environment.database.value', readdedSettingTree)
    assert ObjectHelper.equals(expected, readdedSettingTree)

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    }
)
def getSettingTree_fallbackPriority() :
    # arrange
    defaultFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','fallback-priority.yml'])
    localFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','fallback-priority-local.yml'])
    expected = {
        'print-status': True,
        'server': {
            'scheme': 'http',
            'host': 'localhost',
            'host-and-port': 'localhost:5050',
            'port': 5050,
            'servlet': {
                'context-path': '/test-api'
            }
        },
        'has-it': {
            'or-not': '?',
            'here': '?'
        },
        'flask-specific-port': 'flask run --host=0.0.0.0 --port=5001',
        'api': {
            'name': 'TestApi',
            'extension': 'yml',
            'dependency': {
                'update': False,
                'list': {
                    'web': [
                        'globals',
                        'python_helper',
                        'Popen',
                        'Path',
                        'numpy',
                        'pywin32',
                        'sqlalchemy'
                    ]
                }
            },
            'git': {
                'force-upgrade-command': 'pip install --upgrade --force python_framework'
            },
            'static-package': 'AppData\Local\Programs\Python\Python38-32\statics',
            'list': []
        },
        'swagger': {
            'info': {
                'title': 'TestApi',
                'version': '0.0.1',
                'description': 'description',
                'terms-of-service': 'http://swagger.io/terms/',
                'contact': {
                    'name': 'Samuel Jansen',
                    'email': 'samuel.jansenn@gmail.com'
                },
                'license': {
                    'name': 'Apache 2.0 / MIT License',
                    'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
                }
            },
            'host': 'localhost:5050',
            'schemes': [
                'http'
            ]
        },
        'python': {
            'version': 3.9
        }
    }

    # act
    toAssert = SettingHelper.getSettingTree(localFilePath, keepDepthInLongString=True, fallbackSettingFilePath=defaultFilePath)
    # log.prettyPython(getSettingTree_fallbackPriority, 'localSettings', toAssert, logLevel=log.SETTING)

    assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyPython(expected)} == {StringHelper.prettyPython(toAssert)}'

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        'MY_COMPLEX_ENV' : ' -- my complex value -- ',
        'LATE_VALUE' : '-- late environment value --',
        'ONLY_ENVIRONMENT_VARIABLE' : 'only environment variable value',
        **LOG_HELPER_SETTINGS,
    }
)
def getSettingTree_otherApplication() :
    # arrange
    defaultFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','other-application.yml'])
    localFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','other-application-local.yml'])
    LOCAL_CONFIG_VALUE = 'local config setting value'
    FIRST_LONG_STRING = '''"""Hi
                every
            one
            """'''
    SECOND_LONG_STRING = '''"""Hi
                            every
                            one
                            this
                            is
                            the
                            deepest
                            long
                                        string
                            here
                            """'''
    THIRD_LONG_STRING = '''"""
                    me
                    being
        not
                    fshds
                    """'''
    expected = {
        'print-status': True,
        'local': {
            'config': {
                'setting-key': 'local config setting value'
            }
        },
        'database': {
            'dialect': 'a:b$c:d',
            'username': 'e:f?g:h',
            'password': 'i:j!k:l',
            'host': 'm:n*o:p',
            'port': '[q:r:s:t]',
            'schema': '(u:v:w:x)'
        },
        'environment': {
            'database': {
                'key': 'DATABASE_URL',
                'value': 'a:b$c:d://e:f?g:h:i:j!k:l@m:n*o:p:[q:r:s:t]/(u:v:w:x)'
            },
            'test': 'production',
            'missing': 'not at all'
        },
        'server': {
            'scheme': 'https',
            'host': 'host',
            'servlet': {
                'context-path': '/test-api'
            },
            'port': 5050
        },
        'api': {
            'host-0': 'https://host',
            'host-1': 'https://host/test-api',
            'host-2': 'https://host:5050/test-api',
            'name': 'Globals',
            'extension': 'yml',
            'dependency': {
                'update': False,
                'list': {
                    'web': [
                        'Popen',
                        'Path'
                    ],
                    'local': []
                }
            },
            'list': [
                'Globals'
            ],
            'language': 'EN-US',
            'git': {
                'url': 'https://github.com/SamuelJansen/',
                'extension': 'git'
            }
        },
        'swagger': {
            'host': 'host',
            'info': {
                'title': 'TestApi',
                'version': '0.0.1',
                'description': 'description',
                'terms-of-service': 'http://swagger.io/terms/',
                'contact': {
                    'name': 'Samuel Jansen',
                    'email': 'samuel.jansenn@gmail.com'
                },
                'license': {
                    'name': 'Apache 2.0 / MIT License',
                    'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
                }
            },
            'schemes': [
                'https'
            ]
        },
        'python': {
            'version': 3.9
        },
        'some-reference': {
            'much': {
                'before-its-assignment': 'delayed assignment value'
            },
            'before-its-assignment': 'delayed assignment value'
        },
        'other': {
            'root': {
                'key': 'other root value'
            }
        },
        'my': {
            'self-reference-key': 'self reference value',
            'other': {
                'self-reference-key': {
                    'as-well': 'other self reference value as well'
                },
                'repeated': {
                    'self-reference-key': {
                        'as-well': 'other repeated self reference value as well'
                    }
                }
            },
            'configuration-without-environment-variable-key': 'my default value',
            'configuration-without-environment-variable-key-with-value-surrounded-by-single-quotes': 'my default value',
            'configuration-without-environment-variable-key-and-space-after-colon': 'my default value',
            'own': {
                'very': {
                    'deep': {
                        'configuration': 'other root value'
                    }
                },
                'configuration': 'self reference value'
            },
            'other-with-other-name': {
                'self-reference-key': {
                    'as-well': 'other self reference value as well'
                },
                'configuration': 'self reference value',
                'configuration-as-well': 'other self reference value as well',
                'configuration-repeated-as-well': 'other repeated self reference value as well'
            },
            'override-case': {
                'overrider': 'overrider configuration'
            },
            'configuration': 'self reference value'
        },
        'long': {
            'string': FIRST_LONG_STRING
        },
        'deepest': {
            'long': {
                'string': {
                    'ever': {
                        'long': {
                            'string': SECOND_LONG_STRING
                        }
                    }
                }
            }
        },
        'not': {
            'idented': {
                'long': {
                    'string': THIRD_LONG_STRING
                }
            }
        },
        'new-key': 'new value',
        'my-list': {
            'numbers': [
                1,
                2,
                3,
                4
            ],
            'simple-strings': [
                'a',
                'b',
                'c',
                'd'
            ],
            'complex': [
                2,
                'b',
                'c',
                'd',
                1,
                2,
                True,
                True
            ],
            'with-elemets-surrounded-by-all-sorts-of-quotes': [
                'a',
                'b',
                'c',
                'd',
                'e',
                'f'
            ]
        },
        'specific-for': {
            'previous-assignment': 'delayed assignment value'
        },
        'some-key': {
            'with-an-enter-in-between-the-previous-one': "'''  value  ''' with spaces"
        },
        'it': {
            'contains': {
                'some-composed-key': {
                    'pointing-to': {
                        'a-late-value': 'abcd-- late value ----abcd---- late value ----abcd--efg',
                        'a-late-value-with-an-environment-variable-in-between': 'abcd-- late environment value ----abcd--it.contains.late-value--abcd--efg'
                    }
                },
                'late-value': '-- late value --',
                'environment-variable': {
                    'only': 'only environment variable value',
                    'surrounded-by-default-values': 'ABCD -- only environment variable value -- EFGH',
                    'in-between-default-values': """ABCD -- "some value followed by: "only environment variable value' and some following default value' -- EFGH"""
                },
                'refference': {
                    'to-a-late-definition': 'ABCD -- very late definiton value -- EFGH'
                },
                'one-setting-injection': 'abcdefg',
                'two-consecutive-setting-injection': 'abcdefghijklm',
                'one-inside-of-the-other-setting-injection': 'abcdefghijklm',
                'one-setting-injection-with-environment-variable': 'ABCD-- my complex value --EFG',
                'one-inside-of-the-other-setting-injection-with-environment-variable': 'ABCDEFGEFG-- my complex value --HIJKLMNOP',
                'two-consecutive-setting-injection-with-missing-environment-variable': 'abcdefghijklm'
            }
        },
        'very-late': {
            'definition': 'very late definiton value'
        },
        'handle': {
            'late': {
                'integer': 222233444,
                'float': 2.3,
                'boolean': True
            },
            'integer': 222233444,
            'float': 2.3,
            'boolean': True,
            'empty': {
                'list': [],
                'dictionary-or-set': {},
                'tuple': ()
            }
        },
        'some': {
            'dictionary': {
                'yolo': 'yes',
                'another-yolo': 'no',
                'another-yolo-again': '',
                f'''{'{'}{" 'again?'"}''': f'''{"'yes' "}{'}'}'''
            }
        },
        'some-not-string-selfreference': {
            'integer': 'ABCD -- 222233444 -- EFGH',
            'float': 'ABCD -- 2.3 -- EFGH',
            'boolean': 'ABCD -- True -- EFGH'
        }
    }

    # act
    # log.prettyPython(getSettingTree_fallbackPriority, 'expected', expected, logLevel=log.SETTING)
    falback = SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True)
    # log.prettyPython(getSettingTree_fallbackPriority, 'falback', falback, logLevel=log.SETTING)
    toAssert = SettingHelper.getSettingTree(localFilePath, keepDepthInLongString=True, fallbackSettingFilePath=defaultFilePath, fallbackSettingTree=falback)
    # log.prettyPython(getSettingTree_fallbackPriority, 'toAssert', toAssert, logLevel=log.SETTING)

    # assert
    assert LOCAL_CONFIG_VALUE == SettingHelper.getSetting('local.config.setting-key', toAssert)
    assert True == SettingHelper.getSetting('print-status', toAssert)
    assert 'Globals' == SettingHelper.getSetting('api.name', toAssert)
    assert "a:b$c:d://e:f?g:h:i:j!k:l@m:n*o:p:[q:r:s:t]/(u:v:w:x)" == SettingHelper.getSetting('environment.database.value', toAssert), SettingHelper.getSetting('environment.database.value', toAssert)
    assert expected['long']['string'] == toAssert['long']['string']
    assert expected['deepest']['long']['string']['ever']['long']['string'] == toAssert['deepest']['long']['string']['ever']['long']['string']
    assert expected['not']['idented']['long']['string'] == toAssert['not']['idented']['long']['string']
    assert ObjectHelper.equals(expected['some']['dictionary'], toAssert['some']['dictionary'])
    assert ObjectHelper.equals(expected, toAssert), f'{expected} --x-- {toAssert}'

@Test(
    environmentVariables={
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        'MIRACLE' : 'yes.this.is.possible',
        **LOG_HELPER_SETTINGS,
    }
)
def getSettingTree_whenThereAreNoneValuesAllOverThePlace() :
    TEST_AMOUNT = 16
    for index in range(TEST_AMOUNT) :
        # arrange
        noneValuesFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource', 'nonevalues', f'none-values{index}.yml'])
        exception = None

        # act
        try :
            toAssert = SettingHelper.getSettingTree(noneValuesFilePath)
            # log.prettyPython(getSettingTree_whenThereAreNoneValuesAllOverThePlace, f'{index}', toAssert, logLevel=log.DEBUG)
        except Exception as e :
            exception = e
            # print(f'{index}: {exception}')

        # assert
        assert ObjectHelper.isNotNone(exception)
        assert StringHelper.isNotBlank(str(exception))

    SECOND_TEST_AMOUNT = 31
    for index in range(TEST_AMOUNT, SECOND_TEST_AMOUNT) :
        # arrange
        noneValuesFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource', 'nonevalues', f'none-values{index}.yml'])
        exception = None

        # act
        try :
            toAssert = SettingHelper.getSettingTree(noneValuesFilePath)
            # log.prettyPython(getSettingTree_whenThereAreNoneValuesAllOverThePlace, f'{index}', toAssert, logLevel=log.DEBUG)
        except Exception as e :
            exception = e
            # print(f'{index}: {exception}')

        # assert
        assert ObjectHelper.isNone(exception)

    ENVIRONMENT_INJECTION = 7
    for index in range(ENVIRONMENT_INJECTION) :
        # arrange
        falbackFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource', 'nonevalues', f'import-from{index}.yml'])
        noneValuesFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource', 'nonevalues', f'the-one-to-import{index}.yml'])
        exception = None

        fallback = None

        assert 'yes.this.is.possible' == EnvironmentHelper.get('MIRACLE')

        # act
        try :
            fallback = SettingHelper.getSettingTree(falbackFilePath)
            toAssert = SettingHelper.getSettingTree(noneValuesFilePath, fallbackSettingFilePath=falbackFilePath, fallbackSettingTree=fallback)
            # log.prettyPython(getSettingTree_whenThereAreNoneValuesAllOverThePlace, f'{index}', toAssert, logLevel=log.DEBUG)
        except Exception as e :
            exception = e
            # print(fallback)
            print(f'{index}: {exception}')

        # assert
        assert ObjectHelper.isNone(exception)

    FAIL_ENVIRONMENT_INJECTION = 7
    for index in range(FAIL_ENVIRONMENT_INJECTION) :
        # arrange
        failFalbackFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource', 'nonevalues', f'fail-import-from{index}.yml'])
        failNoneValuesFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource', 'nonevalues', f'fail-the-one-to-import{index}.yml'])
        exception = None

        fallback = None

        # act
        try :
            failFallback = SettingHelper.getSettingTree(failFalbackFilePath)
            toAssert = SettingHelper.getSettingTree(failNoneValuesFilePath, fallbackSettingFilePath=failNoneValuesFilePath, fallbackSettingTree=failFallback)
            # log.prettyPython(getSettingTree_whenThereAreNoneValuesAllOverThePlace, f'{index}', toAssert, logLevel=log.DEBUG)
        except Exception as e :
            exception = e
            # print(fallback)
            # print(f'{index}: {exception}')

        # assert
        assert ObjectHelper.isNotNone(exception)
        assert StringHelper.isNotBlank(str(exception))

@Test(
    environmentVariables={
        'ENVIRONMENT_BOOLEAN_VALUE': True,
        log.ENABLE_LOGS_WITH_COLORS : True,
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS,
    }
)
def getBooleanSetting():
    # arrange
    defaultFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','boolean-application.yml'])
    localFilePath = str(EnvironmentHelper.OS_SEPARATOR).join(['python_helper', 'api', 'test', 'api', 'resource','boolean-application-local.yml'])

    # act
    falseValue = SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True)['boolean']['value']
    trueValue = SettingHelper.getSettingTree(localFilePath, keepDepthInLongString=True, fallbackSettingFilePath=defaultFilePath, fallbackSettingTree=SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True))['boolean']['value']
    environmentInjectionFalseValue = SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True)['boolean']['environment-injection']['value']
    environmentInjectionTrueValue = SettingHelper.getSettingTree(localFilePath, keepDepthInLongString=True, fallbackSettingFilePath=defaultFilePath, fallbackSettingTree=SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True))['boolean']['environment-injection']['value']
    isTrue = SettingHelper.getSettingTree(localFilePath, keepDepthInLongString=True, fallbackSettingFilePath=defaultFilePath, fallbackSettingTree=SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True))['boolean']['environment-injection']['is-true']
    shouldBeFalse = SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True)['boolean']['environment-injection']['this-is-true']
    shouldBeTrue = SettingHelper.getSettingTree(localFilePath, keepDepthInLongString=True, fallbackSettingFilePath=defaultFilePath, fallbackSettingTree=SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True))['boolean']['environment-injection']['this-is-true']

    thisIsAlsoTruePartial = SettingHelper.getSettingTree(localFilePath, keepDepthInLongString=True, fallbackSettingFilePath=defaultFilePath, fallbackSettingTree=SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True))
    thisIsAlsoFalsePartial = SettingHelper.getSettingTree(localFilePath, keepDepthInLongString=True, fallbackSettingFilePath=defaultFilePath, fallbackSettingTree=SettingHelper.getSettingTree(defaultFilePath, keepDepthInLongString=True))
    # print(thisIsAlsoTruePartial)
    # print(thisIsAlsoFalsePartial)

    thisIsAlsoTrue = thisIsAlsoTruePartial['boolean']['environment-injection']['this-is-also-true']
    thisIsAlsoFalse = thisIsAlsoFalsePartial['boolean']['environment-injection']['this-is-also-false']

    #assert
    assert trueValue, f'trueValue should be True with type bool, but is {trueValue} with type {type(trueValue)}'
    assert bool == type(trueValue), f'trueValue should be True with type bool, but is {trueValue} with type {type(trueValue)}'
    assert not falseValue, f'falseValue should be False with type bool, but is {falseValue} with type {type(falseValue)}'
    assert bool == type(falseValue), f'falseValue should be False with type bool, but is {falseValue} with type {type(falseValue)}'

    assert environmentInjectionTrueValue, f'environmentInjectionTrueValue should be True with type bool, but is {environmentInjectionTrueValue} with type {type(environmentInjectionTrueValue)}'
    assert bool == type(environmentInjectionTrueValue), f'environmentInjectionTrueValue should be True with type bool, but is {environmentInjectionTrueValue} with type {type(environmentInjectionTrueValue)}'
    assert not environmentInjectionFalseValue, f'environmentInjectionFalseValue should be False with type bool, but is {environmentInjectionFalseValue} with type {type(environmentInjectionFalseValue)}'
    assert bool == type(environmentInjectionFalseValue), f'environmentInjectionFalseValue should be False with type bool, but is {environmentInjectionFalseValue} with type {type(environmentInjectionFalseValue)}'

    assert isTrue, f'isTrue with type bool, but is {isTrue} with type {type(isTrue)}'
    assert bool == type(isTrue), f'isTrue with type bool, but is {isTrue} with type {type(isTrue)}'
    assert not shouldBeFalse, f'shouldBeFalse with type bool, but is {shouldBeFalse} with type {type(shouldBeFalse)}'
    assert bool == type(shouldBeFalse), f'shouldBeFalse with type bool, but is {shouldBeFalse} with type {type(shouldBeFalse)}'
    assert shouldBeTrue, f'shouldBeTrue with type bool, but is {shouldBeTrue} with type {type(shouldBeTrue)}'
    assert bool == type(shouldBeTrue), f'shouldBeTrue with type bool, but is {shouldBeTrue} with type {type(shouldBeTrue)}'

    assert thisIsAlsoTrue, f'thisIsAlsoTrue with type bool, but is {thisIsAlsoTrue} with type {type(thisIsAlsoTrue)}'
    assert bool == type(thisIsAlsoTrue), f'thisIsAlsoTrue with type bool, but is {thisIsAlsoTrue} with type {type(thisIsAlsoTrue)}'
    assert not thisIsAlsoFalse, f'thisIsAlsoFalse with type bool, but is {thisIsAlsoFalse} with type {type(thisIsAlsoFalse)}'
    assert bool == type(thisIsAlsoFalse), f'thisIsAlsoFalse with type bool, but is {thisIsAlsoFalse} with type {type(thisIsAlsoFalse)}'
