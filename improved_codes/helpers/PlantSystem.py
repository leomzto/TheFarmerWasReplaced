# Plant System

from Numbers import *
import Extras
import Ground

MULTIPLIER = 1

SOILED_GROUND = Grounds.Soil

MAX_DRONES = max_drones()

WATER_AMOUNT = num_items(Items.Water)
IS_WATERING = False

FERTILIZER_AMOUNT = num_items(Items.Fertilizer)
IS_FERTILIZING = False

def plant_crop(plant_type, will_use_water=False, will_use_fertilizer=False):
	global WORLD_SIZE
	
	global SOILED_GROUND
	
	global MAX_DRONES
	
	global IS_FERTILIZING
	global IS_WATERING
	
	global FERTILIZER_AMOUNT
	global WATER_AMOUNT
	
	if will_use_water != False:
		IS_WATERING = True
	if will_use_fertilizer != False:
		IS_FERTILIZING = True
	
	if Ground.get_groud() != SOILED_GROUND:
		Ground.soil()
	
	if WATER_AMOUNT > MAX_DRONES and IS_WATERING and Extras.need_water():
		Extras.use_water()
		
	if can_harvest():
		harvest()
	
	plant(plant_type)
	
	if FERTILIZER_AMOUNT > MAX_DRONES and IS_FERTILIZING:
		Extras.use_fertilize()
		
	