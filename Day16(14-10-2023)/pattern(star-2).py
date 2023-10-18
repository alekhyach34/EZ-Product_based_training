'''Pattern4
   *
  * *
 * * * '''

size = 4
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print("*", end=' ')
    print()

def star_pattern4(n):
    spaces = n
    for i in range(1, n + 1):
        for j in range(1, spaces + 1):
            print(" ", end="")
        for k in range(1, i + 1):
            print("* ", end="")
        print()
        spaces = spaces - 1
n = int(input("Enter number of rows:"))
star_pattern4(n)
