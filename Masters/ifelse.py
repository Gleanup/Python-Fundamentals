print("sample if else");
x=y=0
for i in input():
  if(i=='0'):
    x+=1;
  else:
    y+=1;
print("YES" if x==1 or y==1 else "NO",end="")
