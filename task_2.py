


# Task 1 დაბეჭდეთ 1-და 10-მდე რიცხვების ჯამი.
# sum = 0
# for num in range(1,10):
#     sum = sum + num
# print(f"sum is : {sum}")

# Tassk2 შეამოწმეთ შეყვანილი რიცხვი ლუწია თუ კენტი
# number = int(input("write the number"))
# if number % 2 == 0:
#     print("it is even number")
# else:
#     print("this is odd")

# Task3 გამოიანგარიშეთ შეყვანილი რიცხვის ფაქტორიალი (ფაქტორიალი - 1-დან N-მდე რიცხვების ნამრავლი

# number = int(input("write the number"))
# f = 1
# for i in range(1, number):
#     f = f * i
#     print(f"factorial is :{f}")


# # Task4 დაბეჭდეთ 3-ის პირველი 5 ჯერადი.
# num = 3
# result = 0
#
# for i in range(1, 6):
#     result = num * i
#     print(result)



# Task 5გამოიანგარიშეთ სამი რიცხვის საშუალო
# average_num1 = int(input("write number"))
# average_num2 = int(input("write number"))
# average_num3= int(input("write number"))
# result = (average_num1 + average_num2 + average_num3) / 3
# print(f"result is : {result}")

# Task 6 დააბეჭდეთ შემდეგი პატერნი:
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1, 6):
#     print(str(i) * i)



#  Task 7 დაბეჭდეთ შეყვანილი რიცხვის ციფრების ჯამი
# პირობა კარგად ვერ გავიგე
# num1 = int(input("write the number"))
# num2 = int(input("write the number"))
# result = num1 + num2
# print(f"result is {result}")



# Task 8დაბეჭდეთ სამი შეყვანილი რიცხვიდან მაქსიმალურის მნიშვნელობა
# maxNumber = float('-inf')
#
# for i in range(3):
#     num = int(input("Enter a number: "))
#     if num > maxNumber:
#         maxNumber = num
#
# print(f"The maximum number is: {maxNumber}")


# Task 9დაითვალეთ ხმოვანთა რაოდენობა შეყვანილ სტრიქონში.
# word = input("write the word")
# vowel = ["a", "e", "i", "o", "u"]
# vowel_sum = 0
# for string in range(len(word)):
#     for v in range (len(vowel)):
#         if word[string] == vowel[v]:
#             vowel_sum += 1
# print(f"the number of vowel is: {vowel_sum}")


# Task 10 დაბეჭდეთ საერთო ელემენტები ორ სიას შორის.

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# s = []
# for el in list1:
#     if el in list2:
#         s.append(el)
# print(f"this is the common numbers: {s}")



# Task 11 შექმენით შემთხვევითი რიცხვი 1-დან 10-მდე და  შეამოწმეთ დაემთხვევა თუ არა
# მომხმარებლის შეტანილ რიცხვს, გამოიყენეთ random ბილბლიოთეკა

from random import randint

random_number = randint(1, 10)
random_num_str = str(random_number)
user_num = int(input("Write the number: "))

found = False
for r in random_num_str:
    if int(r) == user_num:
        found = True
        break

    if found:
        print(f"this is random number{random_num_str}")
        print(f"this is the same number{user_num}")
    else:
        print(f"no match")






