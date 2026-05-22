def insert_end(arr, element):
    print("Initial array")
    
    for i in range(len(arr)):
        print(arr[i])
    arr.append(element)
    print("Inserting element at end")
    
    for i in range(len(arr)):
        print(arr[i])
arr = [10, 20, 30, 40]
element = 50
insert_end(arr, element)