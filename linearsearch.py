def linear_search(k):
    for i in arr:
        if(i==k):
            print("key found")
arr=list(map(int,input().split()))
#arr=[8,7,5,3,9,2]
k=int(input())
l=linear_search(k)
l
space complexity--O(1)
