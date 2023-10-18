'''2) Take the input from the user int the given
format(consist of name and code)
find the max digit from the code which is less or equal to the length
of string and put that place char in final string,if there is no any
digit found which not satisfy the condition that simply put 'X'.
#input:
Abhishek:43848,Mayur:3749,Friend:3949,Yeah:7878
#Output:kueX'''

'''n=input()
li=[]
fs=''
li=n.split(',')
for i in li:
    temp=i.split(':')
    name=temp[0]
    number=temp[1]
    l=len(name)
    max=0
    for digit in number:
        if(int(digit)<=l):
            if(max<int(digit)):
                max=int(digit)
    if max==0:
        fs+='X'
    else:
        fs+=name[max-1]
print(fs)'''


s=input()
los=s.split(',')
op=''
for i in los:
    nc=i.split(':')
    name=nc[0]
    code=nc[1]
    l=len(name)
    max=0
    for i in code:
        if int(i)>max and int(i)<=len(name):
            max=int(i)
    if max==0:
        op+='X'
    else:
        op+=name[max-1]
print(op)
