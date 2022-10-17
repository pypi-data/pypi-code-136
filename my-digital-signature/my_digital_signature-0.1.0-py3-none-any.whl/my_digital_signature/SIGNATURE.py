# first_name = None  # user's first name
#
# last_name = None  # user's last name
#
# date_of_birth = None  # user's date of birth in digits in the format YYYYMMDD
#
# date_today_in_words = None  # current date in words in the format YYYYMMDD
#
# time_now_HH_MM_SS = None  # Current time up to seconds in the format HH:MM:SS
# # in digits
from datetime import datetime
from num2words import num2words


def create_signature(first_name: str, last_name: str, date_of_birth: str) -> str:
	"""Creates a unique digital signature for New Users.
	:param first_name: The first name of the user. Preferably capitalized!
	:param last_name: The last name of the user. Preferably capitalized!
	:param date_of_birth: The date of birth of the user. YYYY-MM-DD
	:return: Identification string that's unique to the user
	"""
	
	# NAME SPLIT
	name_first_split = first_name[len(first_name)//2:][::-1]
	name_second_split = last_name[0:len(last_name)//2][::-1]
	name_third_split = last_name[len(last_name)//2:][::-1]
	name_fourth_split = first_name[0:len(first_name)//2][::-1]
	
	# DATE SPLIT
	dob = date_of_birth.replace("-", "")
	dob_first_split = dob[len(dob)//4:len(dob)//2][::-1]
	dob_second_split = dob[len(dob)//2:3*len(dob)//4][::-1]
	dob_third_split = dob[3*len(dob)//4:][::-1]
	dob_fourth_split = dob[:len(dob)//4][::-1]
	
	# TODAY'S DATE
	date_today, time_now = datetime.now().strftime('%x').split("/"), \
	                       datetime.now().strftime('%X:%f')[::-1].split(
		                       ":")
	
	date_string = ""
	
	for d in date_today:
		date_string += num2words(int(d)).replace("-", "")
	
	date_first_split = date_string[
	                   len(date_string)//4:len(date_string)//2][::-1]
	date_second_split = date_string[
	                    len(date_string)//2:3*len(date_string)//4][
	                    ::-1]
	date_third_split = date_string[3*len(date_string)//4:][::-1]
	date_fourth_split = date_string[:len(date_string)//4][::-1]
	
	signature = name_first_split+dob_third_split+date_second_split+time_now[
		3]+name_second_split+dob_fourth_split+date_third_split+time_now[0][
		:3:-1] +name_third_split+dob_first_split+date_first_split+time_now[
		2]+name_fourth_split+dob_second_split+date_fourth_split+time_now[1]
	
	return signature
