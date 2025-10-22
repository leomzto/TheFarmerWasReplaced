# Hay Farming
import Extras
import Ground

WORLD_SIZE = get_world_size()

DRONES_TO_SPAWN = WORLD_SIZE - 1

COMPANION_MAPPING = {}
HAY_MAPPING = {}

GRASS = Entities.Grass
CARROT = Entities.Carrot

SOILED_GROUND = Grounds.Soil

def get_comps(posX, posY):
	global COMPANION_MAPPING
	global HAY_MAPPING
	
	companion = get_companion()
	
	if companion == None:
		return False
		
	entity_targ, (x_targ, y_targ) = companion

	if (x_targ, y_targ) not in COMPANION_MAPPING:
		COMPANION_MAPPING[(x_targ, y_targ)] = entity_targ
		HAY_MAPPING[(posX, posY)] = (x_targ, y_targ)
		return True	
	return False

def task(max_items=None):
	global WORLD_SIZE
	global COMPANION_MAPPING
	global HAY_MAPPING
	
	global GRASS
	global CARROT
	
	global SOILED_GROUND
	
	do = False
	
	if max_items == None:
		do = True
	else:
		do = num_items(Items.Hay) < max_items 
	
	while do:
		for _ in range(WORLD_SIZE):
			posX, posY = Extras.get_pos()
			
			harvest()
			
			if Ground.get_groud() == SOILED_GROUND:
				Ground.soil()
	
			if (posX, posY) in COMPANION_MAPPING:
				entity_targ = COMPANION_MAPPING[(posX, posY)]
				
				if entity_targ == CARROT:
					if Ground.get_groud() != SOILED_GROUND:
						Ground.soil()
					plant(CARROT)
				elif entity_targ != GRASS:
					plant(entity_targ) 
			else:
				if (posX, posY) in HAY_MAPPING:
					companion_pos = HAY_MAPPING.pop((posX, posY))
					if companion_pos in COMPANION_MAPPING:
						COMPANION_MAPPING.pop(companion_pos)
				
				get_comps(posX, posY)
			move(North)
		
		if max_items != None and num_items(Items.Hay) >= max_items:
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