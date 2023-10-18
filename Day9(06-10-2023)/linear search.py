#Linear Search
def linearSearch(arr,x):
    flag=0
    for i in range(len(arr)):
        if x==arr[i]:
            flag=1
            return i
    if flag==0:
        return -1
    else:
        return 1
arr=list(map(int,input().split(",")))
x=int(input())
res=linearSearch(arr,x)
if res==-1:
    print("Element not found")
else:
    print("Element found at position:",res)


