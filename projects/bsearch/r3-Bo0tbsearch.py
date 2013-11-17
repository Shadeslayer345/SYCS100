''' Team r3-Bo0t 
	Barry Harris
	Errol Grannum
	Boluwatife Aiki-Raji
	Hallie Lomax
	Brittany Miller
	Eric Walker 
	Chris Quist'''

##Eric Walker
def bitSearch(y, s): ##begin bitsearch of y and the search variable
    sortingsort(y) ##calls the function sortingsort(y)
    print "Please wait while we attempt to find your query..." ##explains what it is doing
    extant = False ##assigns extant to be false
    startingPara = 0 ##assigns the starting parameter to equal 0
    endingPara = len(y) - 1 ##assigns the ending parameter to be the length of the list minus 1 since the length of a list is going to be 1 more than the final index
    search = s ##assigns search to be s
    while ((endingPara > startingPara + 1) and (extant == False)): ##says that while the ending is > starting + 1 (to even out the minus 1 of ending) and extant does not equal true
        midpoint = ((startingPara + endingPara) // 2) ##assigns the midpoint to be half of the sum of the starting and ending paras
        if search < y[midpoint]: ##sees if search is < y at the index of the midpoint
            endingPara = midpoint - 1 ##if so, the ending para now is the midpoint minus 1 to shift the function
        elif search > y[midpoint]: ##sees if search is  > y at index of the midpoint
            startingPara = midpoint + 1 ## if so, the starting para now is the midpoint + 1 to shift the function
        elif search == y[midpoint]: ## checks to see if the search is y index midpoint
            extant = True ##if so, extant = True, stopping the while loop
            print 'We found it, we found it, we found it, Yay!' #this is printed to assure the user that the search was found
        else:
            print 'Computer malfunction. Self destruct sequence activated. Please check search request...' ##tells the user that the search value was not found


# Chris Quist's binary search
def bsearch(wlist, item):
    beginning=0
    end = len(wlist)
    while beginning!=end:
        middle = (beginning + end)/2
        if item == wlist[ middle]:
            return middle
        elif item < wlist[middle]:
            end = middle
        else:
            if beginning == middle:
                return -1
            else:
                beginning = middle
    return -1
