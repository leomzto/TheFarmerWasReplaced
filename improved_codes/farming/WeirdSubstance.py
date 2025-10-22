from Movement import move_to

def main(max_items=None):
	clear()
	move_to(4, 4)
	till()
	use_item(Items.Water)
	use_item(Items.Water)
	use_item(Items.Water)
	
	while True:
		if max_items != None and num_items(Items.Weird_Substance) >= max_items:
			break
		use_item(Items.Water)
		for _ in range(888):
			plant(Entities.Tree)
			if Entities.Grass in get_companion():
				use_item(Items.Fertilizer)
			harvest()
			
#main()