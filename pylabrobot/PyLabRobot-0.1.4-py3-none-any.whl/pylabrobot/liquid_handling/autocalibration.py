
def autocalibrate(initial_volume, measure, target_volume, max_delta):
  """ Autocalibrate volume correction curve.

  Assumes the relation between the volume and measured target volume is (near) linear.

  Args:
    initial_volume: volume to start testing with
    measure: function to compute target_volume, like a plate or weight reading.
    target_volume: target volume, like a target weight or plate
    max_delta: maximum acceptable difference between reading and target volume.
  """

  # TODO: specify source/target wells, handle aspirate commands. stuff like that.

  volume = initial_volume
  measured = measure()
  while abs(measured - target) > max_delta:
    volume = (target_volume/measure) * volume
    # move new volume.
    measured = measure()
  return volume

# Usage:
# autocalibrate(1, measure, target_volume, max_delta)
