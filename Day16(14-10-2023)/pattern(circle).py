'''Pattern-3'''
def circle(n):
    row=n
    col=n
    for i in range(row):
        for j in range(col):
            if i==j or (i+j)==n-1:
                print(" ",end=" ")
            elif i==0 or i==n-1 or j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
circle(4)
