n=input()
c=0
while len(n)>1:
    n=str(sum(map(int,n)))
    c+=1
print(c)
