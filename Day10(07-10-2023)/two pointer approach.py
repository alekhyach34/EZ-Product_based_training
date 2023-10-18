'''#Two pointer Approach(2 pointers in one loop)
problem:#1(Two sum problem)
arr[]={2,3,5,7,10,12,15,20},target=19
Answer:4,6
Explanation:return i and jth pointer positions whose sum of indexed
values equals to target.'''

def two_pointer_approach(t, l):
    l.sort()
    i = 0
    j = len(l) - 1

    while i < j:
        if l[i] + l[j] == t:
            return i, j
        elif l[i] + l[j] < t:
            i += 1
        else:
            j -= 1


l = list(map(int, input().split()))
t = int(input())

result = two_pointer_approach(t, l)
print(result)
