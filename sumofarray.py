def sumof(arr):
    s=0
    for i in arr:
        s+=i
    print(s)
#arr=[1,2,3,4]
arr=list(map(int,input().split()))
a=sumof(arr)
a
space complexity--O(n)
