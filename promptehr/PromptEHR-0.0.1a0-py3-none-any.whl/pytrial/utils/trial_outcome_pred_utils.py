
import csv 
import os 
import torch, csv, os
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.dataloader import default_collate


dir_path = os.path.dirname(os.path.realpath(__file__))
base_file = ""
# rows = list(csv.reader(csvfile, delimiter=','))[1:]

def read_csv_to_data(data_file):
	rows = list(csv.reader(csvfile, delimiter=','))[1:]
	nctid_lst = [row[0] for row in rows]
	label_lst = [row[3] for row in rows]
	icdcode_lst = [row[6] for row in rows]
	drugs_lst = [row[7] for row in rows]
	smiles_lst = [row[8] for row in rows]
	criteria_lst = [row[9] for row in rows] 
	return nctid_lst, label_lst, smiles_lst, icdcode_lst, criteria_lst 
	# dataset = Trial_Dataset(nctid_lst, label_lst, smiles_lst, icdcode_lst, criteria_lst)
	# data_loader = data.DataLoader(dataset, batch_size = batch_size, shuffle = shuffle, collate_fn = trial_collate_fn)
	# return data_loader



def text_2_lst_of_lst(text):
	"""
		"[""['F53.0', 'P91.4', 'Z13.31', 'Z13.32']""]"
	"""
	text = text[2:-2]
	code_sublst = []
	for i in text.split('", "'):
		i = i[1:-1]
		code_sublst.append([j.strip()[1:-1] for j in i.split(',')])
	# print(code_sublst)	
	return code_sublst 

def get_icdcode_lst():
	input_file = 'demo_data/demo_trial_outcome_data/raw_data.csv'
	with open(input_file, 'r') as csvfile:
		rows = list(csv.reader(csvfile, delimiter = ','))[1:]
	code_lst = []
	for row in rows:
		code_sublst = text_2_lst_of_lst(row[6])
		code_lst.append(code_sublst)
	return code_lst 

def combine_lst_of_lst(lst_of_lst):
	lst = list(reduce(lambda x,y:x+y, lst_of_lst))
	lst = list(set(lst))
	return lst

def collect_all_icdcodes():
	code_lst = get_icdcode_lst()
	code_lst = list(map(combine_lst_of_lst, code_lst))
	code_lst = list(reduce(lambda x,y:x+y, code_lst))
	code_lst = list(set(code_lst))
	return code_lst

def find_ancestor_for_icdcode(icdcode, icdcode2ancestor):
	if icdcode in icdcode2ancestor:
		return 
	icdcode2ancestor[icdcode] = []
	ancestor = icdcode[:]
	while len(ancestor) > 2:
		ancestor = ancestor[:-1]
		if ancestor[-1]=='.':
			ancestor = ancestor[:-1]
		if icd10.find(ancestor) is not None:
			icdcode2ancestor[icdcode].append(ancestor)
	return

def build_icdcode2ancestor_dict():
	pkl_file = "demo_data/demo_trial_outcome_data/icdcode2ancestor_dict.pkl"
	if os.path.exists(pkl_file):
		icdcode2ancestor = pickle.load(open(pkl_file, 'rb'))
		return icdcode2ancestor 
	all_code = collect_all_icdcodes() 
	icdcode2ancestor = defaultdict(list)
	for code in all_code:
		find_ancestor_for_icdcode(code, icdcode2ancestor)
	pickle.dump(icdcode2ancestor, open(pkl_file,'wb'))
	return icdcode2ancestor 










sentence2vec = dict() 

def clean_protocol(protocol):
	protocol = protocol.lower()
	protocol_split = protocol.split('\n')
	filter_out_empty_fn = lambda x: len(x.strip())>0
	strip_fn = lambda x:x.strip()
	protocol_split = list(filter(filter_out_empty_fn, protocol_split))	
	protocol_split = list(map(strip_fn, protocol_split))
	return protocol_split 

def split_protocol(protocol):
	protocol_split = clean_protocol(protocol)
	inclusion_idx, exclusion_idx = len(protocol_split), len(protocol_split)	
	for idx, sentence in enumerate(protocol_split):
		if "inclusion" in sentence:
			inclusion_idx = idx
			break
	for idx, sentence in enumerate(protocol_split):
		if "exclusion" in sentence:
			exclusion_idx = idx 
			break 		
	if inclusion_idx + 1 < exclusion_idx + 1 < len(protocol_split):
		inclusion_criteria = protocol_split[inclusion_idx:exclusion_idx]
		exclusion_criteria = protocol_split[exclusion_idx:]
		if not (len(inclusion_criteria) > 0 and len(exclusion_criteria) > 0):
			print(len(inclusion_criteria), len(exclusion_criteria), len(protocol_split))
			exit()
		return inclusion_criteria, exclusion_criteria ## list, list 
	else:
		return protocol_split, 

def protocol2feature(protocol, sentence_2_vec):
	result = split_protocol(protocol)
	inclusion_criteria, exclusion_criteria = result[0], result[-1]
	inclusion_feature = [sentence_2_vec[sentence].view(1,-1) for sentence in inclusion_criteria if sentence in sentence_2_vec]
	exclusion_feature = [sentence_2_vec[sentence].view(1,-1) for sentence in exclusion_criteria if sentence in sentence_2_vec]
	if inclusion_feature == []:
		inclusion_feature = torch.zeros(1,768)
	else:
		inclusion_feature = torch.cat(inclusion_feature, 0)
	if exclusion_feature == []:
		exclusion_feature = torch.zeros(1,768)
	else:
		exclusion_feature = torch.cat(exclusion_feature, 0)
	return inclusion_feature, exclusion_feature 


def smiles_txt_to_lst(text):
	"""
		"['CN[C@H]1CC[C@@H](C2=CC(Cl)=C(Cl)C=C2)C2=CC=CC=C12', 
		  'CNCCC=C1C2=CC=CC=C2CCC2=CC=CC=C12']" 
	"""
	text = text[1:-1]
	lst = [i.strip()[1:-1] for i in text.split(',')]
	return lst 

def icdcode_text_2_lst_of_lst(text):
	text = text[2:-2]
	lst_lst = []
	for i in text.split('", "'):
		i = i[1:-1]
		lst_lst.append([j.strip()[1:-1] for j in i.split(',')])
	return lst_lst 

def trial_collate_fn(x):
	nctid_lst = [i[0] for i in x]     ### ['NCT00604461', ..., 'NCT00788957'] 
	label_vec = default_collate([int(i[1]) for i in x])  ### shape n, 
	smiles_lst = [smiles_txt_to_lst(i[2]) for i in x]
	icdcode_lst = [icdcode_text_2_lst_of_lst(i[3]) for i in x]
	criteria_lst = [protocol2feature(i[4], sentence2vec) for i in x]
	return [nctid_lst, label_vec, smiles_lst, icdcode_lst, criteria_lst]




