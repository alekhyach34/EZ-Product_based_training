def findGCD(nums):
    min_ele=min(nums)
    res=min_ele
    max_ele=max(nums)
    while res>0:
        if min_ele%res==0 and max_ele%res==0:
            break
        res-=1
    return res
nums=list(map(int,input().split()))
print(findGCD(nums))