from StevenTricks.dictur import findstr
from warren.conf.twse import collection


class Packet:
    def __init__(self, title):
        # title is the target type of stock
        self.title = title
        self.packet = collection[title]

    def payload(self, datemin=None):
        # datemin is the minimum of title
        # Firstly find the date key of payload
        datekey = findstr(self.packet, 'date')
        if len(datekey) == 1:
            datekey = datekey[0]
        else:
            print(self.packet, '/n________')
            print(datekey, '/n________/ndatekey length shouldn\'t greater than 1')
            return 'PacketValueError'

        # if you don't assign the date, give the date_min. Or give the specific date.
        if cal is None:
            self.packet['payload'][datekey] = self.packet['date_min']
        else:
            self.packet['payload'][datekey] = datemin

        return self.packet['payload']


if __name__ == '__main__':
    pass