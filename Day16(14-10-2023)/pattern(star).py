'''Python program to print the pattern
   *
  ***
 *****
******* '''

'''n = 4
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()'''


'''pattern-2'''
def pyramid(n):
    row=n
    col=2*n-1
    start , end=n-1,n-1
    for i in range(row):
        for j in range(col):
            if j>=start and j<=end:
                print("*",end="")
            else:
                print(" ",end="")
        print()
        start-=1
        end+=1
pyramid(5)
