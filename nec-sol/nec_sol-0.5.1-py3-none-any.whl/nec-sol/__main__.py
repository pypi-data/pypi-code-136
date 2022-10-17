from collections import OrderedDict
from simple_term_menu import TerminalMenu
import getpass
import platform
import re
import requests
import subprocess
import sys
import urllib.parse
import json
import os
import traceback
import argparse
from typing import Union, List, Tuple, Optional, Dict, Set, Any

#-------------------------------------------------------------------------------
class Plugin:
	def __init__(self, name: str, version: str, url: Optional[str] = None, dependencies: Optional[List[str]] = []):
		if not(version is None or version.startswith(('<=', '>=', '==', '~='))):
			raise Exception(f'invalid version detected: {version}')

		self.name			= name
		self.version		= version
		self.url			= url
		self.dependencies	= dependencies
		
	def __repr__(self):
		return f'[Plugin name={self.name}, version={self.version}, url={self.url}, dependencies={self.dependencies}]'

L_EMPH  	= "\033[1m"
L_ERROR		= "\033[0;31m"
L_SUCCESS	= "\033[0;32m"
L_RESET 	= "\033[0m"

s_access			= None
s_available			= None
s_installed			= None
s_prefix			= None
s_license_version	= None
s_version			= None
s_dependencies		= None
s_python_packages	= None
s_default_versions	= None

#-------------------------------------------------------------------------------
# taken from: https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv
def is_virtualenv():
	return (hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

#-------------------------------------------------------------------------------
def run(cmd):
	ret = subprocess.run(cmd)
	if ret.returncode != 0:
		raise Exception("PIP error detected")

#-------------------------------------------------------------------------------
def run_output(cmd: Union[List[str], Tuple[str]]) -> str:
	ret = subprocess.run(cmd, stdout=subprocess.PIPE)
	if ret.returncode != 0:
		raise Exception("PIP error detected")
	return ret.stdout.decode('utf-8')

#-------------------------------------------------------------------------------
def initialize():
	global s_prefix, s_version, s_license_version, s_available, s_access, s_python_packages, s_installed, s_dependencies

	# Open Config File ---------------------------------------------------------
	with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as f:
		data = json.load(f)
		assert isinstance(data, dict)
		s_prefix			= data.get('prefix')
		s_version			= data.get('version')
		s_license_version	= data.get('license_version')
		s_default_versions	= data.get('default_versions')
		s_available			= list()
		s_access			= set()
		for plugin in data.get('plugins'):
			p = Plugin(*plugin)
			s_available.append(p)
			if p.url: # None == PyPI
				s_access.add(p.url)

	# Init Available Modules ---------------------------------------------------
	output				= run_output(['python3', '-m', 'pip', 'list', 'installed'])
	s_python_packages	= output.split('\n')[2:]
	s_installed			= dict()
	prog				= re.compile(r'^({}-sol[a-z0-9-]+)\s+([0-9\.a-z]+)'.format(s_prefix))
	for x in s_python_packages:
		match = prog.match(x)
		if match:
			s_installed[match[1]] = match[2]

	# Init Available Hardware --------------------------------------------------
	s_dependencies = dict()

	if args.devices == ['all']:
		def add_device(name, func, force=False):
			global s_dependencies
			s_dependencies[name] = None
	else:
		def add_device(name, func, force=False):
			global s_dependencies

			try:
				if func() if force or len(args.devices) == 0 else args.devices.index(name) >= 0:
					s_dependencies[name] = None
			except ValueError:
				pass

	add_device('x86_64',	lambda: platform.machine() == 'x86_64', True)
	add_device('ve',		lambda: os.path.exists('/sys/class/ve'))
	add_device('nvidia',	lambda: os.path.exists('/proc/driver/nvidia/version'))

	dev_cnt = len(s_dependencies)
	if dev_cnt == 0:
		raise Exception('No devices detected or selected via --devices!')
		
	# Init Available Frameworks ------------------------------------------------
	available_frameworks = ['torch', 'tensorflow', 'numpy', 'onnx']
	if len(args.frameworks) == 0: # auto
		args.frameworks = available_frameworks
	else:
		if args.frameworks == ['all']:
			args.frameworks = available_frameworks

		regex = re.compile(r'([a-zA-Z0-9\-]+)\s*(==|<=|>=|~=)?\s*([0-9\.]+(\.post[0-9]+)?)?')

		for d in args.frameworks:
			match = regex.search(d)

			if match is None:
				raise Exception(f'Unsupported framework: {d}')

			name, operator, version = match[1], match[2], match[3]

			if name not in available_frameworks:
				raise Exception(f'Unsupported framework: {d}')

			s_dependencies[name] = None if operator is None and version is None else f'{operator}{version}'

	# Determine Framework versions
	for x in s_python_packages:
		x = x.split(' ')
		d, v = x[0], x[-1]
		if d in args.frameworks:
			s_dependencies[d] = f'=={v}'

	if (len(s_dependencies) - dev_cnt) == 0:
		raise Exception('No frameworks detected or selected via --frameworks!')

	# Init default versions to prevent PIP to try hundreds of combinations
	for k, v in s_default_versions.items():
		if s_dependencies.get(k, False) is None: # False == not found, don't set, None == found but no version specified or found
			s_dependencies[k] = v

#-------------------------------------------------------------------------------
# Callbacks
#-------------------------------------------------------------------------------
def install(args):
	# Run PIP installation -----------------------------------------------------
	is_install	= args.mode != 'download'
	is_local	= args.folder != None

	credentials, user_access = None, None
	if not is_local:
		credentials, user_access = check_license(args)
	
	# Get list of plugins to be installed --------------------------------------
	plugins = available_plugins(args, user_access)

	# uninstall all previous packages ------------------------------------------
	if is_install and len(s_installed) > 0:
		uninstall(args)

	cmd = ['python3', '-m', 'pip', 'install' if is_install else 'download']

	if is_install and not is_virtualenv() and args.user:
		cmd.append('--user')

	for p in plugins:
		assert isinstance(p, Plugin)
		x = p.name
		if p.version is not None:
			x = f'{x}{p.version}'
		cmd.append(x)

	if is_local:
		cmd.append('--no-index')
		cmd.append('-f')
		cmd.append(args.folder)
	else:
		assert isinstance(credentials, tuple) and len(credentials) == 2

		if args.trust:
			cmd.append('--trusted-host')
			cmd.append('sol.neclab.eu')

		# https://pip.pypa.io/en/stable/topics/authentication/#percent-encoding-special-characters
		username = credentials[0]
		password = urllib.parse.quote(credentials[1].encode('utf8'))

		urls = set(p.url for p in plugins if p.url is not None)
		for u in urls:
			cmd.append('-f')
			cmd.append(u.replace('{USERNAME}', username).replace('{PASSWORD}', password))

	run(cmd)

#-------------------------------------------------------------------------------
def uninstall(args):
	if len(s_installed) == 0:
		print('SOL is not installed on this machine')
	else:
		run(['python3', '-m', 'pip', 'uninstall', '-y'] + list(s_installed.keys()))
		print('SOL has been uninstalled from this machine')
	print()

#-------------------------------------------------------------------------------
def check_access(args):
	credentials = None

	def check_login():
		return requests.get('https://sol.neclab.eu/license/', auth=credentials, verify=not args.trust).status_code == 200

	# Fetch License Agreement for this user ------------------------------------
	if args.username is None or args.password is None: # interactive
		while credentials is None:
			print('Please authenticate using your SOL login for verifying your license status:')
			if args.username is None:
				print('User for sol.neclab.eu: ', end='')
				username = input()
			else:
				username = args.username

			password = args.password or getpass.getpass()
			credentials = (username, password)
			print()

			if not check_login():
				print(L_ERROR, 'Login failed!', L_RESET)
				credentials = None
	else: # non-interactive
		credentials = (args.username, args.password)

		if not check_login():
			raise Exception('Login failed!')

	user_access	= set()
	cache		= dict()

	def add_access(url):
		code = cache.get(url, None)
		if isinstance(code, int):
			return code == 200

		auth = None
		if '{USERNAME}:{PASSWORD}@' in url:
			url		= url.replace('{USERNAME}:{PASSWORD}@', '')
			auth	= credentials

		r			= requests.get(url, auth=auth, verify=not args.trust)
		cache[url]	= r.status_code
		return r.status_code == 200

	for url in s_access:
		if add_access(url):
			user_access.add(url)

	return credentials, user_access, cache

#-------------------------------------------------------------------------------
def fetch_license(credentials, args):
	r = requests.get('https://sol.neclab.eu/license/index.php/fetch-license', auth=credentials, verify=not args.trust)
	try:					r.raise_for_status()
	except Exception as e:	return e

	try:					return r.json()
	except Exception:		return Exception(r.content.decode('utf-8'))

#-------------------------------------------------------------------------------
def check_license(args):
	# Helper Functions ---------------------------------------------------------		
	def less(text, step = 40):
		assert isinstance(text, list)
		cnt = len(text)
		for i in range(0, (cnt + step - 1) // step):
			start	= i * step
			end		= min(cnt, start + step)
			for n in range(start, end):
				print(text[n])

			if end < cnt:
				print('')
				input('Press <Enter> for more')
		print('')

	def convert(markdown):
		out	= []
		for l in markdown.split('\n'):
			l = l.replace('<br/>', ' ')
			l = re.sub(r'<[^>]+>', '', l) # removes HTML tags

			def find():
				i = 0
				for i in range(0, len(l)):
					if l[i] != '#' and l[i] != ' ' and l[i] != '*':
						return i
				return i

			r = l[:find()]
			if		r == '# ':	l = "\033[47m\033[1;30m"	+ l[2:] + "\033[0m"
			elif	r == '## ':	l = "\033[1;37m\033[4;37m"	+ l[3:] + "\033[0m"
			elif	r == '**':	l = "\033[1;37m"			+ l[2:-2] + "\033[0m"

			out.append(l)
		return out

	credentials, user_access, _ = check_access(args)

	if len(user_access) == 0:
		raise Exception('You don\'t have access to any SOL packages. Please contact the SOL team to set your permissions correctly!')

	# Check if license is installed and with correct version -------------------
	v = s_installed.get(f'{s_prefix}-sol-license')
	if v != s_license_version:
		# If wrong version is installed, uninstall it before continuing --------
		if v:
			run(['python3', '-m', 'pip', 'uninstall', '-y', f'{s_prefix}-sol-license'])

		# Process license request ----------------------------------------------
		msg = fetch_license(credentials, args)
		if isinstance(msg, Exception):
			raise msg

		license_text			= msg.get('license')
		license_authorization	= msg.get('license_authorization')
		license_acceptance		= msg.get('license_acceptance')
		license_error			= msg.get('license_error')

		if license_text is None or license_authorization is None or license_acceptance is None:
			raise Exception(license_error if license_error else 'invalid msg received from server')

		# Show license text ----------------------------------------------------
		license_text = convert(license_text)

		if args.accept_license:
			license_text			= '\n'.join(license_text)
			license_authorization	= license_authorization.replace('\n', '')
			license_acceptance		= license_acceptance.replace('\n', '')
			print(license_text)
			print()
			print(f'{license_authorization}:', L_EMPH, 'yes, I am [user accepted through --accept-license flag]', L_RESET)
			print()
			print(f'{license_acceptance}:', L_EMPH, 'accept license [user accepted through --accept-license flag]', L_RESET)
			print()
		else:
			less(license_text)

			options			= ['no, I am not', 'yes, I am']
			terminal_menu	= TerminalMenu(options, title=license_authorization)
			choice			= terminal_menu.show()
			if choice != 1:	raise Exception('License declined!')

			options			= ['decline license', 'accept license']
			terminal_menu	= TerminalMenu(options, title=license_acceptance)
			choice			= terminal_menu.show()
			if choice != 1:	raise Exception('License declined!')
	
	return credentials, user_access

#-------------------------------------------------------------------------------
def available_plugins(args, user_access: Optional[Set[str]]) -> List[Plugin]:
	is_x86			= False
	is_ve			= False
	is_nvidia		= False
	is_torch		= False
	is_tensorflow	= False
	is_onnx			= False
	is_numpy		= False

	def check(p):
		nonlocal is_ve, is_x86, is_nvidia, is_torch, is_tensorflow, is_onnx, is_numpy

		if user_access:
			if p.url not in user_access:
				return False
		
		for dep in p.dependencies:
			if dep not in s_dependencies:
				return False

		n = p.name
		if n.endswith('device-nvidia'):			is_nvidia		= True
		if n.endswith('device-ve'):				is_ve			= True
		if n.endswith('device-x86'):			is_x86			= True
		if n.endswith('framework-tensorflow'):	is_tensorflow	= s_dependencies['tensorflow']
		if n.endswith('framework-pytorch'):		is_torch		= s_dependencies['torch']
		if n.endswith('framework-onnx'):		is_onnx			= s_dependencies['onnx']
		if n.endswith('framework-numpy'):		is_numpy		= s_dependencies['numpy']

		return True

	plugins = [p for p in s_available if check(p)]

	if is_tensorflow		is not False:	plugins.append(Plugin('tensorflow',			is_tensorflow	))
	if is_torch				is not False:	plugins.append(Plugin('torch',				is_torch		))
	if is_onnx				is not False:	plugins.append(Plugin('onnx',				is_onnx			))
	if is_numpy				is not False:	plugins.append(Plugin('numpy',				is_numpy		))

	if is_ve:
		if is_tensorflow	is not False:	plugins.append(Plugin('veda-tensorflow',	is_tensorflow	))
		if is_torch			is not False:	plugins.append(Plugin('veda-pytorch',		is_torch		))

	if args.mode == 'download':
		plugins.append(Plugin('nec-sol', f'=={s_version}'))

	return sorted(plugins, key=lambda x: x.name)

#-------------------------------------------------------------------------------
def debug(args):
	credentials, user_access, cache = check_access(args)
	
	msg = fetch_license(credentials, args)

	print(f'{L_EMPH}User Information:{L_RESET}')
	print(f'Username: {credentials[0]}')
	license = f'{L_ERROR}failed{L_RESET}' if isinstance(msg, Exception) else msg['license_type']
	print(f'License: {license}')
	print()
	
	print(f'{L_EMPH}User Permissions:{L_RESET}')
	for k, v in sorted(cache.items()):
		print(f'{k.replace("{USERNAME}:{PASSWORD}@", "")}:{L_SUCCESS if v == 200 else L_ERROR} {"granted" if v == 200 else "denied"}{L_RESET}')
	print()

	print(f'{L_EMPH}Devices/Frameworks to be installed:{L_RESET}')
	for k, v in sorted(s_dependencies.items()):
		print(f'- {k}{"" if v is None else v}')
	print()

	print(f'{L_EMPH}Plugins to be installed:{L_RESET}')
	for p in available_plugins(args, user_access):
		print(f'- {p.name}{"" if p.version is None else p.version}')
	print()

	if args.verbose:
		print(f'{L_EMPH}Installed Packages:{L_RESET}')
		for line in s_python_packages:
			print(line)

#-------------------------------------------------------------------------------
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=f'NEC-SOL Package Manager v{s_version}')
	parser.add_argument('mode', choices=[
		'download',
		'install',
		'uninstall',
		'debug',
	], help='installation mode')
	parser.add_argument('--accept-license', action='store_true', help='accept SOL license agreement')
	parser.add_argument('-u', '--username', default=None, type=str, help='SOL user name')
	parser.add_argument('-p', '--password', default=None, type=str, help='SOL user password')
	parser.add_argument('-f', '--folder', default=None, type=str, help='folder pointing to downloaded SOL packages')
	parser.add_argument('--trust', action='store_true', help='trust all SSL certificates (not recommended)')
	parser.add_argument('--devices', choices=[
		'all',
		'x86_64',
		've',
		'nvidia'
	], nargs='*', type=str, default=[], help='manually list devices to download/install')
	parser.add_argument('--frameworks', nargs='*', type=str, default=[], help='manually list frameworks to download/install')
	parser.add_argument('--user', action='store_true', help='install all packages using --user flag')
	parser.add_argument('--verbose', action='store_true', help='shows debug information')
	args = parser.parse_args()
	
	try:
		if sys.platform != 'linux':
			raise Exception(f'SOL only works on linux, but you are running: {sys.platform}')

		initialize()
		
		print(f'{L_EMPH}## NEC-SOL Package Manager v{s_version}{L_RESET}')
		
		if		args.mode == 'install':		install		(args)
		elif	args.mode == 'download':	install		(args)
		elif	args.mode == 'uninstall':	uninstall	(args)
		elif	args.mode == 'debug':		debug		(args)
		else:	raise Exception(f'unsupported installer mode: {mode}')
	except Exception as e:
		print()
		print(L_ERROR, str(e), L_RESET)
		print()
		if args.verbose:
			for line in traceback.format_tb(e.__traceback__):
				print(line)