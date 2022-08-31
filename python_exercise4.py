# Asks the user for a number that is divisible by 2                                  
# Keep asking until the user provides a number that is divisible by 2.               
#print 'Question 4. \n'

def isDivisibleBy2(num):
    if (num % 2) == 0:
        return True
    else:
        return False

print(isDivisibleBy2(10))
print(isDivisibleBy2(15))

#Output:
True
False

