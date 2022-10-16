import os
import requests

def download():
	print('Download starts ...')
	def absolute_pwd(file_name):
		return os.path.join(os.path.dirname(__file__), file_name)
		
	pwd = absolute_pwd('')

	if not os.path.exists(absolute_pwd('model')):
		os.makedirs(absolute_pwd('model'))
		
	if not os.path.exists(absolute_pwd('data')):
		os.makedirs(absolute_pwd('data'))
		
	# download checkpoint file
	MODEL_VERSION = '0.0.1'
	url = 'https://docs.google.com/uc?export=download&id=1R42l-os9KlI1UJkwudEtvmwfJf6d3fPg'
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('model/BGCfinder_model_checkpoint_' + MODEL_VERSION), 'wb').write(r.content)

	# download example files
	url = 'https://docs.google.com/uc?export=download&id=1I_Px_oKyRmx9gRNhDnqwyM5s1VAw6shR'
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('data/input_example_1.fasta'), 'wb').write(r.content)

	url = 'https://docs.google.com/uc?export=download&id=1jsnuKCM_tnpFLxiblM4TVRqeDbRAoUuG'
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('data/input_example_2.fasta'), 'wb').write(r.content)

	print('Download finish')
