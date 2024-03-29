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
	if ((isinstance(a, (int,float))==False) or (isinstance(r, (int,float))==False) or (isinstance(n, int)==False)):
		return 0
	curr_element = a
	gp = []
	if (r==0 or n<=0):
		gp.append(0)
		return gp
	gp.append(a)
	for i in range(1,n):
		curr_element *= r
		curr_element = round(curr_element,3)
		gp.append(curr_element)
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	if ((isinstance(a, (int,float))==False) or (isinstance(d, (int,float))==False) or (isinstance(n, int)==False)):
		return 0
	ap=[]
	if (n<=0):
		ap.append(0)
		return ap
	curr_element = a
	ap.append(a)
	for i in range(1,n):
		curr_element += d
		curr_element = round(curr_element,3)
		ap.append(curr_element)
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	if ((isinstance(a, (int,float))==False) or (isinstance(d, (int,float))==False) or (isinstance(n, int)==False)):
		return 0
	hp=[]
	error_case = 0
	if (n<=0):
		return 0
	# if there is error case then i am returning 0
	if (d != 0 and (a*d)<=0 ):
		error_case = a * (-1/d)
		if (a%d==0):
			if(error_case <=n-1 or a==0):
				return 0
	# If no error is detected then return HP
	ap_element = a
	curr_element = round(1/ap_element, 3)
	hp.append(curr_element)
	for i in range(1,n):
		ap_element += d
		curr_element = round( 1/ap_element, 3)
		hp.append(curr_element)
	return hp
