def insert_position(arr, element, position):
    print("initial array")
    
    for i in range(len(arr)):
        print(arr[i])
    arr.insert(position-1, element)
    print("Inserting element at given position")
    
    for i in range(len(arr)):
        print(arr[i])

arr = [10, 20, 30, 40, 50]
element = 41
pos = 5
    
insert_position(arr, element, position)