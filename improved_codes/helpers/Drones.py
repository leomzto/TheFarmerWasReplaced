# Drones

import Extras

WORLD_SIZE = get_world_size()

def send_home():
	global WORLD_SIZE
	
	while get_pos_x() != 0:
		x = get_pos_x()
		if x > WORLD_SIZE // 2:
			move(East)
		else:
			move(West)
			
	while get_pos_y() != 0:
		y = get_pos_y()
		if y > WORLD_SIZE // 2:
			move(North)
		else:
			move(South)

def send_to_center():
	global WORLD_SIZE
	
	center = WORLD_SIZE // 2
	
	while True:
		x, _ = Extras.get_pos()
		
		if x == center:
			break
		elif x > center:
			move(West)
		else:
			move(East)
	
	while True:
		_, y = Extras.get_pos()
		
		if y == center:
			break
		elif y > center:
			move(South)
		else:
			move(North)

			
def move_drone(posX, posY):
	global WORLD_SIZE
	
	x, y = Extras.get_pos()
	
	while x != posX:
		dirX = get_pos_x() - x
		if dirX < 0:
			if abs(dirX) <= WORLD_SIZE // 2:
				move(East)
			else:
				move(West)
		else:
			if abs(dirX) <= WORLD_SIZE // 2:
				move(West)
			else:
				move(East)
				
	while y != posY:
		dirY = get_pos_y() - y
		if dirY < 0:
			if abs(dirY) <= WORLD_SIZE // 2:
				move(North)
			else:
				move(South)
		else:
			if abs(dirY) <= WORLD_SIZE // 2:
				move(South)
			else:
				move(North)