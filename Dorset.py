# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# message = 'Good Morning'
# print(len(message)) #affichier le nb de caractères de 0 à ...
# print(message[11]) #afficher un caractère en particulier
# print(message[0:4]) #afficher un groupe de caractère
# print(message[-2]) #-1 est le dernier caracxtère, ici g, -2 l'avant-dernier
# print(message[ :-1]) # du début jusqu'à la fin
# print(message.upper()) #met en majuscule
# print(message.lower()) #minuscule
# print(message.count('o')) #compte le nb de 'o'
# print(message.find('o')) #renvoie la première position du o, ici 1 car le caractere g est le caract. 0
# new_message = message.replace('Morning','Afternoon')
# print(new_message)
# a = 'cccccct'
# b = 'cccg'
# print(a<b) #ordre alphabétique



    # num = int(input("Enter an interger : "))
    # if num < 5:
    #     print("The number is less than 5.")
    # else:
    #     print("The number is greater than 5.")
    

# num = int(input("Enter the number : "))
# if num%2 ==0:
#     print("The number {} is an even number.".format(num))
# else:
#     print(f"The number {num} is an odd number.")
    

#if
#elif
#else

# grade = float(input("Enter your marks : "))
# if grade < 5:
#     print("Suspended.")
# elif grade >= 5 and grade < 7:
#     print("Approved.")
# elif grade >= 7 and grade < 9:
#     print("Notable.")
# else:
#     print("Excellent.")


# weight = float(input("Enter your weight in kilos : "))
# height = float(input("Enter your height in meters: "))
# bmi = weight/height**2
# if bmi < 18.5:
#     print(f"Underweight, bmi : {bmi}.")
# elif bmi >= 18.5 and bmi < 25:
#     print(f"Normal weight, bmi : {bmi}.")
# elif bmi >= 25 and bmi < 30:
#     print(f"Overweight, bmi : {bmi}.")
# else:
#     print(f"Obesity, bmi : {bmi}")


# temp = input("Enter a temperature in C or F : ")
# degree = int(temp[:-1])
# i_check = temp[-1]

# if i_check.upper() == "C":
#     result = int(round((9*degree)/5 +32))
#     o_check = "Fahrenheit"
# elif i_check.upper() == "F":
#     result = int(round((9*degree - 32)*5/9))
#     o_check = "Celsius"
# else:
#     print("Input proper convention.")
#     quit()
# print("The temperatuyre in ", o_check, " is ", result, " degrees.")


# distance = input("Enter a distance in cm or in m : ")
# dist = int(distance[:-1])
    

# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# if num1 % num2 == 0:
#     quotient = int(num1/num2)
#     print(f"{num1} can be divided by {num2} and the quotient is {quotient}")
# else:
#     remainder = num1%num2
#     quotient = num1//num2
#     print(f"{num1} cannot be divided by {num2} ; the quotient is {quotient} and the remainder is {remainder}")
    


# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# num3 = int(input("Enter the third number : "))
# minimum = min(num1, num2, num3)
# print(f"The minimum is {minimum}")

# unit = int(input("Enter the number of units : "))
# price = 0
# if unit < 100:
#     print("There is no charge.")
# elif unit >= 100 and unit < 200:
#     price = 5*(unit-100)
#     print(f"The total bill amount is Rs{price}")
# else:
#     price = 10*(unit-200) + 5*100
#     print(f"The total bill amount is Rs{price}")
    

# num = int(input("Enter ab integer value : "))
# while num>0:
#     res = num//3
#     print("The integer division of {} by 3 gives: {}. ".format(num,res))
#     num = int(input("Enter an integer value : "))
# print("We're done.")

# num = int(input("Enter an integer value : "))
# ndiv = 1
# while ndiv < num:
#     res = num//ndiv
#     print("The integer division of {} by {} gives : {}.".format(num, ndiv, res))
#     ndiv = ndiv + 1
    
# print("We're done.")
# print("Total number of divisions : {}.".format(ndiv))

# num=int(input("enter"))
# ndiv=0

# while num>0:
#     res=num//3
#     print("Divion of {} by 3 : {}".format(num,res))
#     ndiv=ndiv+1
#     print("Nb of divions so far : {}".format(ndiv))
#     num=int(input("enter"))
# print("Done")


# num = 0
# ndiv = 0
# while num <= 211:
#     if num % 3 ==0:
#         ndiv += 1
#         print("{} is divisible by 3.".format(num))
#     num += 1
# print("There are {} numbers divisible by 3 between 0 and 211.".format(ndiv))

# sum = 0
# for i in range(1,10):
#     sum += i 
# print(sum)


# sum = 0
# num = 1

# while num <= 10:
#     sum += num
#     num = num + 10

# print(sum)
    
# sum = 0
# nb = 0

# while nb < 10:
#     num = int(input("Enter a number : "))
#     nb += 1
#     sum += num
    
# average = sum/10
# print("The average is : {}".format(average))

# i = 1
# while i <= 4:
#     print("*"*i)
#     i += 1
    
# num = int(input("Enter a number : ")) #factorial
# fact = 1
# while num > 1:
#     fact *= num
#     num -= 1
# print("The result is {}.".format(fact))
# name = 'Jesaa29Roy'
# size = len(name)
# i = 0
# while i < size:
#     if name[i].isdecimal():
#         break;
#     print(name[i], end = ' ')
#     i += 1
# print("\nThe execution has stopped")

# name = 'Jesaa29Roy'
# size = len(name)
# i = -1
# while i < size - 1:
#     i += 1
#     if not name[i].isalpha():
#         continue
#     print(name[i], end = ' ')
# print("\nThe execution has stopped")

# n = int(input("Enter a number : "))
# fac = 1
# for i in range (1, n+1):
#     fac *= i
# print(fac)

# cities = ['Moscow', 'Paris', 'Dublin', 'London', 'New York', 'Singapore']
# cities.append('Roma')
# for city in cities:
#     print(city)
# print(cities[0])
# cities.remove('Roma')
# for city in cities:
#     print(city)
# while True:
#     try:
#         ent = input("Pres Enter to exit or Enter  a number: ")
#         if ent == "":
#              break    
#         num = int(ent)
#         if (num%2)==0:
#             print(f"{num} is Even")
#         else:
#             print(f"{num} is Odd")
#         #break
#     except:
#         print("Please enter an int.")
def est_premier(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

while True:
    try:
        ent = input("Appuyez sur Enter pour quitter ou entrez un nombre : ")
        if ent == "":
            break
        num = int(ent)
        if est_premier(num):
            print(f"{num} est un nombre premier.")
        else:
            print(f"{num} n'est pas un nombre premier.")
    except ValueError:
        print("Veuillez entrer un entier valide.")
