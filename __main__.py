import utils as U
import merge_sort as M

running = True
print("~"*50)
print("Welcome to the Merge Sort Program!")
while running:
    size = input("Please enter number size:")

    # Size + check input type and 
    while not U.validate_positive(size):
        print("")
        size = input("Please enter number size:")
    size = int(size)
    print("")
    
    lower_bound = input("Enter the lower bound of the list:")
    upper_bound = input("Enter the upper bound of the list:")
    while not U.validate_bound(lower_bound, upper_bound):
        print("")
        lower_bound = input("Enter the lower bound of the list:")
        upper_bound = input("Enter the lower bound of the list:")
    lower_bound = int(lower_bound)
    upper_bound = int(upper_bound)
    print("")

    arr = U.RLG(size, lower_bound, upper_bound)
    print(f"Unsorted list: {arr}")
    print("")
    arr = M.Merge_sort(arr)
    print(f"Sorted list: {arr}")
    print("")
    again = input("Do you want to sort another list?")
    while not U.validate_choice(again):
        print("")
        again = input("Do you want to sort another list?")

    if U.choice_to_bool(again) == False:
        print("Goodbye!")
        running = False
    else:
        print("")
    print("~"*50)
    print("")    
