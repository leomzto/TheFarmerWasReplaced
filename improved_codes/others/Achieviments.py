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


from Maze2 import *
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
			

#clear()
#thousand_flips()
#giant_pumpkin()
#recycling()
