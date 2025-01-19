def Merge_sort(arr:list[int]=None) -> list[int]:
    if arr is None:
        return "I need a list you dimwit"
    elif None in arr:
        return "I need a PROPER list witn NO NULL ELEMENTS YOU DUMB N-"
    if len(arr) <= 1:
        return arr
    M = len(arr) // 2
    lside = Merge_sort(arr[:M])
    rside = Merge_sort(arr[M:])

    return Merge(lside, rside)

def Merge(L_arr:list[int], R_arr:list ) -> list[int]:
    left_pointer = 0
    right_pointer = 0
    merged = []
    while len(L_arr) > left_pointer and len(R_arr) > right_pointer:
        if L_arr[left_pointer] < R_arr[right_pointer]:
            merged.append(L_arr[left_pointer])
            left_pointer += 1
        else:
            merged.append(R_arr[right_pointer])
            right_pointer += 1

    while len(L_arr) > left_pointer:
        merged.append(L_arr[left_pointer])
        left_pointer += 1

    while len(R_arr) > right_pointer:
        merged.append(R_arr[right_pointer])
        right_pointer += 1
        
    return merged