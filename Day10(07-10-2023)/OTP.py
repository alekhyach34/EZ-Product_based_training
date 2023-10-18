'''1) input:7564168
Example: seperate odd place integers : 5 4 6
you have to return a 4 digit OTP by squaring the digits.
digits from above ex : 5 4 6
squares: 25,16,36
so OTP to be returned is first four digits:2516'''

n=input()
o=''
for i in range(1,len(n),2):
    o+=str(int(n[i])**2)
print(o[:4])
    
