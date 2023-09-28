'''create a dynamic 1d array it should contain number between 1 to 50.
1. extract and print even nos
2. power values'''
print("Enter array size:")
a=int(input())
print("Enter range:")
b=list(map(int,input().split(" ")))
k=[]
s=[]
e=[]
print("Enter array elements:")
for i in range(a):
    d=int(input())
    if(d>=b[0] and d<=b[1]):
        k.append(d)
    else:
        continue
for i in k:
    if i%2==0:
        s.append(i)
for i in k:
    for j in range(0,max(s)):
        if(2**j==i):
            e.append(i)
print("Even numbers are:")
print(s)
print("2 powers are:")
print(e)
