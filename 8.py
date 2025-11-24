first=[0]
mas=[x for x in range(201)]
k=int(input())
if k>=0 and k<=10:
    print(mas[k-1])
if k>10 and k<=190:
    if k%2==0:
        print(mas[10+(k-10)//2-1]%10)
    else:
        print(mas[10+(k-10)//2-1]//10)
if k>190:
    if k%3==2:
        print(mas[10+(k-10)//2-1]//100)
    elif k%3==0:
        print(mas[10+(k-10)//2-1]//10%10)
    else:
        print(mas[10+(k-10)//2-1]%10)
    
    

