#use for loop and while loop and find sumofdigits
num=int(input())
s=0
'''while(num>0):
    r=num%10
    s=s+r
    num//=10
print(s)'''
for i in range(num):
    i=num%10
    s=s+i
    num//=10
print(s)
