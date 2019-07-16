def insertion(arr):
    # set up 2 regions
    # loop through the right region starting at arr[1] until the end of the arr
    for i in range(1,len(arr)):
        # grab the current value
        current_value=arr[i]
        # grab the position of the current index
        position=i
        # if the current value < the left neighboring value
        while(position>0 and current_value<arr[position-1]):
                # set current index to be the neighboring value
            arr[position]=arr[position-1]
                # position-=1
            position-=1
        arr[position]=current_value
        # set arr[1] to arr[0]
    # return the arr
    return arr

print(insertion([4,3,2,1,5]))