def move_zeroes(arr):
    j = 0
    
    for i in range(len(arr)):
        if arr[i] != 0 :
            arr[j] , arr[i] = arr[i] , arr[j]
            j += 1
    return arr

arr = [0,1,0,3,12]
print(move_zeroes(arr))      


