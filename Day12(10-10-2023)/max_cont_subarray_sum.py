#Print the sum of maximum sub array
'''a=list(map(int,input().split(",")))
a1=-999999
b=0
for i in range(len(a)):
    b=b+a[i]
    if(a1<b):
        a1=b
    if(b<0):
        b=0
print(a1)'''

#Kadanes algorithm
def kadanes(arr):
    _sum=float("-inf")
    cs=arr[0]
    n=len(arr)
    for i in range(1,n):
        if cs<0:
            cs=0
        if arr[i]<0:
            _sum=max(_sum,cs+arr[i])
        cs=cs+arr[i]
    return max(_sum,cs)
print(kadanes([-1,-2,3,-4,-6,18,65,110]))
   
