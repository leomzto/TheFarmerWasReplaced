import Get
import mBasicSetup
import mTreasure

clear()

LIMITS = {
	Items.Wood: 1000000000,
	Items.Hay: 1000000000,
	Items.Carrot: 1000000000,
	Items.Pumpkin: 1000000000,
	Items.Cactus: 1000000000,
	Items.Power: 200000
}


ITEM_TO_ENTITY = {
	Items.Wood: Entities.Tree,
	Items.Hay: Entities.Grass,
	Items.Carrot: Entities.Carrot,
	Items.Pumpkin: Entities.Pumpkin,
	Items.Cactus: Entities.Cactus,
	Items.Power: Entities.Sunflower
}

PRIORITY = [Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin, Items.Cactus, Items.Power]

def farm_logic():
	for item in PRIORITY:
		if num_items(item) < LIMITS[item]:
			entity = ITEM_TO_ENTITY[item]
			mBasicSetup.do_action("farm", entity, item, LIMITS[item])
			
			return

	mBasicSetup.do_action("farm", Entities.Sunflower)

maze_size = 10
while True:
	farm_logic()
	#mTreasure.make_maze(maze_size)
	#mTreasure.search_treasure(0, maze_size)

