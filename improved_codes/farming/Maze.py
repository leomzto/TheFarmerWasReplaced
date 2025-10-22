import Extras
import Movement

def make_maze(maze_size = 6):
	SUBSTANCE_AMOUNT = get_world_size() * maze_size
	if num_items(Items.Weird_Substance) > SUBSTANCE_AMOUNT:
		plant(Entities.Bush)
		use_item(Items.Weird_Substance, SUBSTANCE_AMOUNT)
		return True
	else:
		return False
	
def is_treasure():
	if Extras.get_plant() == Entities.Treasure:
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
		
def search_treasure(start_facing = 0):
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
		
def main():
	START_POINT = [4, 4]
	while True:
		Movement.move_to(START_POINT[0], START_POINT[1])
		make_maze()
		search_treasure()
		
main()
		