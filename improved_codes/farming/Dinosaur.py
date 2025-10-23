import Drones
import Extras
import PlantSystem
import Movement

WORLD_SIZE = get_world_size()

DINO_HAT = Hats.Dinosaur_Hat

def search_in_all_tiles():
	global WORLD_SIZE
	global DINO_HAT
	
	clear()
	change_hat(DINO_HAT)
	
	steps = 0
	loop = True
	
	while loop:
		if not Movement.can_drone_move():
			change_hat(Hats.Purple_Hat)
			loop = False
			
		for pos in range(WORLD_SIZE - 1):
			move(East)
		move(North)
		
		for pos in range(WORLD_SIZE):
			for x in range(WORLD_SIZE - 2):
				if Extras.is_even(pos):
					move(North)
				else:
					move(South)
				steps += 1
				
			if pos != WORLD_SIZE - 1:
				move(West)
			else:
				move(South)
			steps += 1
			
		continue

def movements(posX, posY):
	global WORLD_SIZE
	
	moves_list = []
	
	if Extras.is_even(posX):
		if posY != 0:
			moves_list.append(South)
	else:
		if posY != WORLD_SIZE - 1:
			moves_list.append(North)
			
	if Extras.is_even(posY):
		if posX != WORLD_SIZE - 1:
			moves_list.append(East)
	else:
		if posX != 0:
			moves_list.append(West)
			
	return moves_list
	
def nextSquare(apple_pos, priority):
	moves_list = []
	
	dino_posX, dino_posY = Extras.get_pos()
	
	x_diference = dino_posX - apple_pos[0]
	y_diference = dino_posY - apple_pos[1]

	if x_diference < 0 and x_diference != 0:
		moves_list.append(East)
	if x_diference > 0 and x_diference != 0:
		moves_list.append(West)
	if y_diference < 0 and y_diference != 0:
		moves_list.append(North)
	if y_diference > 0 and y_diference != 0:
		moves_list.append(South)

	moves = movements(dino_posX, dino_posY)

	if priority in moves_list and priority in moves and can_move(priority):
		return priority
	
	for direction in moves_list:
		if direction in moves and can_move(direction):
			return direction
	
	return moves[random() * len(moves) // 1]

def look_for_best_path():
	global WORLD_SIZE
	global DINO_HAT
	
	clear()	
	

	#Drones.send_home()
	Drones.send_to_center()
	change_hat(DINO_HAT)
	
	
	path = []
	
	dir = East
	
	apples = 1
	max_apples = (WORLD_SIZE * WORLD_SIZE) - 1
	
	steps = 0
	
	while True:
		apple_pos = measure()
		
		posX, posY = Extras.get_pos()
		dino_pos = Extras.get_pos()
		
		if not Movement.can_drone_move():
			change_hat(Hats.Purple_Hat)
			return True

		if apples == max_apples:
			change_hat(Hats.Green_Hat)
			return True
			
		while dino_pos != apple_pos:
			dir = nextSquare(apple_pos, dir)
			move(dir)
			steps += 1
			
			dino_pos = Extras.get_pos()
			
		apples += 1

def main(method="look_for_best_path"):
	if method != "look_for_best_path":
		exec = search_in_all_tiles()
	else:
		exec = look_for_best_path()
		
	exec()
	
	
main()

	