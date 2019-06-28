# factors-of-no.py
i=int(input())
for s in range(1,i+1):
    if i%s==0:
        print(s,end=' ')
