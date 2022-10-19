import json
import time
import datetime as dt
from granturismo.intake import Listener
from pathlib import Path
from argparse import ArgumentParser

def parseargs():
  parser = ArgumentParser()
  parser.add_argument('-t', '--track', type=str, required=True,
                    help='The track name as it appears in Gran Truismo')
  return parser.parse_args()


if __name__ == '__main__':
  odir = Path('./data/trackDataRaw')
  odir.mkdir(parents=True, exist_ok=True)
  track_id = len(list(odir.glob('*.json')))

  count = 0
  race_started = False
  finished = False
  #args = parseargs()
  track_name = 'Autódromo de Interlagos' #args.track
  layout = None

  packets = []
  listener = Listener('192.168.1.207')

  if layout is not None:
    print(f'[{track_name} - {layout}]')
  else:
    print(f'[{track_name}]')
  print(f'\tWaiting for race to start')


  while True:
    try:
      packet = listener.get()
    except TimeoutError as e:
      continue

    # time trials will have lapsInRace == 0
    # circuit experience sectors will have lapsInRace == 1 && lapCount == 2
    # menu screen will have lapCount == 65535
    curr_time = dt.datetime.fromtimestamp(time.time()).isoformat()
    if packet.flags.loading_or_processing:
      print(f'[{curr_time}] loadingOrProcessing')
      in_race = False
    elif packet.lap_count == 1 and packet.laps_in_race == 0: # were in a time trial first lap
      print(f'[{curr_time}] lapCount:[{packet.lap_count}] && lapsInRace:[{packet.laps_in_race}]')
      in_race = True
    else:
      in_race = packet.lap_count is None \
          and (packet.lap_count <= 1) \
          and (packet.laps_in_race > 0 and
        packet.laps_in_race >= packet.lap_count)


    if not in_race and not race_started:
      # race hasn't started yet!
      continue

    if in_race and not race_started:
      # the race has started!
      print(f'\tRace started! capturing packets now')
      race_started = True

    if not in_race and finished:
      # we've already saved the packets
      continue

    if not in_race and race_started and not finished:
      if count < 10:
        print(f'\tFalse start. Resetting conditions. packetCount:[{count}]')
        count = 0
        finished = False
        race_started = False
        continue

      # the race ended, save the data
      _packets = list(filter(lambda p: p['lapCount'] == 1, packets))
      print(f'\tRace ended. Captured {len(_packets)}. Saving telemetry data')
      filename = odir.joinpath(f'{track_name} - {layout}.json') if layout is not None else odir.joinpath(f'{track_name}.json')
      print(f'\tWriting to file {filename}')
      with open(filename, 'w') as f:
        json.dump({
          'track': {
            'id': track_id,
            'name': track_name,
            'layout': layout,
          },
          'packets': _packets
        }, f)
      finished = True
      break

    packets.append({
      'position': packet['position'],
      'orientation': packet['orientation'],
      'lapCount': packet['lapCount']
    })
    count += 1