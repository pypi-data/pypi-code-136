import threading
from datetime import datetime, timedelta
from uuid import uuid4


class GetHistoryData:
  data_available_from = datetime.fromisoformat('2017-05-01')
  today = datetime.today()
  yesterday = today - timedelta(days=1)

  def __init__(self, client, symbol, range_from, range_to):
    self.client = client
    self.symbol = symbol
    self.range_from = datetime.fromisoformat(range_from)
    self.range_to = datetime.fromisoformat(range_to)
    self.results = []

  def generate_payload(symbol, range_from, range_to):
    return {
      "symbol": symbol,
      "resolution": "1",
      "date_format": 1,
      "range_from": range_from,
      "range_to": range_to,
      "cont_flag":"1"
    }

  def get_ranges(self):
    def generate_fetch_from_date(fetch_to_date):
      return fetch_to_date + timedelta(days=1)

    def generate_fetch_to_date(fetch_from_date):
      next_date = fetch_from_date + timedelta(days=100)
      return self.range_to if next_date > self.range_to else next_date

    ranges = []

    while True:
      last_fetch_date = ranges[-1]['fetch_to_date'] if len(ranges) else self.range_from - timedelta(days=1)

      if last_fetch_date >= self.range_to:
        break
      else:
        ranges.append({
          'fetch_from_date': generate_fetch_from_date(last_fetch_date), 
          'fetch_to_date': generate_fetch_to_date(last_fetch_date)
        })

    return ranges

  def generate_tasks(self):
    tasks = []

    chunks = self.get_ranges()

    for chunk in chunks:
      tasks.append({
        'id': uuid4().hex,
        'symbol': self.symbol, 
        'fetch_from_date': chunk['fetch_from_date'].strftime('%Y-%m-%d'), 
        'fetch_to_date': chunk['fetch_to_date'].strftime('%Y-%m-%d'),
      })

    return tasks

  def generate_data_json(self, task):
    payload = self.generate_payload(
      task['symbol'], (task['fetch_from_date']).strftime('%Y-%m-%d'), (task['fetch_to_date']).strftime('%Y-%m-%d')
    )

    data = self.client.history(payload)

    self.results.extend(data['candles'])

  def download(self):
    if self.range_from.strftime('%Y-%m-%d') < self.data_available_from.strftime('%Y-%m-%d'):
      return {'error': 'Data only available from %s' % self.data_available_from.strftime('%Y-%m-%d')}
      
    if self.range_to.strftime('%Y-%m-%d') > self.yesterday.strftime('%Y-%m-%d'):
      return {'error': 'History Data only available upto %s' % self.yesterday.strftime('%Y-%m-%d')}

    tasks = self.generate_tasks()

    for task in tasks:
      download_thread = threading.Thread(target=self.generate_data_json, args=(task,))

      download_thread.start()
      download_thread.join()

    return {'results': self.results}
