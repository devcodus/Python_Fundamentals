#Part 1
def draw_stars(arr):
    for x in arr:
        print x * "*"
draw_stars([3,4,7,11])

#first attempt#
# list = [3,6,1]
# list = str(list)
# print '\n'.join(list)*"*"

# print str(3) + "hi"

# print [2,3,1,2]/4

#Part 2
def str_and_int_stars(arr):   
    y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    # for item in y:
    #     print item
    for item in y:
        if isinstance(item, str):
            item = item.lower()
            print len(item)*item[0] 
        elif():
        # isinstance(item, number):
            print item * "*"
str_and_int_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])        
