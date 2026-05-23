
#  deletion of first occurence of an element

def first_occurrence(arr, element):
    print("Initial array")
    
    for i in range(len(arr)):
        print(arr[i])
    if element in arr:
        arr.remove(element)
    print("Final result")
    
    for i in range(len(arr)):
        print(arr[i])
arr = [10, 20, 30, 40, 40, 50, 10]
element = 10
first_occurrence(arr, element)
    