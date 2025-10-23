# Movement

import Extras

world_size = get_world_size()

def move_to(x, y):
	(curr_x, curr_y) = Extras.get_pos()
	dx = x - curr_x
	dy = y - curr_y

	if dx > 0:
		for _ in range(dx):
			move(East)
	elif dx < 0:
		for _ in range(-dx):
			move(West)

	if dy > 0:
		for _ in range(dy):
			move(North)
	elif dy < 0:
		for _ in range(-dy):
			move(South)

def go_home():
	(curr_x, curr_y) = Extras.get_pos()
	for _ in range(curr_y):
		move(South)
	for _ in range(curr_x):
		move(West)
		
def can_drone_move():
	if not can_move(North) and not can_move(South):
		if not can_move(East) and not can_move(West):
			return False
	return True
		