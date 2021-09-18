a =int(input(""));
if(a < 2):
    print("Khong phai so nguyent to");
elif(a == 2):
    print("so nguyen to");
else:
    tam=0;
    for i in range(2 , a, 2):
        if(a % i ==0):
            tam=1
            break;
    if(tam ==1):
        print(" Khong phai so nguyen to");
    else:
        print("La so nguyen to");
