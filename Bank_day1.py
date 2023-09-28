def balance(amount):
    for i in range(12):
        if(i==4):
            x=amount*(4/100)
            #print(x)
        if(i==9):
            amount=amount-25000
            y=amount*(4/100)
            #print(y)
        if(i>9):
            amount=amount+10000
            z=amount*(4/100)
            #print(z)
            total=x+y+z
            print(amount+total)
amount=int(input())
b=balance(amount)
b
#totl-m4*4/12*i
#i is principle amount
