def coinToss(num):
    print "Starting the program..."
    tails_count = 0
    heads_count = 0
    for count in range(1, num+1):
        import random
        
        toss = random.random()
        # print toss
        toss_rounded = round(toss)
        # print toss_rounded
        
        if toss_rounded == 0:
            tails_count = tails_count + 1
            print "Attempt #",count, "Throwing a coin... It's a tails! ... Got", heads_count, "head(s) so far and", tails_count, "tail(s) so far"
        
        elif toss_rounded == 1:
            heads_count = heads_count + 1
            print "Attempt #",count, "Throwing a coin... It's a heads! ... Got", heads_count, "head(s) so far and", tails_count, "tail(s) so far"
    print "Ending the program. Thank You!"
print coinToss(5000)