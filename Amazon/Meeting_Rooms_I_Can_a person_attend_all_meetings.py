"""Sort the input intervals acc to start time using lambda function in key argument of sorted function
or list.sort(key=lambda function)
then iterate over the list and check if end time of a meeting is after the start time of the next meeting"""


arr = [[5,10],[15,20],[0,3]]
new_arr = sorted(arr,key=lambda x: x[0])

def Meeting_Rooms(arr):
    for i in range(len(arr)-1):
        if arr[i][1] > arr[i+1][0]:
            return False
    return True

print(Meeting_Rooms(new_arr))
