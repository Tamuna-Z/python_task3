# 1. დაწერეთ ფუნქცია სახელად greet, რომელიც იღებს სახელს პარამეტრად და ბეჭდავს მისალოც შეტყობინებას.
def greeting(name):
    print(f"Welcome {name}")
greeting("tamuna")
# 2. შექმენით ლამბდა ფუნქცია რიცხვის კვადრატის გამოსათვლელად. გამოიძახეთ ლამბდა ფუნქცია 4 მნიშვნელობით.
square = lambda a:a ** 2
print(square(4))
# 3. დაწერეთ ფუნქცია calculate_discount, რომელიც ითვლის ფასდაკლებას მოცემულ ფასზე ფასდაკლების
# განაკვეთის საფუძველზე.
def calculate_discount(price,discount):
    result = price - price * discount
    return result
lastResult =calculate_discount(100, 0.1)
print(lastResult)

# 4. დაწერეთ ფუნქცია, სახელად split_name, რომელიც პარამეტრად იღებს სრულ სახელს და აბრუნებს ელემენტს,
# რომელიც შეიცავს სახელსა და გვარს ცალკეულ ელემენტებად.

def split_name(fullname):
     name ,surname = fullname.split(" ")
     return name, surname
result4 = split_name("tamuna zurabashvili")
print(result4)

# 5.  შექმენით ფუნქცია სახელად greet_user, რომელიც პარამეტრებად იღებს სახელს და მისალმების შეტყობინებას.
# მიეცით ნაგულისხმევი
# მნიშვნელობა "Hello" მისალოცი შეტყობინებისთვის.
def greet_user(name,greet="Hello"):
    return f"{greet} {name}"
print(greet_user("tamuna"))

# დაწერეთ პროგრამა, რომელიც იყენებს ფუნქციას მართკუთხედის ფართობის გამოსათვლელად.
# ფუნქციამ უნდა მიიღოს სიგრძე და სიგანე პარამეტრებად და დააბრუნოს ფართობი.
# ფუნქციის გამოძახება სიგრძე=5 და სიგანე=8.

def function(length,width):
    area=length * width
    return area
print(function(34,56))

# შექმენით ფუნქცია სახელწოდებით print_square,
# რომელიც იღებს რიცხვს პარამეტრად და ბეჭდავს მის კვადრატს.
# გამოიყენეთ ეს ფუნქცია ლუპში 1-დან 5-მდე რიცხვების კვადრატების დასაბეჭდად.

def print_square(num):
    result7 = num ** 2
    return result7
for i in range(1,6):
    print(print_square(i))

#     """
# შეიმუშავეთ ფუნქცია სახელწოდებით calculate_average,
# რომელიც პარამეტრად იღებს რიცხვების ჩამონათვალს და აბრუნებს საშუალოს.
# დაამატეთ docstring ფუნქციის მიზნის ასახსნელად.
#
# """
#
#
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


nums_list = [1, 2, 3, 4, 5]
result = calculate_average(nums_list)
print(result)

