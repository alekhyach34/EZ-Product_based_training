#Binary Search
def binarySearch(arr,x,low,high):
    while low<=high:
        mid=(low+high)//2
        if x==arr[mid]:
            return mid
        elif x>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=list(map(int,input().split(",")))
x=int(input())
res=binarySearch(arr,x,0,len(arr)-1)
if res!=-1:
    print("Element found at:",res)
else:
    print("Element not found")

