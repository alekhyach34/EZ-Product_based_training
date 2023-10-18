'''ceil value:
int arr[]={1, 2, 8, 10, 10, 12, 19}
ceil of 7(smallest element but which is greater than 7)in the above array:8

floor value:
int arr[]={1, 2, 8, 10, 10, 12, 19}
floor of 7(greatest element but which is smaller than 7)in the above array:7
'''

def binary_search_floor(arr,target):
    left,right=0,len(arr)-1
    floor=-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            floor=arr[mid]
            left=mid+1
        else:
            right=mid-1
    return floor
arr=list(map(int,input().split(',')))
target=int(input())
print(binary_search_floor(arr,target))
