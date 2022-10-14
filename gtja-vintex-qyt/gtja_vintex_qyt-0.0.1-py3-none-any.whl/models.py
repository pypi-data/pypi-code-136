import json


class GTJAVintexQytResult:
    def __init__(self, response: str):
        self.content = response
        self.json = json.loads(self.content)

        self.data = []
        self.code = self.json['code']
        self.msg = self.json['msg']
        self.total = self.json['total']


class Securities:
    def __init__(self,
                 firstdroptype: str,
                 vc_type: str,
                 qcid: str,
                 qcname: str,
                 dropid: str,
                 market: str,
                 stkcode: str,
                 stkname: str,
                 totalleftqty: int,
                 totallockqty: int,
                 startdate: str,
                 limitdate: str,
                 reslimit: int,
                 floorrate: str,
                 upperrate: str,
                 relatedcustid: str,
                 contractid: str,
                 applyid: str
                 ):
        self.firstdroptype = firstdroptype
        self.vc_type = vc_type
        self.qcid = qcid
        self.qcname = qcname
        self.dropid = dropid
        self.market = market
        self.stkcode = stkcode
        self.stkname = stkname
        self.totalleftqty = totalleftqty
        self.totallockqty = totallockqty
        self.startdate = startdate
        self.limitdate = limitdate
        self.reslimit = reslimit
        self.floorrate = floorrate
        self.upperrate = upperrate
        self.relatedcustid = relatedcustid
        self.contractid = contractid
        self.applyid = applyid


class SecuritiesSummary:
    def __init__(self,
                 stkcode: str,
                 stkname: str,
                 market: str,
                 actualleftqty: int,
                 floorrate: str,
                 startdate: str):
        self.stkcode = stkcode
        self.stkname = stkname
        self.market = market
        self.actualleftqty = actualleftqty
        self.floorate = floorrate
        self.startdate = startdate


