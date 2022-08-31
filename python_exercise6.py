#Write a Python program that takes distance and time as input and displays the speed in, meters per
#second, kilometres per hour and miles per hour

#a) Store all given inputs in variables (distance, and time).
distance=float(input("Enter the Distance : "))
time=float(input("Enter the time in minutes : "))

#b) Calculate the average speed in kilometer per minutes, print the output.
average_speed=distance/time
print("Average speed in kilometer per minutes : ",average_speed)

#c) Calculate the time in seconds.
seconds=time*60
print("Time In Seconds : ",seconds)

#d) Calculate the average speed in kilometer per seconds, print the output.
kmperseconds=average_speed/60
print("Average speed in kilometer per seconds : ",kmperseconds)

#e) Write a function converts from kilometer to miles.
#(Hint: there are 1.61 kilometers in a mile).

def kilometersToMiles(distance):
    return distance/1.61
print("Kilometers to Miles : ",kilometersToMiles(distance))

#f) Calculate the average speed in miles per minute? print the output.
avgspeedInMiles=kilometersToMiles(distance)/time
print("Average Speed In Miles Per Minutes : ",avgspeedInMiles)