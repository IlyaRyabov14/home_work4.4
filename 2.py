import random

mas=[random.randint(-50, 50) for i in range(random.randint(10,20))]

print(*mas)

maxi=int(input("MAX= "))

mini=int(input("MIN= "))

masi=[]

if maxi>=mini:

   for i in range(len(mas)):

      if maxi>=mas[i] and mini<=mas[i]:

          masi.append(i)

   print("Кол-во:",len(masi))

   print("Индексы:",masi)
   