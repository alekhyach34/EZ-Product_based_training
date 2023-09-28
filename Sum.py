s=0
def a(n):
    if n<=0:
        return 0
    else:
        return n+a(n-1)
n=int(input())
print(a(n))
