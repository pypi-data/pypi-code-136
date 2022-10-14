from . import powerpy

def get_token_usage(authorization):
	url = "https://api.powerbi.com/v1.0/myorg/availableFeatures"
	
	response = powerpy.get(url, authorization)
	available_features = response.json()
	features = available_features['features']
	
	return features[1]['additionalInfo']['usage']

def get_datasets_in_group(group_id, authorization):
	url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/datasets"
	
	response = powerpy.get(url, authorization).json()
	
	return response['value']
	
def get_datasets_names_in_group(group_id, authorization):
	datasets = get_datasets_in_group(group_id, authorization)
	list = []
	for i in range(len(datasets)):
		list.append(datasets[i]['name'])
		
	return list

def refresh_dataset_in_group_by_name(dataset_name, group_id, authorization):
	datasets = get_datasets_in_group(group_id, authorization)
	
	for i in range(len(datasets)):
		if dataset_name == datasets[i]['name']:
			dataset_id = datasets[i]['id']
	url = f"https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/refreshes"
	
	return powerpy.post(url, authorization)

def refresh_dataset_by_id(dataset_id, authorization):
	url = f"https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/refreshes"
	
	return powerpy.post(url, authorization)