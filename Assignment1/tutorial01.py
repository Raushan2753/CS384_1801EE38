# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	multiplication = num1 * num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	if num2==0:
		print("The result is infinite as the number is divided by zero")
		return
	else:
		division = num1/num2
		return division
		
# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	power_num = 1
	if ((isinstance(num1, (float,int))==False) or (isinstance(num2,int)==False)):
		return 0
	if (num1==0 and num2==0):
		power_num = 0
	elif (num1!=0 and num2==0):
		power_num=1
	elif (num1==0 and num2!=0):
		power_num = 0
	elif (num2<0):
		# making number 2 positive by multipliying it with -1
		num2 = num2 * (-1)
		for i in range(0,num2):
			power_num *= (1/num1)
		# Rounding power to 3 decimal places
		power_num = round(power,3)
	else:
		for i in range(0,num2):
			power_num *= num1
	return power_num
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
	gp = []
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[]
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp = []
	return hp
