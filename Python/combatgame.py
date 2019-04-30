import time
import random

def main():
	#[a,b,c, d] 
	#[0] is the monster's health, 
	#[1] is its speed, 
	#[2] is its damage, 
	#[3] is its armour class
	goblin = [8, 2, 4, 2]
	spider = [12, 5, 6, 4]
	dragon = [30, 7, 10, 7]
	smiley = [21, 6 , 8, 1]
	weapon = None

	print("This is a combat simulator")
	time.sleep(1)
	print("")

	"""
	new weapon template
	elif weaponch in []:
		print("")
		time.sleep(0.5)
		print("")
		weapon = [, ]
	"""

	while weapon == None:
		weaponch = str.lower(input("Choose your weapon! \n"))
		if weaponch in ['dagger', 'knife', 'pointy stick', 'throwing knife', 'throwing knives', 'knives','shank']:
			print("You chose to use a pointy dagger!")
			time.sleep(0.5)
			print("Daggers are very fast, but very weak")
			#[a,b] a[0:10], speed. b[0:10], damage
			weapon = [4, 1]

		elif weaponch in ['short sword','machete']:
			print("You chose to use a short sword!")
			time.sleep(0.5)
			print("Short swords are fast, but weak")
			weapon = [3, 2]

		elif weaponch in ['long sword', 'sword']:
			print("You chose to use a long sword!")
			time.sleep(0.5)
			print("Long swords are average in speed and damage")
			weapon = [3, 3]

		elif weaponch in ['battle ax', 'wits']:
			print("You chose to use a battle ax!")
			time.sleep(0.5)
			print("Battle axes are strong, but slow")
			weapon = [2, 4]

		elif weaponch == 'great sword':
			print("You chose to use a great sword!")
			time.sleep(0.5)
			print("Great swords are very strong, but very slow")
			weapon = [1, 5]

		elif weaponch == 'stick':
			print("You saw the rack of weapons but you don't confide to society's standards,")
			time.sleep(0.5)
			print("so you pick up a stick on the ground")
			time.sleep(0.5)
			print("Sticks are very fast, but extremely weak")
			weapon = [4, 1]	

		elif weaponch in ['laser sword', 'light saber', 'lightsaber']:
			print("You chose to use the mythical laser sword!")
			time.sleep(0.5)
			print("Laser swords are deadly, and extremely fast")
			weapon = [5, 10]

		elif weaponch in ['charisma', 'my looks', 'my good looks', 'sexiness', 'my face', 'my beautiful face', 'charm']:
			print("You chose to use you charm!")
			time.sleep(0.5)
			print("You're pretty gorgeous, you've got this battle in the bag")
			weapon = [10, 1]	

		elif weaponch in ['mace', 'morning star', 'club']:
			print("You chose to use a mace!")
			time.sleep(0.5)
			print("Maces are slow but deadly!")
			weapon = [2, 5]

		elif weaponch in ['magic', 'dark magic', 'spells', 'will', 'will power', 'spookiness', 'magic missile', 'fireball']:
			print("You chose to use deadly magic!")
			time.sleep(0.5)
			print("Magic is literally the best way to go!")
			weapon = [10, 10]

		elif weaponch in ['nap', 'sleep', 'rest', 'take a nap']:
			print("You chose to go to sleep!")
			time.sleep(0.5)
			print("Sleep well!")
			weapon = [0, 0]

		elif weaponch in ['bomb', 'nuke', 'atomic bomb', 'hydrogen bomb', 'grenade','explosives', 'bazooka', 'grenade launcher', 'rocket launcher']:
			print("You chose to use deadly explosives!")
			time.sleep(0.5)
			print("Bombs are far past slow, but incinerates anything in its path!")
			weapon = [0.3, 100]

		elif weaponch in ['test']:
			print("test weapon")
			time.sleep(0.5)
			weapon = [100, 100]

		elif weaponch in ['gun', 'pistol', 'rifle', 'sniper rifle', 'assault rifle']:
			print("You chose to use a gun!")
			time.sleep(0.5)
			print("Guns are fast and powerful!")
			weapon = [5, 7]

		elif weaponch in ['spear', 'pike', '11-foot pole', 'staff', 'rod']:
			print("You chose to use a spear!")
			time.sleep(0.5)
			print("spears are fast and average in damage")
			weapon = [5, 3]

		elif weaponch in ['potato', 'potahto', 'carrot', 'peas', 'potato gun', 'tomato', 'radishes', 'cilantro', 'waffles', 'spam', 'ghost pepper','potato launcher']:
			print("You chose to try and start a food fight!")
			time.sleep(0.5)
			print("Food is delicious, but not practical in a real fight")
			weapon = [6, 1]

		elif weaponch in ['peace', 'talk', 'words', 'my words', 'compromise', 'diplomacy', 'hugs', 'justice', 'law', 'order', 'law and order', 'the united nations','friendship', 'community']:
			print("You chose to not fight!")
			time.sleep(0.5)
			print("Just because you won't attack, doesn't mean they won't")
			weapon = [0, 100]

		elif weaponch in ['deception', 'lies', 'trickery', 'evil']:
			print("You decide to deceive you foe!")
			time.sleep(0.5)
			print("trickery is slow but deadly")
			weapon = [1, 6]

		elif weaponch in ['staring contest', 'looking', 'my eyes', 'eyes', 'stare']:
			print("You decided to have a staring contest with your foe!")
			time.sleep(0.5)
			print("First to break loses!")
			weapon = [3, 3]

		elif weaponch in ['fists', 'fisticuffs', 'bare hands', 'bare handed', 'hand to hand', 'hand', 'fist']:
			print("You decided to fight with your bare hands!")
			time.sleep(0.5)
			print("Your fists are extremely fast, and extremely weak")
			weapon = [8, 1]

		elif weaponch in ['rock', 'rocks', 'stone', 'stones', 'tomahawk', 'rotten tomato', 'rotten tomaotes', 'throwing weapon', 'sling', 'pebbles']:
			print("You decided to go with a throwing weapon!")
			time.sleep(0.5)
			print("They're slow but pack a punch!")
			weapon = [1, 5]

		elif weaponch in ['whip', 'sock whip', 'rope']:
			print("You decided to use a whip!")
			time.sleep(0.5)
			print("whips are fast and pretty deadly")
			weapon = [5, 6]

		elif weaponch in ['stapler', 'staple gun', 'nail gun']:
			print("You decided to use a staple gun!")
			time.sleep(0.5)
			print("Fast, but the stples don't do much")
			weapon = [3, 2]

		elif weaponch in ['wooden spoon','fork','ladle','spoon','spatula','soup spoon','whisk','plastic spoon','spork','butter knife']:
			print("You decided to use kitchen utensils")
			time.sleep(0.5)
			print("Fast, but don't do much")
			weapon = [6, 1]

		elif weaponch in ['frying pan','pot','sauce pan','wok']:
			print("You chose to use A FRIGGEN FRYING PAN")
			time.sleep(0.5)
			print("You are now a certified badass")
			weapon = [5, 6]

		elif weaponch in ['memes','meme','dank memes','dat boi','yeet']:
			print("You chose to use memes as a weapon")
			time.sleep(0.5)
			print("Memes are the best thing to arise on this planet")
			weapon = [3, 20]

		elif weaponch in ['fast test']:
			print("Fast weapon test")
			time.sleep(0.5)
			weapon = [100, 0]

		elif weaponch in ['taser', 'stun stick', 'shock stick', 'electric fence', 'electric chair', 'static electricity', 'tesla coil']:
			print("You chose the power of electricity!")
			time.sleep(0.5)
			print("BZZZZZZT ZAP ZAP")
			weapon = [11, 7]

		else:
			print("That's not a valid option.\n")

	#[a,b,c] a, player health. b, player speed. c, player damage. 
	player = [20, weapon[0], weapon[1]]

	time.sleep(2)
	print("")	

	for wtf in ['goblin', 'spider', 'dragon', 'smiley']:
		wtf = str.lower(input("Do you want to fight a goblin, a spider or a dragon? \n"))
		if wtf in ['goblin', 'spider', 'dragon', 'smiley']:
			print("You chose to fight a " + wtf)
			print("")
			time.sleep(1)
			break
		else:
			print("You can't see that monster")
			time.sleep(1)
			continue

	if wtf == 'goblin':
		print("A nasty looking goblin approaches!")
		time.sleep(0.5)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("░░░░░░░░░THE GOBLIN  ATTACKS YOU░░░░░░░░")
		print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████")
		print("███░░░░░░░░░░░░░░███████████░░████████░░")
		print("████████░░░░██████▒█▒▒█▒▒▒▒███▒▒▒███░░░░")
		print("░░░████▒█████▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒██░░░░░░░")
		print("░░░░░░████▒▒▒▒▒▒███▒▒▒▒███▒▒▒█████░░░░░░")
		print("░░░░░░██▒▒▒▒▒▒▒▒█o█▒▒▒▒█o█▒▒▒▒▒▒▒██░░░░░")
		print("░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒██░░░░░")
		print("░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒███░░░░░░")
		print("░░░░░████▒▒▒▒▒▒▒█_█_█_█_█▒▒▒████░░░░░░░░")
		print("░░░░░░░░█████▒▒█_█_█_█_█▒█████░░░░░░░░░░")
		print("░░░░░░░░░░░░█████▒▒▒▒▒▒▒████░A░░░░░░░░░░")
		print("░░░░░░░░░░░░░░░░░████████░░░░█░░░░░░░░░░")
		print("░░░░░░░░░░░░░░░░░█▒▒░█░░░░░░_█_░░░░░░░░░")
		print("░░░░░░░░░░░░░░████▒▒▒██░░░░░░█░░░░░░░░░░")
		print("░░░░░░░░░░░░██░▒▒▒▒▒▒▒████████░░░░░░░░░░")
		print("░░░░░░░░░░░██░▒▒▒▒▒▒▒▒▒████░░░░░░░░░░░░░")
		print("░░░░░░░░░░░█░██░▒▒▒▒░███░░░░░░░░░░░░░░░░")
		print("░░░░░░░░░░██░██░▒▒▒▒██░░░░░░░░░░░░░░░░░░")
		print("░░░░░░░░░░░█████▒▒▒▒█░░░░░░░░░░░░░░░░░░░")
		print("░░░░░░░░░░░░░░░█▒▒▒▒█░░░░░░░░░░░░░░░░░░░")
		print("░░░░░░░░░░░░░░███████░░░░░░░░░░░░░░░░░░░")
		print("░░░░░░░░░░░░░░█░░░░░██░░░░░░░░░░░░░░░░░░")
		print("░░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░░░░░")
		print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("")
		time.sleep(2)
		monster = goblin
		monstername = 'goblin'
		#goblin stats [8, 2, 2, 12]
	
		#spider
	elif wtf == 'spider':
		print("A massive spider approaches!")
		time.sleep(0.5)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("░░░░░░░░░░░░THE SPIDER  ATTACKS YOU░░░░░░░░░░░░")
		print("░░░░░░░░░░░░░░░░░░░██████████░░████░░░░░░░░░░░░")
		print("░░░░░░███████░█████▒▒█████▒░█████░██░░░░░░░░░░░")
		print("░░░░░███░░░███░▒▒░▒▒█░░░░░█░▒░░░████░░░░░░░░░░░")
		print("░░░░░░██████░░▒▒▒▒░█░██░██░█▒▒▒▒░░███████░░░░░░")
		print("░░░███████░▒▒▒▒▒▒▒▒░█░░▒░░█░▒▒▒▒░░██░░████░░░░░")
		print("░████░░░█▒▒▒▒▒▒▒▒▒▒▒░█░█░█░▒▒▒▒▒░░███░░░░███░░░")
		print("░█░░░░░░█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██▒███░░░█░░░")
		print("░░░██▒▒████░░░▒▒▒███████████▒▒░░███░░░████░░░░░")
		print("░░█▒▒██░░█████████▒█▒█▒▒█▒█░█░░██████░░░███░░░░")
		print("░████░░░██░██░░█▒▒█▒█▒▒█▒█▒▒█████▒▒▒░█░░░░█░░░░")
		print("░██░░░░░█░▒█░░░█▒▒▒▒▒▒▒▒▒▒▒▒█░░░░██▒▒░█░░░░░░░░")
		print("░░░░░░░░█▒▒█░░░░██░░████░░██░░░░░░░░███░░░░░░░░")
		print("░░░░░░░░█▒██░░░░░██░░░░░░██░░░░░░░░░░██░░░░░░░░")
		print("░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
		print("░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
		monster = spider
		time.sleep(2)
		monstername = 'spider'
		#spider stats [12, 5, 1, 8]

		#dragon
	elif wtf == 'dragon':
		print("A collosal dragon approaches! \n")
		time.sleep(0.5)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("              THE DRAGON  ATTACKS YOU              ")
		print("              __                  __               ")
		print("             ( _)                ( _)              ")
		print("            / /  \              / /\_\_            ")
		print("           / /    \            / / | \ \           ")
		print("          / /      \          / /  |\ \ \          ")
		print("         /  /   ,  \ ,       / /   /|  \ \         ")
		print("        /  /    |\_ /|      / /   / \   \_\        ")
		print("       /  /  |\/ _ '_|\    / /   /   \     \       ")
		print("      |  /   |/  O \O\ \  / |    |    \     \      ")
		print("      |    |\|      \_\_ /  /    |     \     \     ")
		print("      |  | |/    \.\ o\o)  /      \     |     \    ")
		print("      \    |     /\,`v-v  /        |    |      \   ")
		print("       | \/    /_| \,_|  /         |    | \     \  ")
		print("       | |    /__/_     /   _____  |    |  \     \ ")
		print("       \|    [__]  \_/  |_________  \   |   \    ()")
		print("        /    [___] (    \         \  |\ |   |   // ")
		print("       |    [___]                  |\| \|   /  |/  ")
		print("      /|    [____]                  \  |/\ / / ||  ")
		print("     (  \   [____ /     ) _\      \  \    \| | ||  ")
		print("      \  \  [_____|    / /     __/    \   / / //   ")
		print("      |   \ [_____/   / /        \    |   \/ //    ")
		print("      |   /  '----|   /=\____   _/    |   / //     ")
		print("   __ /  /        |  /   ___/  _/\    \  | ||      ")
		print("  (/-(/-\)       /   \  (/\/\)/  |    /  | /       ")
		print("                (/\/\)           /   /   //        ")
		print("                       _________/   /    /         ")
		print("                      \____________/    (          ")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
		monster = dragon
		time.sleep(2)
		monstername = 'dragon'

	elif wtf == 'smiley':
		print("")
		time.sleep(0.5)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("            ;)              ")
		print("                            ")
		print("        ,----------.        ")
		print("       /  __    __  \       ")
		print("      |  |  |  |  |  |      ")
		print("     @|  |__|  |__|  |@     ")
		print("      |  \   .\   /  |      ")
		print("       \  \______/  /       ")
		print("        \     _    /        ")
		print("         '--------'         ")
		print("              |   __        ")
		print("             /|\_[.']^^^^^\ ")
		print("            / |  '--'vvvvv/ ")
		print("             / \            ")
		print("           _/   \_          ")
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
		monster = smiley
		time.sleep(2)
		monstername = 'smiley'

	combat(player, monster, monstername)

	again = str.lower(input("Do you want to play again? [y/n] "))
	if again in ['yes', 'y', 'yas', 'sure', 'okay', 'why not', 'yolo']:
		main()
	else:
		pass

def combat(player, monster, monstername):
	pspeed = player[1]
	espeed = monster[1]
	palive = True
	ealive = True
	critical = 1
	while (palive or ealive) == True:
		if pspeed >= espeed:

			espeed += monster[1]
			input("It's your turn! Press [enter] to attack!")
			ptohit = random.randrange(1, 21)

			if ptohit > monster[3]:
				if ptohit == 20:
					print("Critical hit!")
					critical = 2

				tedamage = (random.randrange(1, player[2]+2)) * critical
				print("You hit for %2s damage!" % tedamage)
				monster[0] -= tedamage
				critical = 1
				time.sleep(1)

			else:
				print("You missed!")
				time.sleep(1)
		else:
			pspeed += player[1]
			print("The %6s attacks!" % monstername)
			time.sleep(1)
			etohit = random.randrange(1, 21)

			if etohit > 10:
				if etohit == 20:
					print("Critical hit!")
					critical = 2
				tpdamage = (random.randrange(1, monster[2]+2)) * critical
				print("You get hit for %2i damage!" % tpdamage)
				player[0] -= tpdamage
				critical = 1
				time.sleep(1)
			else:
				print("the %6s missed!" % monstername)
				time.sleep(1)

		#death calculations	[0]
		if player[0] < 0:
			palive = False
		else:
			palive = True
			print("You are at %2i health" % player[0])
			print("")
		if monster[0] < 0:
			ealive = False
		else:
			ealive = True
		
		if (palive and not ealive) == True:
			print("You killed the %6s! \n" % monstername)
			return
		elif (ealive and not palive) == True:
			print("The %6s killed you! \n" % monstername)
			return
		elif (ealive and palive) == False:
			print("You both died!\n")
			return

		else:
			continue

if __name__ == '__main__':
	main()
