#Python program to check whether a pair exist or not.
#Using two pointer
def two_pointer(arr,target):
    arr.sort()
    i,j=0,len(arr)-1
    while i<j:
        if arr[i]+arr[j]==target:
            return True
        if arr[i]+arr[j]<target:
            i+=1
        if arr[i]+arr[j]>target:
            j-=1
    return False
arr=list(map(int,input().split(",")))
target=int(input())
print(two_pointer(arr,target))
                
