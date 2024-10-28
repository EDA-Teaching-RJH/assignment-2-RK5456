### Part Three -- your code goes here. 

Unsorted = {3,1,4,1,5,9,2,6,5,3}

sortednumbers = sorted(Unsorted)

# in the loop, I will remove the 1's shown
while 1 in sortednumbers:
    sortednumbers.remove(1)

# here as said 7 and 8 will be added to the end of list
sortednumbers.extend({7,8})

print(sortednumbers)