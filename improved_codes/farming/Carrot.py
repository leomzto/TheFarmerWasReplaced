import Extras
import Ground

WORLD_SIZE = get_world_size()

DRONES_TO_SPAWN = WORLD_SIZE - 1

COMPANION_MAPPING = {}
CARROT_MAPPING = {}

CARROT = Entities.Carrot

TO_SOIL = [Entities.Carrot, Entities.Bush, Entities.Tree]
SOILED_GROUND = Grounds.Soil

def get_comps(posX, posY):
	global COMPANION_MAPPING
	global CARROT_MAPPING
	
	companion = get_companion()
	
	if companion == None:
		return False
		
	entity_targ, (x_targ, y_targ) = companion

	if (x_targ, y_targ) not in COMPANION_MAPPING:
		COMPANION_MAPPING[(x_targ, y_targ)] = entity_targ
		CARROT_MAPPING[(posX, posY)] = (x_targ, y_targ)
		return True
		
	return False


def soil_n_plant(entity):
	global TO_SOIL
	
	if entity in TO_SOIL and Ground.get_groud() != SOILED_GROUND:
		Ground.soil()
	plant(entity)


def task(max_items=None):
	global WORLD_SIZE
	global COMPANION_MAPPING
	global CARROT_MAPPING
	
	do = False
	
	if max_items == None:
		do = True
	else:
		do = num_items(Items.Carrot) < max_items 
	
	while do:
		for _ in range(WORLD_SIZE):
			posX, posY = Extras.get_pos()
			
			harvest()
			
			if (posX, posY) in COMPANION_MAPPING:
				entity_targ = COMPANION_MAPPING[(posX, posY)]
				
				soil_n_plant(entity_targ)
				
				if entity_targ == CARROT and Extras.need_water():
					Extras.use_water()
				
			elif (posX, posY) in CARROT_MAPPING:
				soil_n_plant(CARROT)
				
				if Extras.need_water():
					Extras.use_water()

				companion_pos = CARROT_MAPPING.pop((posX, posY))
				if companion_pos in COMPANION_MAPPING:
					COMPANION_MAPPING.pop(companion_pos)
				
				get_comps(posX, posY)
				
			else:
				soil_n_plant(CARROT)
				
				if Extras.need_water():
					Extras.use_water()

				get_comps(posX, posY)			
			move(North)
			
		if max_items != None and num_items(Items.Carrot) >= max_items:
			do = False
def main(max_items=None):
	clear()
	global DRONES_TO_SPAWN
	
	for _ in range(DRONES_TO_SPAWN):
		spawn_drone(task)
		move(East)
	
	if max_items != None:
		task(max_items)
	else:
		task()

#main()