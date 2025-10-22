# Cactus farm_cact
import PlantSystem
import Drones
import Extras
import Numbers

WORLD_SIZE = get_world_size()

MAX_DRONES = max_drones()


CACTI = Entities.Cactus
CACTI_AMOUNT = num_items(Items.Cactus)


def plant_cacti():
	global WORLD_SIZE
	
	global CACTI
	
	global MAX_DRONES
	
	drone_list = []
	
	def row():
		for y in range(WORLD_SIZE):
			PlantSystem.plant_crop(CACTI)			
			move(North)
			
		return True
		
	for x in range(WORLD_SIZE):
		if num_drones() >= MAX_DRONES:
			row()
			break
			
		if x != WORLD_SIZE - 1:
			drone_list.append(spawn_drone(row))
		move(East)
		
	for d in drone_list:
		while not wait_for(d):
			continue
			
def swap_cactus(pos):
	x, y = Extras.get_pos()
	
	center = measure()
	needs_swap = True
	
	if pos == North:
		top_side = measure(North)
		bottom_side = measure(South)
		
		if y != WORLD_SIZE - 1:
			if center > top_side:
				swap(North)
				needs_swap = False
				
		if y != 0:
			if center < bottom_side:
				swap(South)
				needs_swap = False
				
	if pos == East:
		left_side = measure(West)
		right_side = measure(East)
		
		if x != WORLD_SIZE - 1:
			if center > right_side:
				swap(East)
				needs_swap = False
				
		if x != 0:
			if center < left_side:
				swap(West)
				needs_swap = False
				
	if not needs_swap:
		swap_cactus(pos)
		
	return needs_swap
	
def sort_farm():
	global WORLD_SIZE
	
	for p in [(North, East), (East, North)]:
		Drones.send_home()
		
		def row():
			while True:
				swap_controller = True
				
				for _ in range(WORLD_SIZE):
					sw = swap_cactus(p[1])
					
					if swap_controller:
						swap_controller = sw
					move(p[1])
				
				if swap_controller:
					return True
				
		Drones.send_home()
			
		drone_list = []
		for i in range(WORLD_SIZE):
			drone = spawn_drone(row)
				
			if drone != None:
				drone_list.append(drone)
				move(p[0])
			else:
				row()
					
		for d in drone_list:
			wait_for(d)
				
def farm_cacti(amount):
	
	MULTIPLIER = PlantSystem.MULTIPLIER * Numbers.BILLION
	TOTAL_AMOUNT = amount * MULTIPLIER
	
	while num_items(Items.Cactus) < TOTAL_AMOUNT:
		Drones.send_home()
		plant_cacti()
		sort_farm()
		harvest()
		
	return True
	
def main(max_items=10):
	clear()
	farm_cacti(max_items)
		

main(10)