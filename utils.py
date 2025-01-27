import random as R

def RLG(len:int, l_bound:int, u_bound:int):

    A = []
    for x in range(len):
        integer = R.randint(l_bound, u_bound)
        A.append(integer)
    return A

def validate_input_type_int(inp):
    try:
        int(inp)
        return True   
    except:
        print("Invalid input, try again\n")
        return False

def validate_positive(inp):
    if validate_input_type_int(inp):
        if int(inp) > 0:
            return True
        else:
            print("Number must be greater than 0\n")
            return False
    else:
        return False

def validate_bound(low_b, upp_b):
    if validate_input_type_int(low_b) and validate_input_type_int(upp_b):
        if int(low_b) < int(upp_b):
            return True
        else:
            print("Range must be larger than 0\n")
            return False
    else:
        return False

def validate_choice(inp_set:list[str], inp):
    for state in range(len(inp_set)):
        if inp_set[state].upper() == inp.upper():
            return True
    print("Invalid input, try again\n")
    return False
    
def Y_or_N_choice(inp):
    for state in range(len(inp_set)):
        if inp_set[state][0].upper() == "Y":
            return True
        else:
            return False
