# Find maximum element in an array

# arr =[10,20,41,63,100]

def find_max(arr):
    
    if not arr:
        return none
    
    maximum = arr[0]
    
    for num in range(len(arr)):
        if arr[num] > maximum:
            maximum = arr[num]
    return maximum

arr = [10,20,41,63,100]
print(find_max(arr))