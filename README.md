#Task 1: Calculate Factorial Using a Function
                                            
def fact(num):                              
    factorial = 1                           
    while num > 1:                          
        factorial *= num                    
        num -= 1                            
    return factorial                        
n = int(input("enter the number:"))         
print(f"factorical of {n} is {fact(n)}")    


#Problem Statement: Write a Python program that:
#1.   Asks the user for a number as input.
#2.   Uses the math module to calculate the:
#o   Square root of the number
#o   Natural logarithm (log base e) of the number
#o   Sine of the number (in radians)


import math

num = float(input("enter the number:"))
output = math.sqrt(num)
print(f"square root : {output}")

def calculate_natural_log():
    try:
        # Take user input
        num_str = input("Enter the number: ").strip()

        # Try converting to float
        num = float(num_str)

        # Validate input (log is undefined for non-positive numbers)
        if num <= 0:
            print("Error: Natural logarithm is only defined for positive numbers.")
            return

        # Calculate natural log (base e)
        result = math.log(num)

        print(f"Natural logarithm (ln) of {num} is: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")


if __name__ == "__main__":
    calculate_natural_log()

radians =float(input("enter the radians:"))

radians = math.pi / 2
print(f"sine :{radians}")
    

