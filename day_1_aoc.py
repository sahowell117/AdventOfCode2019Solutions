import math
# load the numbers
with open("numbers.txt") as inf:
    numbers = inf.readlines()
numbers = [x.strip() for x in numbers]
y = 0 
need_moar_fuel = 1
while (need_moar_fuel != 0):
	need_moar_fuel = 0
	temp = 0
	for i, x in enumerate(numbers):
		temp = math.floor((float(x)/3))
		if temp > 2:
			temp = temp -2
			need_moar_fuel +=1			
			y += temp 
			numbers[i] = temp
		else:
			numbers[i] = 0
			

# write to a file
with open("Output.txt", "w") as outf:
	for  x in numbers:
		outf.write(str(x)+"\n")
	outf.write(str(y))