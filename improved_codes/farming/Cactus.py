import Extras
import Movement
import Ground

set_world_size(6)

world_size = get_world_size()
cactus = Entities.Cactus

def soil_n_plant():
	global cactus
	if not Ground.is_soiled():
		Ground.soil()

	entity = Extras.get_plant()
	if entity == None:
		plant(cactus)
	else:
		if entity != cactus:
			if can_harvest():
				harvest()
			plant(cactus)

def fill_farm():
	Movement.go_home()
	for y in range(world_size):
		for x in range(world_size):
			soil_n_plant()
			if x < world_size - 1:
				move(East)
		if y < world_size - 1:
			move(North)
		if y % 2 == 1:
			for _ in range(world_size - 1):
				move(West)

def is_all_grown():
	Movement.go_home()
	for y in range(world_size):
		for x in range(world_size):
			entity = Extras.get_plant()
			if entity != cactus:
				return False
			if not can_harvest():
				return False
			if x < world_size - 1:
				move(East)
		if y < world_size - 1:
			move(North)
		if y % 2 == 1:
			for _ in range(world_size - 1):
				move(West)
	return True

def trigger_harvestables():
	if is_all_grown():
		Movement.go_home()
		if can_harvest():
			harvest()

def compare_n_swap_row():
	Movement.go_home()
	swapped = False
	direction_east = True

	for y in range(world_size):
		for x in range(world_size - 1):
			curr = measure()
			
			if direction_east:
				next_val = measure(East)
				if curr > next_val:
					swap(East)
					swapped = True
				move(East)
			else:
				next_val = measure(West)
				if curr < next_val:
					swap(West)
					swapped = True
				move(West)
		
		if y < world_size - 1:
			move(North)
		
		if direction_east:
			direction_east = False
		else:
			direction_east = True
	
	return swapped

def compare_n_swap_column():
	Movement.go_home()
	swapped = False

	for x in range(world_size):
		for y in range(world_size - 1):
			curr = measure()
			next_val = measure(North)
			if curr > next_val:
				swap(North)
				swapped = True
			move(North)
		
		for _ in range(world_size - 1):
			move(South)
		if x < world_size - 1:
			move(East)

	return swapped

def sort():
	while True:
		swapped = False

		row_swapped = compare_n_swap_row()
		if row_swapped:
			swapped = True

		col_swapped = compare_n_swap_column()
		if col_swapped:
			swapped = True

		if not swapped:
			break

def main():
	clear()
	fill_farm()
	
	while True:
		fill_farm()
		Movement.go_home()
		

		if is_all_grown():
			sort()
			trigger_harvestables()
			
main()
	
