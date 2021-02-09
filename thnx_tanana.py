s=0
for i in input():
 s+=int(i)
a=str(2*s)
l=''
for b in a:
 if int(b)%2!=0:
  l+='@'
 else:
  l+=b
print(l+' thnx tanana')
