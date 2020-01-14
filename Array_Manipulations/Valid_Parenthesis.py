import math

def IsValid(arr):
    # Create dict for closing brackets
    closing_dict = {")":"(","]":"[","}":"{"}
    stack =[]
    for i in range(len(arr)):
        if arr[i] in closing_dict:
            p = stack.pop()
            if p!= closing_dict[arr[i]]:
                return False
        else:
            stack.append(arr[i])
    return True

print(IsValid(list('([()])')))