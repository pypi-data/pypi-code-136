import itertools
import threading

def sip(iterable, block_size):
  """Sips a fixed size from the iterable."""
  ct = 0
  block = []

  for x in iterable:
    ct += 1
    block.append(x)
    if ct == block_size:
      yield block
      ct = 0
      block = []

  if len(block) > 0:
    yield block


def run():
	all_items = []
	for _ in range(500):
		items = ( (100000000,212213123212) for _ in range(20000) )
		all_items = itertools.chain(all_items, items)

	for i in sip(all_items, 500000):
		print(i)


t = threading.Thread(target=run)
t.start()

t.join()