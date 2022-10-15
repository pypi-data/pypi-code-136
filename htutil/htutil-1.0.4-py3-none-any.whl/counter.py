'''
Author: HaoTian Qi
Date: 2021-03-22 09:41:32
Description: Counter
LastEditTime: 2021-04-08 15:10:28
LastEditors: HaoTian Qi
FilePath: \htutil\htutil\counter.py
'''
class Counter():
    def add(self, object):
        if object in self.__dict__:
            self.__dict__[object] += 1
        else:
            self.__dict__[object] = 1

    def to_dict(self):
        return self.__dict__

    def dump(self):
        print(self.__dict__)


def main():
    c = Counter()
    c.add('1')
    c.add('1')
    c.add('2')

    print(c.to_dict())

    c.dump()

if __name__ == '__main__':
    main()
