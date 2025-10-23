import Extras
import Ground
import PlantSystem

WORLD_SIZE = get_world_size()

SOILED_GROUND = Grounds.Soil

SUNFLOWER = Entities.Sunflower

def make_task(target_petal, is_replanting):
	global WORLD_SIZE
	
	posX, _ = Extras.get_pos()

	def task():
		for _ in range(WORLD_SIZE):
			if measure() == target_petal:
				while not can_harvest():
					use_item(Items.Fertilizer)
				harvest()
			
			if is_replanting:
				if Extras.get_plant() != SUNFLOWER:
					PlantSystem.replant(SUNFLOWER)
			
			move(North)
			
		return
		
	return task

def task_setup():
	global WORLD_SIZE
	
	for _ in range(WORLD_SIZE):
		if can_harvest():
			harvest()
			
		PlantSystem.replant(SUNFLOWER)
		move(North)
		
	return

def task_manager():
	global WORLD_SIZE
	
	first_run = True
	
	while True:
		if first_run:
			for _ in range(WORLD_SIZE - 1):
				spawn_drone(task_setup)
				move(East)
				
			task_setup()
			move(East)
			
			first_run = False
		
		for petal_count in range(15, 7, -1):
			drone_task = make_task(petal_count, False)
			for _ in range(WORLD_SIZE - 1):
				spawn_drone(drone_task)
				move(East)
				
			drone_task()
			move(East)
		
		_replant = make_task(7, True)
		for _ in range(WORLD_SIZE - 1):
			spawn_drone(_replant)
			move(East)
			
		_replant()
		move(East)

def farm_power():
	task_manager()
	
def main():
	clear()
	while True:
		farm_power()
		
main()
		