import torch, csv, os
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.dataloader import default_collate



class TrialOutcomeDatasetBase(Dataset):
	'''
	Trial dataset for trial outcome prediction 

    Parameters
    ----------		
    data: a tuple of length 5, 
    containing nctid list, label list, smiles string list, icd-codes list and criteria list
	''' 
	def __init__(self, data):
		nctid_lst, label_lst, smiles_lst, icdcode_lst, criteria_lst = data 
		self.nctid_lst = nctid_lst 
		self.label_lst = label_lst 
		self.smiles_lst = smiles_lst 
		self.icdcode_lst = icdcode_lst 
		self.criteria_lst = criteria_lst 

	def __len__(self):
		return len(self.nctid_lst)

	def __getitem__(self, index):
		return self.nctid_lst[index], self.label_lst[index], self.smiles_lst[index], \
				self.icdcode_lst[index], self.criteria_lst[index]
	#### smiles_lst[index] is list of smiles

def csvfile2dataloader(csvfile):
	'''
	Transform the csvfile (data file) into dataloader 
	'''
	with open(csvfile, 'r') as csvfile:
		rows = list(csv.reader(csvfile, delimiter=','))[1:]
	## nctid,status,why_stop,label,phase,diseases,icdcodes,drugs,smiless,criteria
	nctid_lst = [row[0] for row in rows]
	label_lst = [row[3] for row in rows]
	icdcode_lst = [row[6] for row in rows]
	drugs_lst = [row[7] for row in rows]
	smiles_lst = [row[8] for row in rows]
	criteria_lst = [row[9] for row in rows] 

	data = nctid_lst, label_lst, smiles_lst, icdcode_lst, criteria_lst 
	dataset = TrialOutcomeDatasetBase(data)
	data_loader = DataLoader(dataset, batch_size = 32, shuffle = True, collate_fn = trial_collate_fn)
	return data_loader







