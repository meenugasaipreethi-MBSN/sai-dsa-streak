# Deletion at beginning
def del_start(arr):
    print("Initial array")
    for i in range(len(arr)):
        print(arr[i])
    del arr[0]
    print("array after deletion")
    
    for i in range(len(arr)):
        print(arr[i])
arr = [1, 10, 20, 30, 40]
del_start(arr)