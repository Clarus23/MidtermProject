# Program make a simple calculator

#계산 log를 남기기 위해
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] %(message)s')

file_handler = logging.FileHandler('./logs/output.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y

#Need to define divide function.
def divide (x,y):
    return x/y

print("Calculator started.")

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            logger.info(str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            logger.info(str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2)))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            logger.info(str(num1) + " * " + str(num2) + " = " + str(multiply(num1, num2)))
            
        elif choice =='4':
            print(num1, "/", num2, "=", divide(num1,num2))
            logger.info(str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2)))
            

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")



#commit test