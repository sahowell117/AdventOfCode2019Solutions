import math
#this program loops thru a long list of comma delimited integers and performs some calculations
#load the numbers
def loadNumberList(fileName):
	with open(fileName) as inf:
		intcode = inf.read()
		intcode = intcode.split(",")
		for i, x in enumerate(intcode):
			intcode[i] = int(x)
	return intcode		
#1 means add the numbers indicated by position 2 & 3, and put the sum at position indicated by number 4. 2 means multiply. 99 means stop
def runIntcode(intcode):
	opcode = 0
	opcode_position = 0
	opcode = intcode[opcode_position]

	input_value_1 = 0
	input_value_2 = 0
	input_position_1 = 0
	input_position_2 = 0
	output_val = 0
	output_value = 0
	for i, x in enumerate(intcode):
		opcode = intcode[opcode_position]
		if opcode == 99:
			break
		input_position_1 = intcode[opcode_position+1]
		input_position_2 = intcode[opcode_position+2]
		output_position = intcode[opcode_position+3]
		input_value_1 = intcode[input_position_1]
		input_value_2 = intcode[input_position_2]
		if opcode == 1:
			output_val = input_value_1 + input_value_2
		if opcode == 2:	
			output_val = input_value_1 * input_value_2
		intcode[output_position] = output_val	
		opcode_position = opcode_position + 4
	return intcode[0]	
noun = 0
verb = 0
a = loadNumberList("numbers.txt")
for i in range (0,100):
	for k in range (0, 100):
		a[1] = i
		a[2] = k
		retval = runIntcode(a)
		if retval == 19690720:
			noun = i
			verb = k
			print("noun: " + str(i) + " verb: " + str(k))
		a = loadNumberList("numbers.txt")