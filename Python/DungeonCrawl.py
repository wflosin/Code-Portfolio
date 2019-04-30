import random, time, msvcrt

#0 is empty space
#1 is wall
#2 is win space
#5 is maze gen point
#6 is untouched path
#7 is touched path
#8 is barrier wall
#9 is player space


def main():
	block = [",-------,",
			 "|       |",
			 "|       |",
			 "|       |",
			 "|_______|"]
	blank = "         "
	winspace = ["         ",
				" E       ",
				"   X     ",
				"     I   ",
				"       T "]
	playerspace = ["  _,==,_ ",
				   "  {'-'}  ",
				   "   <[]>  ",
				   "    /|   ",
				   "   / |   "]
	#5 and 7 are just placeholders
	mapping = [5,5,5,5,'',5,5,5,5]

	win = False

	player = "O"
	""" map1 = [1,1,1,1,1,1,1,1,1,1,1,1,
			1,0,0,0,0,1,0,0,0,0,0,1,
			1,1,1,1,0,0,0,1,0,1,0,1,
			1,0,0,1,0,1,1,2,1,0,0,1,
			1,0,1,1,0,0,1,0,0,0,1,1,
			1,0,0,0,1,0,0,1,1,1,1,1,
			1,0,1,0,0,1,0,0,1,0,0,1,
			1,1,0,1,0,0,1,0,1,0,1,1,
			1,1,0,0,1,0,1,0,1,0,0,1,
			1,1,0,1,1,0,0,0,1,1,0,1,
			1,0,9,0,0,0,1,0,0,0,0,1,
			1,1,1,1,1,1,1,1,1,1,1,1]
			"""

	running = True

	def mapng(mapping):
		#mapping = [1,0,1,0,"",0,1,1,1]
		row = [["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],
				["","",""],]

		#while loop to assign the 'textures' to the row variable
		#
		for i in range(9):
			if i < 3:
				if mapping[i] == 1 or mapping[i] == 8:
					for j1 in range(5): 
						row[j1][i] = block[j1]
				elif mapping[i] == 0:
					for j2 in range(5):
						row[j2][i] = blank
				elif mapping[i] == 2:
					for ja in range(5):
						row[ja][i] = winspace[ja]

			elif 3 <= i < 6:
				if mapping[i] == 1 or mapping[i] == 8:
					for j3 in range(5): 
						row[j3+5][i-3] = block[j3]
				elif mapping[i] == 0:
					for j4 in range(5):
						row[j4+5][i-3] = blank
				elif mapping[i] == 9:
					for j5 in range(5):
						row[j5+5][i-3] = playerspace[j5]
				elif mapping[i] == 2:
					for jb in range(5):
						row[jb+5][i-3] = winspace[jb]


			elif 6 <= i:
				if mapping[i] == 1 or mapping[i] == 8:
					for j6 in range(5): 
						row[j6+10][i-6] = block[j6]
				elif mapping[i] == 0:
					for j7 in range(5):
						row[j7+10][i-6] = blank
				elif mapping[i] == 2:
					for jc in range(5):
						row[jc+10][i-6] = winspace[jc]


		for x in range(15):
			print(row[x][0], row[x][1], row[x][2])

		"""
		print(row[0][0], row[0][1], row[0][2])
		print(row[1][0], row[1][1], row[1][2])
		print(row[2][0], row[2][1], row[2][2])
		print(row[3][0], row[3][1], row[3][2])
		print(row[4][0], row[4][1], row[4][2])
		print(row[5][0], row[5][1], row[5][2])
		print(row[6][0], row[6][1], row[6][2])
		print(row[7][0], row[7][1], row[7][2])
		print(row[8][0], row[8][1], row[8][2])
		print(row[9][0], row[9][1], row[9][2])
		print(row[10][0], row[10][1], row[10][2])
		print(row[11][0], row[11][1], row[11][2])
		print(row[12][0], row[12][1], row[12][2])
		print(row[13][0], row[13][1], row[13][2])
		print(row[14][0], row[14][1], row[14][2]) 

		[[',-------,', '         ', ',-------,'],
		 ['|       |', '         ', '|       |'],
		 ['|       |', '         ', '|       |'],
		 ['|       |', '         ', '|       |'],
		 ['|_______|', '         ', '|_______|'],
		 ['         ', '  _,==,_ ', '         '],
		 ['         ', "  {'-'}  ", '         '],
		 ['         ', '   <[]>  ', '         '],
		 ['         ', '    /|   ', '         '],
		 ['         ', '   / |   ', '         '],
		 [',-------,', ',-------,', ',-------,'],
		 ['|       |', '|       |', '|       |'],
		 ['|       |', '|       |', '|       |'],
		 ['|       |', '|       |', '|       |'],
		 ['|_______|', '|_______|', '|_______|']]
				"""

	def char(char_position, win, map1, mapsize):
		#CHaracter movement--
		#1,1,1,1,1
		#1,0,0,0,1
		#1,1,0,1,1
		#1,0,9,0,1
		#1,1,1,1,1
		move = False
		while move == False:
			inp = msvcrt.getch().decode().upper()
			if inp.upper() == 'W':
				if map1[char_position - mapsize] in [0,2]:
					map1[char_position] = 0
					char_position -= mapsize
					map1[char_position] = 9
					move = True
					#print("up", char_position)

			elif inp.upper() == 'S':
				if map1[char_position + mapsize] in [0,2]:
					map1[char_position] = 0
					char_position += mapsize
					map1[char_position] = 9
					move = True
					#print("down", char_position)

			elif inp.upper() == "A":
				if map1[char_position - 1] in [0,2]:
					map1[char_position] = 0
					char_position -= 1
					map1[char_position] = 9
					move = True
					#print("left", char_position, move)

			elif inp.upper() == "D":
				if map1[char_position + 1] in [0,2]:
					map1[char_position] = 0
					char_position += 1
					map1[char_position] = 9
					move = True 
					#print("right", char_position)

		return (char_position, win)

	def mapgen(mapsize=None):
		if mapsize < 4:
			print("Default: 12")
			time.sleep(1)
			mapsize = 12

		map_a = [1] * mapsize**2

		#bounds
		for i in range(mapsize):
			map_a[i] = 8
			map_a[(-i)-1] = 8
			if 0 < i < mapsize:
				map_a[mapsize*(i)] = 8
				map_a[mapsize*(i)+(mapsize-1)] = 8

		#5 current maze builder position
		#6 places its been
		#7 places its been twice
		
		#maze builder position
		while True:
			temp_pos = random.randrange(mapsize, len(map_a)-mapsize)
			if map_a[temp_pos] != 8:
				map_a[temp_pos] = 5
				break

		global udlr
		udlr = [mapsize, -mapsize, -1, 1]

		maze = False
		while maze == False:
			global movespot 
			movespot = map_a.index(5)
			direction = udlr[random.randrange(0,4)]

			if map_a[movespot + direction] == 1:
				counter2 = 0
				if (map_a[movespot + 2*direction] == 1):
					map_a[movespot + 2*direction] = 5
					map_a[movespot] = 6
					map_a[movespot + direction] = 6
			
			def dead_end(map_a):
				wall = 0
				for i in range(4):
					if (map_a[movespot+udlr[i]] == 8) or (map_a[movespot+2*udlr[i]] == 6) or \
					(map_a[movespot+2*udlr[i]] == 7) or (map_a[movespot+2*udlr[i]] == 8):
						wall += 1
					if wall == 4:
						return True
				if wall < 4:
					return False


			if dead_end(map_a) == True:
				#reverse algorithm
				while True:
					direction = udlr[random.randrange(0,4)]
					if map_a[movespot+direction] == 8:
						continue
					if (map_a[movespot+direction] == 6) and (map_a[movespot+2*direction] == 6):
						map_a[movespot+direction] = 7
						map_a[movespot] = 7
						map_a[movespot+2*direction] = 5
					if dead_end(map_a) == False:
						break

					#map is done code
					try: 
						index = map_a.index(6)
						continue
					except ValueError:
						map_a = [0 if i is 7 else i for i in map_a]
						#print(map_a)
						index = map_a.index(5)
						map_a[index] = 9
						maze = True
						break

		#assigning the win space
		while True:
			temp_pos = random.randrange(mapsize, len(map_a)-mapsize)
			if (map_a[temp_pos] != 8) or (map_a[temp_pos] != 1) or (map_a[temp_pos] != 9):
				map_a[temp_pos] = 2
				break

		return map_a


	def game(running):
		#map generation
		try:
			mapsize = int(input("Map size: "))
		except ValueError:
			print("Default: 12 x 12")
			time.sleep(1)
			mapsize = 12
		map1 = mapgen(mapsize)
		#print(map1)

		#game loop
		while running:
			char_position = map1.index(9)

			#assigns the 9 long mapping variable to fill the squares
			#around the player space: 9
			i = 0
			while i < 3:
				#1,1,1,1,1
				#1,0,0,0,1
				#1,1,0,1,1
				#1,0,9,0,1
				#1,1,1,1,1
				mapping[i] = map1[char_position - ((mapsize+1)-i)]
				mapping[i+3] = map1[char_position + (i-1)]
				mapping[i+6] = map1[char_position + ((mapsize-1)+i)]
				i += 1

			mapng(mapping)
			char(char_position, win, map1, mapsize)
			
			if 2 not in map1:
				print("You Win!")
				for w in range(13):
					print(" " * 27)
					running = False
				time.sleep(3)

	game(running)

if __name__ == "__main__":
	main()
