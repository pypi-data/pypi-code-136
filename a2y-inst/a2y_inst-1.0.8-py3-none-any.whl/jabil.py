from typing import List


class Measurement:
	def __init__(self, name: str, result: bool = True, value=None, date_time: str = ''):
		self.name = name
		self.result = result
		self.value = value
		self.date_time = date_time

	def is_ok(self):
		return self.result

	def is_ng(self):
		return not self.is_ok()

	@property
	def result_str(self) -> str:
		return 'Pass' if self.result else 'Fail'


class Tar:
	def __init__(
			self, serial_number: str = 'NoSerial', customer='', board_style='', tester_name='',
			test_process='', fixture_slot=1, assembly_number='', assembly_revision='',
			firmware_revision='', test_status='P', line='1',
			**kwargs
	):
		self.test_process = test_process
		self.test_status = test_status

		self.serial_number = serial_number
		self.customer = customer
		self.board_style = board_style
		self.tester_name = tester_name
		self.fixture_slot = fixture_slot
		self.assembly_number = assembly_number
		self.assembly_revision = assembly_revision
		self.firmware_revision = firmware_revision
		self.line = line
		self.fail_message = ''
		self.measurements: List[Measurement] = []
		self.kwargs = kwargs

	def load_test_report(self, measurements: List[Measurement], aborted: bool = False):
		if aborted:
			self.test_status = 'A'

		for measurement_raw in measurements:
			measurement: Measurement = measurement_raw
			if self.test_status == 'P' and measurement.is_ng():
				self.test_status = 'F'
				self.fail_message = measurement.name
		self.measurements = measurements

	def generate(self, filename: str):
		LE = '\n'
		start_date = ''
		stop_date = ''
		for measurement in self.measurements:
			if start_date == '' or measurement.date_time < start_date:
				start_date = measurement.date_time
			if stop_date < measurement.date_time:
				stop_date = measurement.date_time
		with open(filename, 'w') as f:
			f.write('S%s%s' % (self.serial_number, LE))
			f.write('C%s%s' % (self.customer, LE))
			f.write('B%s%s' % (self.board_style, LE))
			f.write('N%s%s' % (self.tester_name, LE))
			f.write('P%s%s' % (self.test_process, LE))
			f.write('s%s%s' % (self.fixture_slot, LE))
			f.write('n%s%s' % (self.assembly_number, LE))
			f.write('r%s%s' % (self.assembly_revision, LE))
			f.write('W%s%s' % (self.firmware_revision, LE))
			f.write('T%s%s' % (self.test_status, LE))
			f.write('L%s%s' % (self.line, LE))

			for key, value in self.kwargs.items():
				f.write(f'{key}{value}{LE}')

			f.write('[%s%s' % (start_date, LE))
			f.write(']%s%s' % (stop_date, LE))
			if self.test_status == 'F':
				f.write('F%sM%s%s' % (LE, self.fail_message, LE))

			for measurement_raw in self.measurements:
				measurement: Measurement = measurement_raw
				f.write('M%s%s' % (measurement.name, LE))
				if measurement.value is not None and measurement.value != '':
					f.write('d%s%s' % (measurement.value, LE))
				else:
					f.write('d%s%s' % (measurement.result_str, LE))
