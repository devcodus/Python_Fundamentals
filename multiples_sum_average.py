#multiples_sum_average.py

#Part 1

#FIRST ATTEMPT#
# for count in range (0, 1001):
# count = 0
# if (count < 1001 and
#         count % 2 == 1):
#     print count 
#     count += 1

count = 0
for count in range (1, 1001, 2):
    print count

# #Part 2
for count in range (5, 1000005, 5):
    print count

#Sum List
sum = 0
a = [1, 2, 5, 10, 255, 3]

for integer in a:
    sum = sum + integer

print sum

#Average List
sum = 0
avg = 0
a= [1, 2, 5, 10, 255, 3]
for integer in a:
    sum = sum + integer
avg = sum/len(a)
print avg

