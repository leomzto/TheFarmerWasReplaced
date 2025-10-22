# MultiFarm AFK
import Hay
import Wood
import Carrot
import Pumpkin
import Sunflower
import WeirdSubstance
import Maze2
import Dinosaur
import Cacti

WEIRD_SUBSTANCE = "Entities_WeirdSubstance"

ITEM_CONVERSION = {
	Items.Power: Entities.Sunflower,
	Items.Wood: Entities.Tree,
	Items.Hay: Entities.Grass,
	Items.Carrot: Entities.Carrot,
	Items.Pumpkin: Entities.Pumpkin,
	Items.Cactus: Entities.Cactus,
	Items.Bone: Entities.Dinosaur,
	Items.Weird_Substance: WEIRD_SUBSTANCE,
	Items.Gold: Entities.Treasure
}

LIMITS = {
	Items.Power:  185000,
	Items.Hay: 10000000000,
	Items.Wood: 30000000000,
	Items.Carrot: 10000000000,
	Items.Pumpkin: 1000000000,
	Items.Cactus: 10, # * BILLION MULTIPLIER
	Items.Bone: 100000000,
	Items.Weird_Substance: 30000000,
	Items.Gold: 100000000
}

PRIORITY = [Items.Hay, Items.Wood, Items.Carrot, Items.Pumpkin, Items.Cactus, Items.Bone, Items.Weird_Substance, Items.Gold, Items.Power]

def multi_farm():
	global WEIRD_SUBSTANCE
	for item in PRIORITY:
		while num_items(item) < LIMITS[item]:
			entity = ITEM_CONVERSION[item]
			
			if entity == Entities.Sunflower:
				Sunflower.main(LIMITS[item])
			elif entity == Entities.Grass:
				Hay.main(LIMITS[item])
			elif entity == Entities.Tree:
				Wood.main(LIMITS[item])
			elif entity == Entities.Carrot:
				Carrot.main(LIMITS[item])
			elif entity == Entities.Pumpkin:
				Pumpkin.main(LIMITS[item])
			elif entity == Entities.Cactus:
				Cacti.main(LIMITS[item])
			elif entity == Entities.Dinosaur:
				Dinosaur.main(LIMITS[item])
			#elif entity == WEIRD_SUBSTANCE:
				#WeirdSubstance.main(LIMITS[item])
			#elif entity == Entities.Treasure:
				#Maze2.main(LIMITS[item])
			else:
				break

	# farm gold if all full
	#Maze2.main()
	Dinosaur.main()
	
def main():
	multi_farm()
	
main()