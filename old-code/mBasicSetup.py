import Get
import mTreasure

size = get_world_size()

def can_plant_(plant_name):
	cost = get_cost(plant_name)
	missing = None

	for item in cost:
		if num_items(item) < cost[item]:
			missing = item
			break

	if missing:
		return (False, missing)
	return (True, None)

ITEM_TO_ENTITY = {
	Items.Power: Entities.Sunflower,
	Items.Wood: Entities.Tree,
	Items.Hay: Entities.Grass,
	Items.Carrot: Entities.Carrot,
	Items.Pumpkin: Entities.Pumpkin,
	Items.Cactus: Entities.Cactus
}

plants = [Entities.Grass, Entities.Bush, Entities.Carrot, Entities.Pumpkin,
		  Entities.Pumpkin, Entities.Pumpkin, Entities.Carrot, Entities.Sunflower,
		  Entities.Cactus, Entities.Grass, Entities.Bush]

def plant_c_b_g():
	global size
	for i in range(size):
		for j in range(size):

			if can_harvest():
				harvest()

			if get_water() < 0.5 and num_items(Items.Water) > size * size:
				use_item(Items.Water)
			index = j // 2
			plant_now = plants[index]

			if not Get.is_soiled():
				till()
			plant(plant_now)

			if plant_now == Entities.Pumpkin:
				if not can_harvest():
					plant(Entities.Pumpkin)
				move(North)
				continue

			move(North)
		move(East)

def plant_cell(plant_name, item_name=None, max_items=None, _recursion_depth=0):
	if _recursion_depth > 3:
		return False

	if item_name != None and max_items != None and num_items(item_name) >= max_items:
		return False

	can_plant, missing = can_plant_(plant_name)

	if can_plant:
		if can_harvest():
			harvest()
		if get_water() < 0.5 and num_items(Items.Water) > size * size:
			use_item(Items.Water)

		if plant_name not in [Entities.Grass, Entities.Tree] and not Get.is_soiled():
			till()

		if plant_name == Entities.Tree:
			if Get.is_soiled():
				till()
			if Get.is_even(get_pos_x()) and Get.is_even(get_pos_y()):
				plant(plant_name)
			else:
				plant(Entities.Bush)

		elif plant_name == Entities.Pumpkin:
			plant(plant_name)
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(plant_name)
				#if num_items(Items.Fertilizer) != 0:
					#use_item(Items.Fertilizer)
					
		elif plant_name == Entities.Sunflower:
			petalas = measure()

			if petalas == 15 and can_harvest():
				harvest()
			else:
				if get_entity_type() != Entities.Sunflower:
					plant(Entities.Sunflower)

		else:
			if not Get.is_soiled():
				till()
			plant(plant_name)
			if plant_name not in [Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot, Entities.Sunflower] and num_items(Items.Fertilizer) != 0:
				use_item(Items.Fertilizer)

		if can_harvest():
			harvest()
		return True

	else:
		entity_to_plant = ITEM_TO_ENTITY[missing] 
		if entity_to_plant:
			return plant_cell(entity_to_plant, item_name, max_items, _recursion_depth + 1)
		return False

def plant_row(plant_name, item_name=None, max_items=None):
	for _ in range(size):
		if not plant_cell(plant_name, item_name, max_items):
			break
		move(East)

def plant_all_board(plant_name, item_name=None, max_items=None):
	global size
		
	def row_task():
		for _ in range(size):
			if not plant_cell(plant_name, item_name, max_items):
				break
			move(East)

	for _ in range(size):
		if not spawn_drone(row_task):
			row_task()

		move(North)
		
def plant_(plant_name):
	global size
	for i in range(size):
		for j in range(size):

			if can_harvest():
				harvest()

			if get_water() < 0.25 and num_items(Items.Water) > size * size:
				use_item(Items.Water)

			if plant_name not in [Entities.Grass, Entities.Tree] and not Get.is_soiled():
				till()

			if plant_name == Entities.Tree:
				if Get.is_soiled():
					till()
				if Get.is_even(i) and Get.is_even(j):
					plant(plant_name)
				else:
					plant(Entities.Bush)
				move(North)
				continue

			if plant_name == Entities.Pumpkin:
				if not can_harvest():
					plant(plant_name)
					use_item(Items.Fertilizer)
				move(North)
				continue

			if not Get.is_soiled():
				till()

			plant(plant_name)
			if num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
			if can_harvest():
				harvest()

			move(North)
		move(East)

def do_action(action, sub_action=None, item_name=None, max_items=None):
	if action == "maze":
		if mTreasure.make_maze():
			found = mTreasure.search_treasure(0)
			if mTreasure.is_treasure():
				harvest()

	elif action == "farm":
		if sub_action != None and (item_name == None or num_items(item_name) < max_items):
			plant_all_board(sub_action, item_name, max_items)

	elif action == "multi_farm":
		plant_c_b_g()