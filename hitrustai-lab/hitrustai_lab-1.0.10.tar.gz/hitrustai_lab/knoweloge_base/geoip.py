import maxminddb


class Geoip:
    def __init__(self, path):
        self.reader1 = maxminddb.open_database(path)

    def get_diia(self, ip):
        re = self.reader1.get(ip)['diia']
        return re

    def get_mmdb(self, ip):
        re = self.reader1.get(ip)
        return re
