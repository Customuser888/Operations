#import math - в варианте 19 не нужен

a = int(input('Введите a: '))
z1 = ((1+a+a**2)/(2*a+a**2)+2-(1-a+a**2)/(2*a-a**2))**-1*(5-2*a**2) #Если ввести 2, то будет ошибка из-за деления на 0
z2 = (4-a**2)/2

print (f'z1 = {z1}')
print (f'z2 = {z2}')