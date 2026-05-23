# Deletion at given position

def del_position(arr, pos):
    print("Initial Array")
    
    for i in range(len(arr)):
        print(arr[i])
    del arr[pos-1]
    print("Array after deletion")
    
    for i in range(len(arr)):
        print(arr[i])
arr=[10, 20, 30, 40, 50]
pos=5
del_position(arr, pos)