#program menentukan nilai terbesar

#input bilangan 1,2,3

num1 = int(input('masukan bilangan ke-1='))
num2 = int(input('masukan bilangan ke-2='))
num3 = int(input('masukan bilangan ke-3='))

#proses dan output

if num1 > num2 and num1 > num3:
    print('bilangan terbesar adalah =',num2)
elif num2 > num1 and num2 > num3:
    print ('bilangan terbesar adalah =',num2)
else :
    print('bilangan terbesar adalah =',num3)
          
