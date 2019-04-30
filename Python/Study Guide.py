import time, json
def main():
	#f = open("Documents/Programs/Python Programs/Study Guide Data", 'a')
	#cal = {"{}/{}/18".format(j+1,i+1):None for i in range(12) for j in range(month_len[i+1])}
#################################################################################################
	def tomorrowf(today,month_len):
		today_l = list(today)
		date = [int(''.join(today_l[:2])),int(''.join(today_l[3:5])),int(''.join(today_l[6:]))]
		#if the day bypasses the max of that month
		if date[1] >= month_len[date[0]]:
			date[1] = 0
			#only works for months 10-12
			date[0]+=1
		date[1]+= 1
		tomorrow = str(date).replace(', ','/').replace("[","").replace("]","")
		print(tomorrow, "tomorrow")
		return tomorrow
	def weekf(today,month_len):
		today_l = list(today)
		date = [int(''.join(today_l[:2])),int(''.join(today_l[3:5])),int(''.join(today_l[6:]))]
		for i in range(7):
			#if the day bypasses the max of that month
			if date[1] >= month_len[date[0]]:
				date[1] = 0
				#only works for months 10-12
				date[0]+=1
			date[1]+= 1
			print(i,date[1])
		week = str(date).replace(', ','/').replace("[","").replace("]","")
		print (week, "week")
		return week
################################################################################################
	#with open("Documents/Programs/Python Programs/Study Guide Data", 'a') as f:
	#calendar = json.load(f)
	jsonFile = open("Documents/Programs/Python Programs/StudyGuideData.json", "r") # Open the JSON file for reading
	calendar = json.load(jsonFile) # Read the JSON into the buffer
	jsonFile.close() # Close the JSON file
	month_len = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
	today = time.strftime("%x")
	print(today)
	while True:
		while True:
			try:
				inp = input("add work, home work\n").lower()
			except NameError:
				continue
			break
		if inp == 'quit':
			return

		#add work
		if inp in ['add work',1,'add']:
			while True:	
				work = input("What did you learn today, son?\n")
				if work == 'quit':
					return
				elif work == 'back':
					break				
				while True:
					try:
						inp2 = input('is "{}" right? [y/n]\n'.format(work)).lower()
					except NameError:
						continue
					break
				if inp2 == 'quit':
					return
				elif inp2 == 'back':
					break
				if inp2 in ['yes','y']:
					###what is today?
					calendar[today].append(work)
					#print(today_l,"1")
					###what is tomorrow?
					tomorrow = tomorrowf(today,month_len)
					calendar[tomorrow].append(work)
					###a week from now?
					#print(today_l,"2")
					week = weekf(today,month_len)
					calendar[week].append(work)

					## Save our changes to JSON file
					jsonFile = open("Documents/Programs/Python Programs/StudyGuideData.json", "w+")
					jsonFile.write(json.dumps(calendar))
					jsonFile.close()


		#home work
		elif inp in ['home work',2,'home']:
			while True:
				when = input("[today]? [tomorrow]? a [week]? a date? [M(M)/D(D)/YY] or [quit]\n")
				if when == 'quit':
					return
				elif when == 'back':
					break						
				if when == 'today':
					if '/0' in today:
						today_new = today.replace('/0','/')
					print(today)
					print("\nWhat you need to study:\n"+str(calendar[today_new])+'\n')
				elif when == "tomorrow":
					tomorrow = tomorrowf(today,month_len)
					print("\nWhat you need to study:\n"+str(calendar[tomorrow])+'\n')
				elif when == 'week':
					week = weekf(today,month_len)
					print(week,"ya")
					print("\nWhat you need to study:\n"+str(calendar[week])+'\n')
				#if you input a date
				elif "/" in when:
					try:
						print("\nWhat you need to study:\n"+str(calendar[when])+'\n')
					except KeyError:
						continue

if __name__ == '__main__':
	main()

