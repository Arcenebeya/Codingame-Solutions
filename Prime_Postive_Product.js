n=+readline();
q=0
for(i=2;i<=n;i++)
{
    if(n%i) continue;
    while(n%i==0)
    {
        q++
        n/=i;
    }
}

print(q==2)
