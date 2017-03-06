import random
def scoresAndGrades():
    for num in range (0,11):
        import random
        score = (random.random()*60)+41
        if score >= 90:
            print "Score:", score, "; Your grade is A"
        elif score >= 80:
            print "Score:", score, "; Your grade is B"
        elif score >= 70:
            print "Score:", score, "; Your grade is C"
        elif score >= 60:
            print "Score:", score, "; Your grade is D"  
print scoresAndGrades()
print "End of the program. Bye!"
