import Extras

WORLD_SIZE = 5

IN_HAND_SUBSTANCES = num_items(Items.Weird_Substance)
SUBSTANCE_AMOUNT = WORLD_SIZE * 2**(num_unlocked(Unlocks.Mazes) - 1)
TREASURE = Entities.Treasure

def make_maze():
	global SUBSTANCE_AMOUNT
	
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, SUBSTANCE_AMOUNT)

def is_treasure():
	global TREASURE
	if Extras.get_plant() == TREASURE:
		return True
	else:
		return False
		
def task(max_items=None):
	while True:
		if max_items != None:
			break
		if num_drones() == WORLD_SIZE * WORLD_SIZE:
			make_maze()
			if is_treasure():
				harvest()
	
def main(max_items=None):
	global WORLD_SIZE
	
	set_world_size(WORLD_SIZE)
	cells_list = []
	
	if IN_HAND_SUBSTANCES > SUBSTANCE_AMOUNT:
		clear()
		
		while num_drones() <= 25:
			pos_x, pos_y = Extras.get_pos()
			current = (pos_x, pos_y)
			if current not in cells_list:
				cells_list.append(current)
				spawn_drone(task)
				move(North)
			else:
				move(East)

main()
				