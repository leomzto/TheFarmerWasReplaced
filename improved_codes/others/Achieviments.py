import Extras

def make_flips():
	flips = 0
	while flips < 1000:	
		do_a_flip()
		flips += 1
		
def thousand_flips():
	while True:
		make_flips()
		
pumpkin_count = 0	
def make_the_pumpkin():
	MAX_RANGE = 32
	PUMPKIN = Entities.Pumpkin
	DEAD_PUMPKIN = Entities.Dead_Pumpkin
	
	for i in range(MAX_RANGE):
		till()
		move(North)
	for i in range(MAX_RANGE):
		plant(PUMPKIN)
		move(North)
	
	while True:
		cont = 0
		on = True
		
		for i in range(MAX_RANGE):
			if not can_harvest():
				if Extras.get_plant() == DEAD_PUMPKIN or Extras.get_plant() == None:
					plant(PUMPKIN)
				else:
					cont += 1
					if cont == MAX_RANGE and on:
						global pumpkin_count
						
						pumpking_count += 32
						print(pumpukin_count)
						on = False
					if pumpkin_count == MAX_RANGE * MAX_RANGE:
						harvest()
						
				if on:
					move(North)
				else:
					do_a_flip()
					
def giant_pumpkin():
	while True:
		if spawn_drone(make_the_pumpkin):
			move(East)
		else:
			make_the_pumpkin()				


#from Maze2 import *
def task_for_achi():
	start = 0
	end = 300
	while True:
		if num_drones() == WORLD_SIZE * WORLD_SIZE:
			if is_treasure() and start == end:
				harvest()
				start = 0
			elif is_treasure() and start != end:
				use_item(Items.Weird_Substance, SUBSTANCE_AMOUNT)
				start += 1
				if start == end and is_treasure():
					harvest()
			make_maze()

def recycling():
	global WORLD_SIZE
	if IN_HAND_SUBSTANCES > SUBSTANCE_AMOUNT:
		clear()
		set_world_size(WORLD_SIZE)
		cells_list = []
		
		while num_drones() <= WORLD_SIZE * WORLD_SIZE:
			pos_x, pos_y = Extras.get_pos()
			current = (pos_x, pos_y)
			if current not in cells_list:
				cells_list.append(current)
				spawn_drone(task_for_achi)
				move(North)
			else:
				move(East)
				
def stack_overflow():
	return stack_overflow()
	
def fashion_show():
	set_world_size(5)
	
	hat_list = [
		Hats.Cactus_Hat,
		Hats.Carrot_Hat,
		Hats.Golden_Cactus_Hat,
		Hats.Golden_Carrot_Hat,
		Hats.The_Farmers_Remains
	]

	coords = [
		(0, 0),
		(0, 4),
		(4, 0),
		(4, 4),
		(2, 2)
	]

	def make_drone_task(x_targ, y_targ, hat):
		def drone_task():
			while get_pos_x() != x_targ:
				if get_pos_x() < x_targ:
					move(East)
				else:
					move(West)
			
			while get_pos_y() != y_targ:
				if get_pos_y() < y_targ:
					move(North)
				else:
					move(South)
			
			change_hat(hat)
			
			while True:
				wait_for(drone_task())
		return drone_task

	for i in range(len(hat_list)):
		task = make_drone_task(coords[i][0], coords[i][1], hat_list[i])
		spawn_drone(task)


clear()
#thousand_flips()
#giant_pumpkin()
#recycling()
#stack_overflow()
#fashion_show()