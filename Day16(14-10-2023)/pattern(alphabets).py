'''Pattern-4
a
b c
d e f '''

def alpha(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()
alpha(5)

print()

def alpha(n):
    for i in range(1,n+1):
        for j in range(i):
            print("1",end=" ")
        print()
alpha(5)

print()

def alpha(n):
    char='a'
    for i in range(1,n+1):
        for j in range(i):
            print(char,end=" ")
        print()
alpha(5)

print()

def alpha(n):
    char='a'
    for i in range(1,n+1):
        for j in range(i):
            print(char,end=" ")
            char=chr(ord(char)+1)
            if char>'z':
                char='a'
        print()
alpha(10)

print()


