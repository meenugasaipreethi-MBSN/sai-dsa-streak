def insert_start(arr, element):
    print("Initial")
    
    for i in range(len(arr)):
        print(arr[i])
    arr.insert(0, element)
    print("Inserting element at beginning")
    
    for i in range(len(arr)):
        print(arr[i])
arr = [10, 20, 30, 40]
element = 1
insert_start(arr, element)