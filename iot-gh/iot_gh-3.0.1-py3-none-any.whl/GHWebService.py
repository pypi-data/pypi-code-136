import time
from iot_gh.src.iot_gh.IoTGreenhouse import IoTGreenhouse
from iot_gh.src.iot_gh.AirTable import AirTable

class GHWebService(object):
    """ Web connector for REST service. 
    Post data using json package.
    V3
    10/16/2022
    """
    POST_DELAY = 5     #Seconds between posts - throttle
    DATA_TABLE_NAME = 'GreenhouseData'
    LOGS_TABLE_NAME = 'GreenhouseLogs'
    
    def __init__(self, ws_url, api_key, base_key):
        self.ws_url = ws_url
        self.api_key = api_key
        self.base_key = base_key
        self.data_table = AirTable(ws_url=ws_url,base_key=base_key, api_key=api_key,table_name=self.DATA_TABLE_NAME)
        self.logs_table = AirTable(ws_url=ws_url,base_key=base_key, api_key=api_key,table_name=self.LOGS_TABLE_NAME)
        self.last_post_time = time.time() - 3

    def get_greehhouse(self, id:str=None, name:str=None) -> IoTGreenhouse:
        if id:
            record = self.data_table.get_record(id=id)
        elif name:
            records = self.data_table.get_records_by_search("Name", name)
            record = records[0]
        else:
            return None
        
        gh = IoTGreenhouse()
        self._fill(gh, record)
        return gh
        
    def post_greenhouse(self, gh:IoTGreenhouse, throttle=True):
        #throttle post
        if not throttle or time.time() > self.last_post_time + self.POST_DELAY:
            if gh.id:
                record = self._make_record(gh)
                record = self.data_table.update_record(record)
            else:
                fields = self._make_fields(gh)
                record = self.data_table.add_record(fields)

            self._fill(gh, record)
            self.last_post_time = time.time()      

    def delete_greenhouse(self, gh:IoTGreenhouse):
        if gh.id:
            record = self._make_record(gh)
            self.data_table.delete_record(record)


    def _make_record(self, gh:IoTGreenhouse) -> dict:
        record = {"id": gh.id, "fields": self._make_fields(gh)}
        return record

    def _make_fields(self, gh:IoTGreenhouse) -> dict:    
        fields = {}
        if gh.name:
            fields["Name"] = gh.name
        if gh.temp_inside_F:
            fields["Temp In"] = gh.temp_inside_F
        if gh.temp_outside_F:
            fields["Temp Out"] = gh.temp_outside_F
        if gh.servo_status:
            fields["Servo Status"] = gh.servo_status
        if gh.fan_status:
            fields["Fan Status"] = gh.fan_status
        if gh.led_white_status:
            fields["Heater Status"] = gh.led_white_status
        if gh.message:
            fields["Message"] = gh.message
        return fields

    def _update_record(self, record:dict, gh:IoTGreenhouse):
        record["Temp In"] = gh.temp_inside_F,
        record["Temp Out"] = gh.temp_outside_F,
        record["Servo Status"] = gh.servo_status,
        record["Fan Status"] = gh.fan_status,
        record["Heater Status"] = gh.led_white_status,  #white led simulates heater
        record["Message"] = gh.message
        
    def _fill(self, gh:IoTGreenhouse, record:dict) -> None:
        gh.id = record["id"]
        gh.ID = record["fields"].get("ID")
        gh.name =  record["fields"].get("Name")
        gh.temp_inside_F = record["fields"].get("Temp In")
        gh.temp_outside_F = record["fields"].get("Temp Out")
        gh.servo_status = record["fields"].get("Servo Status")
        gh.fan_status = record["fields"].get("Fan Status")
        gh.led_white_status = record["fields"].get("Heater Status")
        gh.message = record["fields"].get("Message")