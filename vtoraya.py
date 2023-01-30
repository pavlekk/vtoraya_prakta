a = "123456789101112131415161718192021222324252627282930"
b = "12345678910111213141516171819202122232425262728293031"
c = "1234567891011121314151617181920212223242526272829"
d = "12345678910111213141516171819202122232425262728"

print ("Введите год")

god = int(input("Год "))

if (god % 4 == 0 or god % 400 == 0):
   
    print("Ваш год високосный")
    new_list = list(map(int, a))
    a4 = (sum(new_list))
    
    new_list.clear()
    new_list = list(map(int, b))
    b7 = (sum(new_list))
    
    new_list.clear()
    new_list = list(map(int, c))
    c1 = (sum(new_list))
    
    print ("Сумма = ",c1+(b7*7)+(a4*4))
    
else:
    print ("Ваш год не високосный")
    
    new_list = list(map(int, a))
    a4 = (sum(new_list))
    
    new_list.clear()
    new_list = list(map(int, b))
    b7 = (sum(new_list))
    
    new_list.clear()
    new_list = list(map(int, d))
    d1 = (sum(new_list))

    print ("Сумма = ", d1+(b7*7)+(a4*4) )
    
    
    
