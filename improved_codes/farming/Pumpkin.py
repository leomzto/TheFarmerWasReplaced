import Extras
import Ground

WORLD_SIZE = get_world_size()
FIRST_PASS = True

PUMPKIN = Entities.Pumpkin
DEAD_PUMPKIN = Entities.Dead_Pumpkin
 
SOILED_GROUND = Grounds.Soil

def check():
	posX, posY = Extras.get_pos()
	if posX != 0:
		move(East)
	
	l = measure()
	move(West)
	r = measure()
	move(East)
	
	return l == r

def wait_finish_plant(drones_list):
	for drone in drones_list:
		wait_for(drone)

def plant_botton_top():
	global WORLD_SIZE
	global FIRST_PASS
	
	global PUMPKIN 
	global DEAD_PUMPKIN
	
	global SOILED_GROUND
	
	for _ in range(WORLD_SIZE):
		if Extras.get_plant() != PUMPKIN:
			if Ground.get_groud() != SOILED_GROUND:
				Ground.soil()
			plant(PUMPKIN)
				
			if not FIRST_PASS:
				while not can_harvest():
					if Extras.get_plant() == DEAD_PUMPKIN:
						plant(PUMPKIN)
					use_item(Items.Fertilizer)
		
		move(North)
	
	if not FIRST_PASS:
		for _ in range(WORLD_SIZE):
			if  Extras.get_plant() == DEAD_PUMPKIN:
				plant(PUMPKIN)
			
			move(North)

def task():
	plant_botton_top()
	
def farm():
	global WORLD_SIZE
	global FIRST_PASS
	
	list_drones = []
	
	posX, posY = Extras.get_pos()
	if posX!= 0:
		move(East) 
	
	for _ in range(WORLD_SIZE - 1):
		list_drones.append(spawn_drone(task))
		move(East)
	
	plant_botton_top() 
	wait_finish_plant(list_drones)

def check_limit(max_items):
	return num_items(Items.Pumpkin) >= max_items
	
def main(max_items=None):
	clear()
	global FIRST_PASS
	
	if max_items != None:
		while True:
			if check_limit(max_items):
				break
			
			farm()
			FIRST_PASS = False
			
			if check():
				harvest()
				FIRST_PASS = True
				move(West)
	else:
		while True:
			farm()
			FIRST_PASS = False
			
			if check():
				harvest()
				FIRST_PASS = True
				move(West)
		
			
#main()