# Ground 

def get_groud():
	return get_ground_type()

def is_soiled():
	if get_ground_type() == Grounds.Soil:
		return True
	return False
	
def soil():
	till()