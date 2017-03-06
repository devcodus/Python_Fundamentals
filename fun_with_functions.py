#fun_with_functions.py

#odd/evens
# for count in range(1,2001):
#     # print "Number is", count
#     if count % 2 == 0:
#         print count ,"This is an even number"
#     elif count % 2 == 1:
#         print count, "This is an odd number"

#multiply
def multiply(arr, num): 
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr

numbers_array = [2, 4, 6, 10, 16]
print multiply(numbers_array, 5)

#hacker_challenge


