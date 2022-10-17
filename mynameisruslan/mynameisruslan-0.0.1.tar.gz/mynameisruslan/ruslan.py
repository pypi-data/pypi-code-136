class RuslanEngineer:
	"""
	คลาส RuslanEngineer คือ
	เป็นข้อมูลที่เกี่ยวข้องกับ รุสลัน
	ประกอบด้วยชื่อเพจ
	ชื่อช่องยูทูป

	Example:
	# --------------------------
	ruslan = RuslanEngineer()
	ruslan.show_name()
	ruslan.show_google()
	ruslan.about()
	ruslan.show_art()
	# --------------------------

	"""
	def __init__(self):
		self.name = 'รุสลันวิศวกร PLC'
		self.page = 'https://www.google.co.th'

	def show_name(self):
		print('สวัสดีฉันชื่อ {}'.format(self.name))

	def show_google(self):
		print('https://www.google.co.th')

	def about(self):
		text = """
		----------------------------------
		สวัสดี นี่คือลันเอง เป็นคนเขียน PLC siemens 
		สามารถติตามได้เลย ท่านจะได้รับความรู้เกี่ยวกับ 
		การเขียนโปรแกรม PLC
		----------------------------------"""
		print(text)

	def show_art(self):
		text = """
			⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣶⠶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀ 
	⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⠁⠀⢀⠈⢿⢀⣀⠀⠹⣿⣿⣿⣦⣄⠀⠀⠀ 
	⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⠿⠀⠀⣟⡇⢘⣾⣽⠀⠀⡏⠉⠙⢛⣿⣷⡖⠀ 
	⠀⠀⠀⠀⠀⣾⣿⣿⡿⠿⠷⠶⠤⠙⠒⠀⠒⢻⣿⣿⡷⠋⠀⠴⠞⠋⠁⢙⣿⣄ 
	⠀⠀⠀⠀⢸⣿⣿⣯⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠉⢹⡄⠀⠀⠀⠛⠛⠋⠉⠹⡇ 
	⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣼⣇⣀⣀⣀⣛⣛⣒⣲⢾⡷ 
	⢀⠤⠒⠒⢼⣿⣿⠶⠞⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⠃ 
	⢮⠀⠀⠀⠀⣿⣿⣆⠀⠀⠻⣿⡿⠛⠉⠉⠁⠀⠉⠉⠛⠿⣿⣿⠟⠁⠀⣼⠃⠀ 
	⠈⠓⠶⣶⣾⣿⣿⣿⣧⡀⠀⠈⠒⢤⣀⣀⡀⠀⠀⣀⣀⡠⠚⠁⠀⢀⡼⠃⠀⠀ 
	⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣭⣭⣭⣭⣭⣥⣤⣤⣤⣴⣟⠁
		"""
		print(text)

if __name__ == '__main__':
	ruslan = RuslanEngineer()
	ruslan.show_name()
	ruslan.show_google()
	ruslan.about()
	ruslan.show_art()


