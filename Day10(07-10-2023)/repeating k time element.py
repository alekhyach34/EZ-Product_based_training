'''6) Problem statements:
You are given an array of N integers and another integer k. How many
numbers appear in the arrray at least k times?
Strandard input
The first line contains two integers N and k.
The second line contains N integers,representing the elements of the array
Standard output:
Print the answer on the first line
Example:
input:
3 1
1 1 1
output:
1

input:
5 2
1 2 3 2 1
output:
2'''

n,k=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(int(input()))
s,c=set(lst),0
for i in s:
    if lst.count(i)>=k:
        c+=1
print(c)
