def Merge_sort(arr:list[int]=None) -> list[int]:
    if arr is None:
        return "I need a list"
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

def Bubble_sort(arr:list[int]=None) -> list[int]:
    swapped = False
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def Insertion_sort(arr:list[int]=None) -> list[int]:
    for i in range(1,len(arr)):
        curr = arr[i]
        pos = i-1
        while pos >= 0 and curr < arr[pos]:
            arr[pos+1] = arr[pos]
            pos -= 1
        arr[pos+1] = curr
    return arr
 
        
        
