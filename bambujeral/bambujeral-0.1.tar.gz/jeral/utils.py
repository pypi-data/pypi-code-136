import hashlib,random

def getlastid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
		hashid = hashlib.sha256(str(newid).encode())
	else:
		newid = 1
		hashid = hashlib.sha256(str(newid).encode())
	return newid, hashid.hexdigest()