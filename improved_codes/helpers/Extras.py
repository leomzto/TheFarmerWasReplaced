# Extras
def get_pos():
	return (get_pos_x(), get_pos_y())

def is_even(num):
	return num % 2 == 0

def is_odd(num):
	return num % 2 != 0

def need_water(limit=1):
	return get_water() < limit

def use_water():
	use_item(Items.Water)
	
def use_fertilize():
	use_item(Items.Fertilizer)

def get_plant():
	return get_entity_type()


	