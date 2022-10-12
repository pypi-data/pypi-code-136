from thefirstock.firstockModules.loginFunctionality.execution import *


def firstock_login(userId, password, DOBnPAN, vendorCode, apiKey):
    try:
        login = FirstockLogin(
            uid=userId,
            pwd=password,
            factor2=DOBnPAN,
            vc=vendorCode,
            appkey=apiKey,
        )

        result = login.firstockLogin()

        return result

    except Exception as e:
        print(e)
