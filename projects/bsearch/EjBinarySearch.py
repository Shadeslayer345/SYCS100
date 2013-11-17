MyList = [1,4,10,13,14,15,19,29,36]
Target = 13
 # iterative implementation
def BinarySearch(MyList,Target):
    low = 0
    high = len(MyList)
    while low < high:
        mid = (low + high)//2
        if Target > MyList[mid]:
            low = mid + 1
        elif Target < MyList[mid]:
            high = mid
        else: 
            return mid
    return "Number Not Found"
print BinarySearch(MyList,Target)
