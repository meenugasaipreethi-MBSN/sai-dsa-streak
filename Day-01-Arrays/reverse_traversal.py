#  Reverse traversal
def rev_traversal(arr):
    for i in range((len(arr)-1), -1, -1):
        print(arr[i])
arr = [10, 20, 30]
rev_traversal(arr)


# using while loop

def rev_traversal(arr):
    i = len(arr)-1
    while i >= 0:
        print(arr[i])
        i -= 1
arr = [10, 20, 30]
rev_traversal(arr)
        
        
        
    

 