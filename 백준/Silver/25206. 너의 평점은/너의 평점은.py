sum=0
grs=0.0
for i in range (20):
    sub,num,grade=input().split()
    grade=str(grade)
    if(grade=='A+'):
        result=4.5
    elif(grade=='A0'):
        result=4.0
    elif(grade=='B+'):
        result=3.5
    elif(grade=='B0'):
        result=3.0
    elif(grade=='C+'):
        result=2.5
    elif(grade=='C0'):
        result=2.0
    elif(grade=='D+'):
        result=1.5
    elif(grade=='D0'):
        result=1.0
    elif(grade=='F'):
        result=0.0
    else:
        result=0.0
    sum=sum+(result* float(num))
    if(grade=='P'):
        continue
    else:
        grs=grs+float(num)
print(sum/grs)