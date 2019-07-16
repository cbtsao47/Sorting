def add_list(list):
    if list==[]:
        return 0
    return list[0]+add_list(list[1:])

print(add_list([1,2,3,4])) #10
def partition(list):
    left=[]
    pivot=l[0]
    right=[]
    for value in list[1:]:
        if value<pivot:
            left.append(value)
        else:
            right.append(value)
    return left,pivot,right
def quicksort(list):
    # setup base case
    if list == []:
        return []
    left,pivot,right = partition(list)
    return quicksort(left)+[pivot]+quicksort(right)

def quicksort(list,low,high):
    if low >= high:
        return list
    pivot_index= low
    for i in range(low,high):
        list[i],list[pivot_index+1]=list[pivot_index+1],list[i]

