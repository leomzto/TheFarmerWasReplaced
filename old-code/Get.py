import mBasicSetup
import mTreasure
def is_soiled():
	if get_ground_type() == Grounds.Soil:
		return True
	return False
	
def is_even(n):
	return n % 2 == 0
	

def can_plant_(plant_name):
	cost = get_cost(plant_name)
	
	for item in cost:
		if num_items(item) < cost[item]:
			return item
			
	return True
	
def can_unlock_(to_be_unlocked):
	cost_dict = get_cost(to_be_unlocked)

	for item_name in cost_dict:
		item_value = cost_dict[item_name]
		break
	
	return num_items(item_name) >= item_value