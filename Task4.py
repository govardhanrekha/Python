#Create a program to sum of three number from the user input,

# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

# Step 1 - I/O and O/P

# I/O -  int

# O/P - int

# Step 2 - Rough Logic

# return n1+n2+n3

def sum_of_three_numbers(n1=100, n2=200, n3=300):
    return n1 + n2 + n3 
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))   
n3 = int(input("Enter third number: "))    
print("Sum of three numbers is:", sum_of_three_numbers(n1,n2,n3))
print("Sum of three numbers is:", sum_of_three_numbers(n1,n2))
print("Sum of three numbers is:", sum_of_three_numbers(n1))