import Get
import mBasicSetup

substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)

def make_maze(maze_size):
	set_world_size(maze_size)
	if num_items(Items.Weird_Substance) > substance:
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, substance)
		return True
	else:
		return False
	
def is_treasure():
	if get_entity_type() == Entities.Treasure:
		return True
	else:
		return False
		
directions = [North, East, South, West]

def turn_(side, index):
	if side == "left":
		return (index - 1) % 4
	elif side == "right":
		return (index + 1) % 4
	elif side == "back":
		return (index +2) % 4
		
def search_treasure(start_facing = 0, maze_size = None):
	facing = start_facing
	
	while True:
		if is_treasure():
			harvest()
			return True
			
		left = turn_("left", facing)
		front = facing
		right = turn_("right", facing)
		back = turn_("back", facing)
		
		if can_move(directions[left]):
			move(directions[left])
			facing = left
			continue
			
		if can_move(directions[front]):
			move(directions[front])
			continue

		if can_move(directions[right]):
			move(directions[right])
			facing = right
			continue
			
		if can_move(directions[back]):
			move(directions[back])
			facing = back
			continue
			
		return False
		