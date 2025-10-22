# Leaderboarding
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
	while True:
		if max_items != None and num_items(Items.Wood) >= max_items:
			return
		for _ in range(WORLD_SIZE):
			if max_items != None and num_items(Items.Wood) >= max_items:
				return

			posX, posY = Extras.get_pos()
			if can_plant_tree(posX, posY):
				if can_harvest():
					harvest()
					plant(TREE)

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

def main(max_items=None):
	clear()
	global DRONES_TO_SPAWN

	def worker():
		task(max_items)

	for _ in range(DRONES_TO_SPAWN):
		spawn_drone(worker)
		move(East)

	task(max_items)

def farm_until_target(max_items):
	while num_items(Items.Wood) < max_items:
		main(max_items)

def leader():
	max_items = 10000000000
	farm_until_target(max_items)

leaderboard_run(Leaderboards.Wood, "Leaderboarding", 1000000000000)
leader()
