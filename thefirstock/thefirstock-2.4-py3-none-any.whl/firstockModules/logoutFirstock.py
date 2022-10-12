from thefirstock.firstockModules.logoutFunctionality.execution import *


def firstock_logout():
    try:
        logout = FirstockLogout().firstockLogout()
        return logout

    except Exception as e:
        print(e)
