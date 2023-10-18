s="madammadam"
n=len(s)
arr=[[0 for i in range(n)] for j in range(n)]
count=0
i,j=0,0
while j < n:
  jflag=j
  while jflag < n:
    if i==jflag:
      arr[i][jflag]=1
      count+=1
    elif abs(i-jflag)==1:
      if s[i]==[jflag]:
        arr[i][jflag]=1
        count+=1
      else:
        arr[i][jflag]=0
    else:
      if s[i]==s[jflag]:
        if arr[i+1][jflag-1]==1:
          arr[i][jflag]=1
          count+=1
        else:
          arr[i][jflag]=0          
      else:
        i+=1
        jflag+=1
  j+=1
  i=0 
print(count)
