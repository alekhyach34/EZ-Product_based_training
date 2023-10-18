'''5)input: A string of comma seperated numbers are given such that the
numbers 4 and 7 are already available in the list.
Assumption:7 always comes after 4 in the given string
Number1=Add all numbers which do not lie between 4 and 7
(excluding 4 and 7)in the given input.
Number2=numbers formed by concatenating all numbers from 4 to 7
(including 4 and 7)
O/p:sum of Number1 and Number2
Example:2,5,1,4,3,2,7,8
Number1:2+5+1+8=16
Number2:'4'+'3'+'2'+'7'='4327'
o/p:16+4327=4343'''

def demo(s):
    los=s.split(',')
    idxpof=los.index('4')
    idxpos=los.index('7')
    n1,n2=0,''
    for i in los[:idxpof]+los[idxpos+1:]:
        n1+=int(i)
    for i in  los[idxpof:idxpos+1]:
        n2+=i
    return (n1+int(n2))
s=input()
if __name__=='__main__':
    print(demo(s))
