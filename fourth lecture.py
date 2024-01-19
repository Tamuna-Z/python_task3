"""
შექმენით ფუნქცია, რომელიც შეყვანის სახით იღებს რიცხვების სიას და აბრუნებს სიაში ყველა ლუწი რიცხვის ჯამს.
"""


# def sum_of_evens(numbers):
#     result = sum(i for i in numbers if i % 2 == 0)
#     return result
#
#
# print(sum_of_evens([2, 3, 4, 5, 6, 7, 8]))

"""
დაწერეთ ფუნქცია, რომელიც მიიღებს სტრიქონების თაფლს და აბრუნებს 
ახალ თაფლს თითოეული სტრიქონის სიგრძით.

"""
def tuple_length(string_tuples):
    result = tuple(len(i) for i in string_tuples)
    return result
print(tuple_length(("tam","levani","mate")))

"""
მოსწავლის სახელების დიქშენერით და მათი შესაბამისი ქულების გათვალისწინებით, 
შექმენით ფუნქცია, რომელიც აბრუნებს იმ სტუდენტების სახელებს, 
რომლებმაც მიაღწიეს გარკვეულ ზღვარს (მაგ., 80).

"""
# def student_name(student__name,limit):
#     students = []
#     for name, grade in student__name.items():
#         if grade > limit:
#             students.append(name)
#     return students
#
# my_dict = {"niak": 69, "giorgi": 81, "nino": 85}
#
# print(student_name(my_dict, 80))

"""
შექმენით ფუნქცია, რომელიც პარამეტრებად იღებს მთელი რიცხვების ორ კომპლექტს და აბრუნებს ახალ კომპლექტს,
რომელიც შეიცავს საერთო ელემენტებს.

"""

# def common_elems(set1: set, set2: set):
#     result = set1.intersection(set2)
#     return result
#
# set1 = {1,2,3,4,6,8}
# set2 = {7,8,1,10,11,12}
#
# print(common_elems(set1, set2))

"""
შექმენით ფუნქცია, რომელიც კითხულობს ტექსტურ ფაილს,
ითვლის თითოეული სიტყვის შემთხვევებს და წერს სიტყვების სიხშირეს ახალ ტექსტურ ფაილში.
"""

