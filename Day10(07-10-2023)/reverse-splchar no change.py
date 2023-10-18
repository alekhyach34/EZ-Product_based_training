'''4) Reverse the given string and kepping its special character
at the same place.
Example:
    input:srin#ivas
    Output:savi#nirs
    input:we@lcome
    output:em@0clew
    input:pyth#on
    output:noht#yp'''

def demo(s):
    l=[]
    for i in s:
        if i.isalpha():
            l.append(i)
        else:
            spc=i
            idxspc=s.index(i)
    
    l.reverse()
    l.insert(idxspc,spc)
    return ''.join(l)
s=input()
print(demo(s))
