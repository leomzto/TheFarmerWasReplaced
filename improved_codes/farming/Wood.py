import Extras
import Ground

WORLD_SIZE = get_world_size()

DRONES_TO_SPAWN = WORLD_SIZE - 1

COMPANION_MAPPING = {}
TREE_MAPPING = {}

TREE = Entities.Tree
BUSH = Entities.Bush
GRASS = Entities.Grass
CARROT = Entities.Carrot

SOILED_GROUND = Grounds.Soil

def can_plant_tree(posX, posY):
	return posX % 2 == posY % 2

def get_comps(posX, posY):
	global COMPANION_MAPPING
	global TREE_MAPPING
	
	companion = get_companion()
	
	if companion == None:
		return False
		
	entity_targ, (x_targ, y_targ) = companion

	if (x_targ, y_targ) not in COMPANION_MAPPING:
		COMPANION_MAPPING[(x_targ, y_targ)] = entity_targ
		TREE_MAPPING[(posX, posY)] = (x_targ, y_targ) 
		return True
		
	return False


def task(max_items=None):
	global WORLD_SIZE
	global COMPANION_MAPPING
	global TREE_MAPPING
	
	global TREE
	global BUSH
	global GRASS
	global CARROT
	
	global SOILED_GROUND
	
	do = False
	
	if max_items == None:
		do = True
	else:
		do = num_items(Items.Wood) < max_items 
	
	while do:
		for _ in range(WORLD_SIZE):
			posX, posY = Extras.get_pos()
			
			if can_plant_tree(posX, posY):
				if can_harvest():
					harvest()
					plant(TREE)
				else:
					pass
				
				if (posX, posY) in TREE_MAPPING:
					companion_pos = TREE_MAPPING.pop((posX, posY))
					if companion_pos in COMPANION_MAPPING:
						COMPANION_MAPPING.pop(companion_pos)

				get_comps(posX, posY)
				
				if Extras.need_water():
					Extras.use_water()
					
			elif (posX, posY) in COMPANION_MAPPING:
				entity_targ = COMPANION_MAPPING[(posX, posY)]
				harvest()
				
				if entity_targ == GRASS:
					if Ground.get_groud() != SOILED_GROUND:
						Ground.soil()
						
				elif entity_targ == CARROT:
					if Ground.get_groud() != SOILED_GROUND:
						till()

				plant(entity_targ)
				
			else:
				harvest()
				plant(BUSH)
				
			move(North)
			
		if max_items != None and num_items(Items.Wood) >= max_items:
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

def leader():
	max_items = 10000000000
	while num_items(Items.Wood) < max_items:
		main(max_items)
leader()

	
#main()

