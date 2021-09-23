# Author: CMOB 9/23/2021

free = input("how many free throws were scored? ")
basket = input("how many 2 pointers were scored? ")
three = input("how many 3 pointers were scored? ")

free = float(free)
basket = float(basket)
three = float(three)

points = str((three * 3) + (basket * 2) + free)

print("the player scored" + " " + points + " " + "points in the game")
