# num = 11
#
# if num > 5:
#     if num > 8:
#         print("მოცემული რიცხვი მეტია 10-ზე")
#         if num < 10:
#             print("მოცემული რიცხვი არის 8-სა და 10-ს შორის")
#     else:
#         print("მოცემული რიცხვი მეტია 5-ზე მაგრამ ნაკლებია 10-ზე")
# else:
#     print("რიცხვი ნაკლებია 5-ზე")

# try:
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError as e:
#     print(f"you have zero division error: {e}")
# finally:
#     print("always runs")

# Task 1 შექმენით პროგრამა, რომელიც ბეჭდავს რიცხვების კვადრატებს 1-დან 5-მდე for loop-ის გამოყენებით.
# for i in range(1,5):
#     print(i ** 2)

# Task 2 დაწერეთ პროგრამა, რომელიც ითვლის 5-დან 1-მდე while loop-ის გამოყენებით.
# count = 5
# while count > 0:
#     print(count)
#     count -= 1

# Task 3 დაწერეთ პროგრამა რომელიც შეამოწმებს სიაში მონაცემი ლუწია თუ კენტი და დააბრუნებს მათ კვადრატს
# for num in range(1, 15):
#     if num % 2 == 0:
#         print(num ** 2)

# Task4 შექმენით პროგრამა, რომელიც განსაზღვრავს არის თუ არა რიცხვი დადებითი,
# უარყოფითი ან ნულოვანი და არის თუ არა ის ლუწი თუ კენტი.
# number = int(input("write the number"))
# print(number)
# if number > 0:
#     print("dadebiTia")
#     if number % 2 == 0:
#         print("number is even")
#     else:
#         print("number is odd")
# else:
#     print("uaryofitia")


# Task5 დაწერეთ პროგრამა, რომელიც იყენებს for loop-ს
# სიაში პირველი ლუწი რიცხვის საპოვნელად და დასაბეჭდად.

# for num in range(1, 9):
#     if num % 2 == 0:
#         print(num)
#         break

# Task6 შექმენით პროგრამა,
# რომელიც იყენებს for loop-ს ყველა კენტი რიცხვის
# დასაბეჭდად 1-დან 10-მდე, ლუწი რიცხვების გამოტოვებით.

# for num in range(1, 10):
#     if num % 2 == 1:
#         print(num)

# Task7 შექმენით პროგრამა, რომელიც იყენებს
# for loop-ს, რათა შეამოწმოს არის თუ არა
# მოცემული რიცხვი მარტივი.

# prime_num = int(input("enter your number: "))
#
# for i in range(2, prime_num):
#     if not prime_num % i == 0:
#         print("your number is prime")
#         break
#     else:
#         print("your number is not prime")



