# Brian Liu P1
# Dice Roll Game

import random

rollNumber = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

print("Welcome to the Dice Roll Game!")
playerChoice = int(input("How many times do you want to roll the die? "))

while True:
	rollNumber = rollNumber + 1 
	randomNum = random.randint(1,6)
	print("Roll number: " + str(rollNumber) + " Result: " + str(randomNum))
	if rollNumber == playerChoice:
		break
	elif randomNum == 1:
		ones = ones + 1
	elif randomNum == 2:
		twos = twos + 1
	elif randomNum == 3:
		threes = threes + 1
	elif randomNum == 4:
		fours = fours + 1
	elif randomNum == 5:
		fives = fives + 1
	elif randomNum == 6:
		sixes = sixes + 1

print("Results: ")
print("Ones: " + str(ones))
print("Twos: " + str(twos))
print("Threes: " + str(threes))
print("Fours: " + str(fours))
print("Fives: " + str(fives))
print("Sixes: " + str(sixes))

print("Percentages")
print("Ones: " + str(((float(ones) / float(rollNumber))*100)) + "%")
print("Twos: " + str(((float(twos) / float(rollNumber))*100)) + "%")
print("Threes: " + str(((float(threes) / float(rollNumber))*100)) + "%")
print("Fours: " + str(((float(fours) / float(rollNumber))*100)) + "%")
print("Fives: " + str(((float(fives) / float(rollNumber))*100)) + "%")
print("Sixes: " + str(((float(sixes) / float(rollNumber))*100)) + "%")