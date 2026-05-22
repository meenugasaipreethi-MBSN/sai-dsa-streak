# Traversal 
def traversal(arr):
    for num in arr:
        print(num)
arr=[10, 20, 30, 40, 50]
traversal(arr)

# using while loop
def traversal(arr):
    n = len(arr)
    i = 0
    print("Traversal using while loop")
    while i < n:
        print(arr[i])
        i += 1
    arr = [10, 20, 30, 40, 50]
    traversal(arr)

# traversal using for each loop

def traversal(arr):
    for value in arr:
        print(value)
arr = [10, 20, 30, 40, 50]
traversal(arr)

