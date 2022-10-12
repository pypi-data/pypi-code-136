import math


def ungreat_match(str1 : str, str2 : str, mkdefault : float = 0.7 , mismatching_chars : int = 5) -> list:
	i=0
	mk = 0
	min_lenth = min(len(str1), len(str2))
	str1 = str1.lower()
	str2 = str2.lower()
	if str1 == str2:
		return [str1, 'True']
	elif math.fabs(len(str1) - len(str2)) > mismatching_chars:
		return ['mismatching skills', 'False', 'mismatching chars less than needs']
	else:
		# count matching chars
		for char in str1:
			if i < min_lenth:
				if char == str2[i]:
					mk+=1
			i+=1

		# checking the mkdefault condition
		if (mk >=  (min_lenth*mkdefault)):
			if min_lenth == len(str1):
				return [str1, 'True']
			elif min_lenth == len(str2):
				return [str2, 'True']
		else:
			return ['mismatching skills', 'False', 'mkdefault less than needs']
