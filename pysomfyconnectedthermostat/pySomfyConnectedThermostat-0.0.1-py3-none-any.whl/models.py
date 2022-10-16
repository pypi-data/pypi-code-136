from time import time

class Principal:
  def __init__(self, id: int, first_name: str, last_name: str, email: str):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.email = email

class Thermostat:
  def __init__(self, id: str, name: str):
    self.id = id
    self.name = name

class Smartphone:
  def __init__(self, name: str, vendor_id: str, push_token: str):
    self.name = name
    self.vendor_id = vendor_id
    self.push_token = push_token

class ThermostatInfo:
  def __init__(self, temperature: float, temperature_consigne: float, battery: int, mode: str):
    self.temperature = temperature
    self.temperature_consigne = temperature_consigne
    self.battery = battery
    self.mode = mode

class ThermostatCommand:
  def __init__(self, heating_mode: str, derogation_type: str, duration: int, started_at: int, finish_at: int, target_temperature: float):
    self.heating_mode = heating_mode
    self.derogation_type = derogation_type
    self.duration = duration
    self.started_at = started_at
    self.finish_at = finish_at
    self.target_temperature = target_temperature

class SetTemperatureCommand:
  def __init__(self, target_temperature: float, derogation_type: str = 'next_mode'):
    ThermostatCommand.__init__(
      self,
      heating_mode= 'manuel',
      derogation_type= derogation_type,
      duration= None,
      started_at= None,
      finish_at= None,
      target_temperature= target_temperature,
    )

class SetTemperatureWithDurationCommand:
  def __init__(self, target_temperature: float, duration: int):
    ThermostatCommand.__init__(
      self,
      heating_mode= 'manuel',
      derogation_type= 'none',
      duration= duration,
      started_at= time(),
      finish_at= time() + duration,
      target_temperature= target_temperature,
    )

class ResetDerogationCommand:
  def __init__(self):
    ThermostatCommand.__init__(
      self,
      heating_mode= 'at_home',
      derogation_type= 'none',
      duration= 0,
      started_at= 0,
      finish_at= 0,
      target_temperature= 0,
    )

class SetHeatingModeCommand:
  def __init__(self, heating_mode: str):
    ThermostatCommand.__init__(
      self,
      heating_mode= heating_mode,
      derogation_type= 'none',
      duration= 0,
      started_at= None,
      finish_at= None,
      target_temperature= None,
    )