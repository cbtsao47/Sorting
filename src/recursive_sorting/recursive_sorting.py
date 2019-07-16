# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    # loop until arrA and arrB are empty
    while len(arrA)>0 or len(arrB)>0:
        # if arrA or arrB is empty, extend the other arr
        if len(arrA)==0:
            merged_arr.extend(arrB)
            arrB=[]
        if len(arrB)==0:
            merged_arr.extend(arrA)
            arrA=[]
        # compare the first index of both arrA and arrB
        if len(arrA)>0 and len(arrB)>0:
            # append the smaller element into merged_arr
            if arrA[0] > arrB[0]:
                merged_arr.append(arrB[0])            
            # pop it off from whence it came from
                arrB.pop(0)
            else:
                merged_arr.append(arrA[0])
                arrA.pop(0)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if arr length is 1 return it
    if len(arr)<=1:
        return arr
    # find the split point
    split_point=len(arr)//2 #//takes away floating points
    # create left and right arr up to the split point
    arrA=arr[0:split_point]
    arrB=arr[split_point:]
    # merge sort both sides
    left=merge_sort(arrA)
    right=merge_sort(arrB)
    # merge left and right
    result =merge(left,right)
    return result


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
