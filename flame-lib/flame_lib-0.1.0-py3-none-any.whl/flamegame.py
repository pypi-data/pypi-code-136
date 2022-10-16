from math import remainder


class Flamegame:
    def __init__(self,your_name):
        self.your_name = your_name.lower()
    def do_flames(self,cr_name):
        cr_name = cr_name.lower()
        if self.your_name == cr_name:
            return "Can't do flames with the same name"
        if cr_name == '':
            remain_count = len(self.your_name)
            test = "FLAME"
            ch = test[(remain_count-1)%5]
            if ch == 'F':
                return 'Friendship'
            if ch == 'L':
                return 'Lovers'
            if ch == 'A':
                return 'Affection'
            if ch == 'M':
                return 'Marriage'
            if ch == 'E':
                return 'Enemy'
        cr_set = set(cr_name)
        y_set = set(self.your_name)
        common_set = y_set.intersection(cr_set)
        y_dict, cr_dict = {}, {}

        for ch in self.your_name:
            y_dict[ch] = y_dict.get(ch, 0) + 1
        for ch in cr_name:
            cr_dict[ch] = cr_dict.get(ch, 0) + 1
        
        y_count, cr_count = 0, 0
        for key in y_dict:
            if key not in common_set:
                y_count = y_count + 1
        for key in cr_dict:
            if key not in common_set:
                cr_count = cr_count + 1

        test = "FLAME"
        remain_count = y_count + cr_count
        ch = test[(remain_count-1)%5]
        if ch == 'F':
            return 'Friendship'
        if ch == 'L':
            return 'Lovers'
        if ch == 'A':
            return 'Affection'
        if ch == 'M':
            return 'Marriage'
        if ch == 'E':
            return 'Enemy'