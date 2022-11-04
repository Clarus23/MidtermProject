def quit_process():
    # check if user wants another calculation
    # break the while loop if answer is no
    while(True):
        next_calculation = input("Let's do next calculation? (yes/no): ")          
        if next_calculation.lower() == "no":
            return True
        elif next_calculation.lower() == "yes":
            return False
        else: continue

def quit_doublecheck():
        while(True): 
            next_calculation = input("Are you sure? (yes/no): ")
            if next_calculation.lower() == "no":
                return False
            elif next_calculation.lower() == "yes":
                return True
            else: continue