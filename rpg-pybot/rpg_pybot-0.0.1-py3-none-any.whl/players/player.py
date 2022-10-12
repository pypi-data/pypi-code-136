from random import randint


class Player:
    def __init__(self, name):
        self._name = str(name)
        self._classe = "classless"
        self._hp = 100
        self._mp = 100
        self._df = 2
        self._atk = 2
        self._level = 1
        self._xp = 0
        self.special_attack = "Punch"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    def __str__(self):
        return f"NAME: {self._name}\n\tLEVEL: {self._level}\n\tCLASS: {self._classe}\n\tEXP: {self._xp}\n\tHP: {self._hp}\n\tMP: {self._mp}\n\tATK: {self._atk}\n\tDEF: {self._df}\n"

    def player_data(self):
        return print(f"NAME: {self._name}\n\tLEVEL: {self._level}\n\tCLASS: {self._classe}\n\tEXP: {self._xp}\n\tHP: {self._hp}\n\tMP: {self._mp}\n")

    def set_char_class(self, class_number):

        try:
            if int(class_number) >= 0 or int(class_number) <= 3:

                if int(class_number) == 0:
                    self._classe = "Barbarian"
                    self._hp = 200
                    self._mp = 60
                    self._atk = 4
                    self._df = 8
                    self.special_attack = "Bersek Assault"
                elif int(class_number) == 1:
                    self._classe = "Rogue"
                    self._hp = 50
                    self._mp = 50
                    self._atk = 8
                    self._df = 8
                    self.special_attack = "Stealth Attack"
                elif int(class_number) == 2:
                    self._classe = "Warrior"
                    self._hp = 120
                    self._mp = 50
                    self._atk = 5
                    self._df = 5
                    self.special_attack = "Sword Stroke"
                elif int(class_number) == 3:
                    self._classe = "Mage"
                    self._hp = 80
                    self._mp = 200
                    self._atk = 6
                    self._df = 1
                    self.special_attack = "Fire Ball"

        except:
            print("Invalid command")

    @classmethod
    def classe_roll(self):
        return randint(1, 20)

    def attack(self, enemy):
        try:
            if type(enemy) is self.__class__:
                enemy.deffend((self._atk + self.classe_roll()))
                print(f"{self.name} uses {self.special_attack} in {enemy.name}")
                print(f"{enemy.name} HP: {enemy._hp}")
        except:
            print("Invalid command attack")

    def deffend(self, damage):
        defesa = (self._df + self.classe_roll())
        if damage >= defesa:
            self._hp -= (damage - defesa)
        else:
            self._hp -= 1



