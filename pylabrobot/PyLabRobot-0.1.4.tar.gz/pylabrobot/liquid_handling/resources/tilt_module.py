from abc import ABCMeta, abstractmethod
from typing import Optional

from pylabrobot.liquid_handling.resources.abstract import Coordinate, Resource

# TODO: move to separate file, maybe even a separate top level package.
# TODO: STAR should inherit from this, I think
class TiltModuleBackend(metaclass=ABCMeta):
  """ Abstract backend for tilt modules. """
  def __init__(self):
    self.setup_finished = False

  @abstractmethod
  def setup(self):
    self.setup_finished = True

  @abstractmethod
  def stop(self):
    self.setup_finished = False


class TiltModule(Resource):
  """ A tilt module """

  def __init__(
    self,
    name: str,
    backend: TiltModuleBackend,
    location: Coordinate = Coordinate(None, None, None)
  ):
    super().__init__(name=name, size_x=0, size_y=0, size_z=0,
      location=location, category="tilt_module")
    self._backend = backend

  def setup(self):
    self._backend.setup()

    # TODO: This is Hamilton specific
    self._backend.tilt_initialize()

  def stop(self):
    self._backend.stop()

  def move_to_absolute_position(self, position: float):
    """ """

    self._backend.tilt_move_to_absolute_position(position=position)

  def move_to_relative_position(self, steps: float):
    """ """

    self._backend.tilt_move_to_relative_position(steps=steps)

  def go_to_position(self, position: int):
    """ """

    self._backend.tilt_go_to_position(position=position)

  def set_speed(self, speed: int):
    """ """

    self._backend.tilt_set_speed(speed=speed)

  def power_off(self):
    """ """

    self._backend.tilt_power_off()

  def request_error(self) -> Optional[str]:
    """ """

    self._backend.tilt_request_error()

  def request_sensor(self) -> Optional[str]:
    """ """

    self._backend.tilt_request_sensor()

  def request_light_barrier_status(self) -> str:
    """ """

    self._backend.tilt_request_light_barrier_status()

  def request_status(self) -> str:
    """ """

    self._backend.tilt_request_status()

  def request_offset_between_light_barrier_and_init_position(self) -> int:
    """ """

    self._backend.tilt_request_offset_between_light_barrier_and_init_position()

  def request_module_name(self) -> str:
    """ """

    self._backend.tilt_request_module_name()

  def port_set_opent_collector(self, open_collector: int):
    """ """

    self._backend.tilt_port_set_opent_collector(open_collector=open_collector)

  def port_clear_open_collector(self, open_collector: int):
    """ """

    self._backend.tilt_port_clear_open_collector(open_collector=open_collector)

  def set_temperature(self, temperature: float):
    """ """

    self._backend.tilt_set_temperature(temperature=temperature)

  def switch_off_temperature_controller(self):
    """ """

    self._backend.tilt_switch_off_temperature_controller()

  def set_drain_time(self, drain_time: float):
    """ """

    self._backend.tilt_set_drain_time(drain_time=drain_time)

  def set_waste_pump_on(self):
    """ """

    self._backend.tilt_set_waste_pump_on()

  def set_waste_pump_off(self):
    """ """

    self._backend.tilt_set_waste_pump_off()

  def set_name(self, name: str):
    """ """

    self._backend.tilt_set_name()

  def switch_encoder(self, on: bool):
    """ """

    self._backend.tilt_switch_encoder(on=on)

  def initial_offset(self, offset: int):
    """ """

    self._backend.tilt_initial_offset(offset=offset)
