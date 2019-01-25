def fix_address(set_values):
	'''
	@input : gets the address set (current or permanent)
	@output: corrected set values

	Right now this is simple, but can be made more robust after inspecting more data
	'''

	if not check_number(set_values[3]):
		# if the current address pin comes out to be faulty then use the 
		set_values[3] = ''


	return set_values


def check_number(num):

	# This functions checks if the given string only has numbers
	# @Output 1: if all numbers
	#  Output 0 : if alphabets present

	if len(num) < 4:
		return 0

	try:
		num = int(num)
		return 1
	except:
		return 0

#Function 
def fix_row(row):

	'''

	@input : Raw row
	@output : Fixed row

	What are the problems that can be encountered (as inferred from the given data):
	1. Current Address is missing.
	2. Permanent Address is missing.
	3. Invalid pin - (contains some alphabets)


	'''

	# Allot values to the respective fields
	curr_address, curr_city, curr_state, curr_pin,perm_add, perm_city, perm_state, perm_pin = row
	set_curent = [curr_address,curr_city,curr_state, curr_pin]
	set_perman = [perm_add, perm_city, perm_state,perm_pin]

	set_curent = fix_address(set_curent)
	set_perman = fix_address(set_perman)

	row = set_curent+set_perman

	return row
