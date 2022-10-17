import os

version='1.0'

def find_moudle(code_name='code.py'):
	global moudle_list
	if os.path.isdir('moudle'):
		moudle_list=os.listdir('moudle')
		moudle_l=''
		for moudle in moudle_list:
			moudle_l=moudle_l+moudle
		moudle_list=moudle_l.split('.py')
		open(code_name,'w').write('#Made with handongliren\'s MoudleSystem.\n\ndef run():\n' )
		del(moudle_list[-1])
		print('moudle:',moudle_list)

def import_moudle(code_name='code.py'):
	if os.path.isfile(code_name):
		if not open(code_name,'r').read()=='':
			for moudle in moudle_list:
				code_a=open(code_name,'a')
				code_a.write('	from moudle import '+moudle+'\n')
			code_a.write('\n')				

def run_moudle(code_name='code.py'):
	if os.path.isfile(code_name):
		if not open(code_name,'r').read()=='':
			open(code_name,'r')
			for moudle in moudle_list:
				code_a=open(code_name,'a')
				code_a.write('	'+moudle+'.run()\n')

def moudle_code(code_name='code.py'):
	find_moudle(code_name)
	import_moudle(code_name)
	run_moudle(code_name)
