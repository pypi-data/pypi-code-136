import sys


class Sambura:
    def __init__(self, dico: dict):
        """
        user = {
            
            "name of user": "john", 

            "f_name": "Doe", 

            "age": 26, 

            "47th zone": "USA"

        }
        with Sambura(user): import f_name, age, name_of_user, _47th_zone

        print(name_of_user) #=> jonn

        print(age) #=> 26

        print(_47th_zone) #=> USA
        """
        self.dico = dico

    def __enter__(self):
        if not isinstance(self.dico, dict):
            self.dico = self.dico.__dict__

        self.dico = {
            **{str(k).replace(" ", "_"): v for k, v in self.dico.items()},
            **{
                "_" + str(k).replace(" ","_"): v
                for k, v in self.dico.items()
                if str(k).isnumeric() or str(k)[0].isdigit()
            },
        }

        self.sysmodules = sys.modules
        sys.modules = self.dico
        return sys.modules

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.modules = self.sysmodules