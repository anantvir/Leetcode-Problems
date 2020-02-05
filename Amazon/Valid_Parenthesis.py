import math

def IsValid(arr):
    # Create dict for closing brackets
    closing_dict = {")":"(","]":"[","}":"{"}
    stack =[]
    for i in range(len(arr)):
        if arr[i] in closing_dict:  # check if its a closing bracket
            p = stack.pop()
            if p!= closing_dict[arr[i]]:  # if closing bracket then compare top element of stack with opening bracket from closing_dict  
                return False
        else:
            stack.append(arr[i])        # push opening brackets onto stack
    return True

print(IsValid(list('([()])')))