import utils as U
import sorting_algorithm as M
import time as T

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

    sort_choice = input("""What sorting algorithm do you want:
M - Merge
I - Insertion
B - Bubble
""")
    while not U.validate_choice(["M","I","B"],sort_choice):
            sort_choice = input("""What sorting algorithm do you want:
M - Merge
I - Insertion
B - Bubble
""")

    arr = U.RLG(size, lower_bound, upper_bound)
    print(f"Unsorted list: {arr}")
    print("")
    timer = T.time()
    if sort_choice == "M":
        arr = M.Merge_sort(arr)
    elif sort_choice == "I":
        arr = M.Insertion_sort(arr)
    else:
        arr = M.Bubble_sort(arr)
    timer = T.time() - timer
    print(f"Sorted list: {arr}")
    print("")

    print(f"Time taken: {timer}")
    again = input("Do you want to sort another list?")
    while not U.validate_choice(["Yes", "No", "Y", "N"],again):
        print("")
        again = input("Do you want to sort another list?")

    if U.Y_or_N_choice(again) == False:
        print("Goodbye!")
        running = False
    else:
        print("")
    print("~"*50)
    print("")    
