import logging
from arithmetic_operation import *
from set_logger import set_logger
from quit import *

def start_print():
    print("Calculator started.")

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide") 

def run():
    logger = logging.getLogger("calculate")
    error_logger = logging.getLogger("error")
    set_logger(logger, error_logger)

    start_print()
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
                if(num2 != 0):
                    print(num1, "/", num2, "=", divide(num1,num2))
                    logger.info(str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2)))
                else:
                    print("[ERROR] divisor can't be 0")
                    error_logger.error("divisor can't be 0")

            if quit_process():
                if quit_doublecheck():
                    break
        else:
            print("Invalid Input")
            error_logger.warning(str(choice) + " is Invalid Input")