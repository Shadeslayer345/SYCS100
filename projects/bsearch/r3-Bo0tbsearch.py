''' Team r3-Bo0t 
	Barry Harris
	Errol Grannum
	Boluwatife Aiki-Raji
	Hallie Lomax
	Brittany Miller
	Eric Walker
	Kris '''

''' Recursive Function To Search The Sorted List (Barry) '''
def search(inputlist, searchValue, startSearchParameter, endSearchParameter):
		print len(inputlist)
		middleValue = ((startSearchParameter+endSearchParameter)/2)
		if (startSearchParameter <= endSearchParameter):
			if searchValue == inputlist[middleValue]:
				return middleValue
			else:	
				if searchValue < inputlist[middleValue]:
					endSearchParameter = middleValue - 1
					return search(inputlist, searchValue, startSearchParameter, endSearchParameter)
				else:
					startSearchParameter = middleValue + 1
					return search(inputlist, searchValue, startSearchParameter, endSearchParameter)
		else:
			return -1
			
''' Final Main Function Search The List (Barry) '''
def binarySearch(list, searchValue):
	print "\nBinary Searching........."
	startParameter = 0
	endParameter = len(list)-1
	message = search(list, searchValue, startParameter, endParameter)
	if message == -1:
		print "Search Value not found.... %d does not appear to be in the given list" %searchValue
	else:
		print "\nSearch value %d found at position %d" % (searchValue, message)