# Dinosaur
import Extras

dino_hat = Hats.Dinosaur_Hat
world_size = get_world_size()
half_w_size = (get_world_size()**2/2)

def init_phase():
	next_targ = measure()
	
	if next_targ:
		next_targ_x, next_targ_y = next_targ
	else:
		next_targ_x, next_targ_y = Extras.get_pos()
	
	dino_body = []
	tail_length = 0
	
	global half_w_size
	
	while tail_length < half_w_size:
		
		is_x_pos_even = Extras.is_even(get_pos_x())
		is_y_pos_even = Extras.is_even(get_pos_y())
		
		if is_x_pos_even:
			if is_y_pos_even:
				if next_targ_y < get_pos_y():
					if not move(South):
						move(East)
				else:
					if not move(East):
						move(South)
						
			else:
				if next_targ_x < get_pos_x():
					if not move(West):
						move(South)
				else:
					if not move(South):
						move(West)
						
		else:
			if is_y_pos_even:
				if next_targ_x > get_pos_x():
					if not move(East):
						move(North)
				else:
					if not move(North):
						move(East)
						
			else:
				if next_targ_y > get_pos_y():
					if not move(North):
						move(West)
				else:
					if not move(West):
						move(North)
					
		dino_body.append(Extras.get_pos())
		
		if measure():
			next_targ_x, next_targ_y = measure()
			tail_length += 1
			
		else:
			dino_body.pop(0)
		
	return dino_body
	
	
def assemble_path(dino_body):
	cells = []
	
	y = 0
	while y < world_size:
		if Extras.is_even(y):
			x = 0
			
			while x < world_size:
				cells.append((x, y))
				x += 1
				
		else:
			x = world_size - 1
			
			while x >= 0:
				cells.append((x, y))
				x -= 1
				
		y += 1
		
	hx, hy = Extras.get_pos()
	
	h_index = 0
	
	i = 0
	
	while i < len(cells):
		cell_x, cell_y = cells[i]
		
		if cell_x == hx and cell_y == hy:
			h_index = i
			break
		i += 1
		
	if h_index > 0:
		cells = cells[h_index:] + cells[:h_index]
		
	path = []
	i = 1
	
	while i < len(cells):
		pos_x, pos_y = cells[i - 1]
		cell_x, cell_y = cells[i]
		
		dir_x = cell_x - pos_x
		dir_y = cell_y - pos_y
		
		if dir_x == 1 and dir_y == 0:
			path.append(East)
		elif dir_x == -1 and dir_y == 0:
			path.append(West)
		elif dir_y == 1 and dir_x == 0:
			path.append(North)
		elif dir_y == -1 and dir_x == 0:
			path.append(South)
			
		i += 1
		
	return path
	
def execute_path(path, max_items=None):
	while True:
		if max_items != None and check_limit(max_items):
			break
		for direction in path:
			if max_items != None and check_limit(max_items):
				return
			if not move(direction):
				return
	

def check_limit(max_items):
	return num_items(Items.Bone) >= max_items
	
def main(max_items=None):
	#set_world_size(world_size / 2)
	clear()
	change_hat(dino_hat)
	
	dino_body = init_phase()
	path = assemble_path(dino_body)
	
	execute_path(path, max_items)
	
	clear()
	
main()
	