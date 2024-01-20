# 1 შექმენით ფუნცია რომელსაც გადაეცემა list ტიპის მონაცემი და დააბრუნებს შებრუნებულ
# მონაცემს თითო ელემენტის გამოტოვებით

# def reversed_list(my_list):
#     result1 = my_list[::-2]
#     return result1
# my_list = [1,2,3,4,5,6,7]
# print(reversed_list(my_list))


#2.  დაწერეთ ფუნქცია რომელიც დააბრუნებს ლისთში არსებული მონაცემების უდიდეს და უმცირეს ელემენტს

# def max_min(my_list):
#     result_max = max(my_list)
#     result_min = min(my_list)
#     return result_max , result_min
# my_list = [1,2,3,4,5,6,7]
# print(max_min(my_list))


#3. შექმენით ფუნცქია რომელსაც გადაეცემა list, მისი თითოეული ელემენტი აქციეთ ტექსტურ
# მონაცემად და დააბრუნეთ ერთიანი ტექსტი
# def whole_text(my_list):
#     new_text = " "
#     for i in my_list:
#         new_text += str(i)
#     strip_text = new_text.strip()
#     return strip_text
# my_list = ["learning", "never" ,"ends"]
# print(whole_text(my_list))


# 4.შექმენით ფუნცქია რომელსაც გადაეცემა ორი set მონაცემი, დააბრუნეთ საერთო ელემეტების
# ახალი სეტი და ასევე გაერთიანებული სეტი

# def common_el_est(set1, set2):
#     result1 = set1.intersection(set2)
#     result_union =set1.union(set2)
#     return result1, result_union
# set1 = {1, 2, 3, }
# set2 = {1, 2,3, 5, 6}
# print(common_el_est(set1, set2))


#5. შექმენით ფუნცქია რომელსაც გადაეცემა ტექსტი, დაყავით ტექსტი წინადადებების
# მიხედვით და თითოეული წინადადება დაამატეთ ლისთში რომელიც
# იქნება ფუნქციის დასაბრუნებელი მნიშვნელობა

# import nltk
# def text_division(text):
#     sentences = nltk.sent_tokenize(text)
#     return sentences
#
# text = "dada dsfsfd. dfsdfs ffgfgf. sdfsfsf sffdgfd."
# print(text_division(text))

# 6.დაწერეთ ფუნქცია რომელიც აერთიანებს ორ dict ტიპის მონაცემს
# def union_dict(dict1, dict2):
#     result1 = {**dict1, **dict2}
#     return result1
# dict1 = {"location": "tbilisi", "name": "gio", }
# dict2 = {"hobby": "gaming", "age": 23, }
# print(union_dict(dict1, dict2))


# 7.დაწერეთ ფუნქცია რომელსაც გადაეცემა ტექსტი, შექმენით dict ტიპის
# მონაცემი სადაც თითოეული ასო ბგერისა და სიმბოლოს რაოდენობას ჩაწერს.

# def write_char_amount(text):
#     let_count = {"letters": 0, "symbols": 0}
#
#     for letter in text:
#         if letter.isalpha():
#             let_count["letters"] += 1
#         else:
#             let_count["symbols"] += 1
#
#     return let_count
#
# my_text = "In digital words , learning never ends!"
# print(write_char_amount(my_text))


# 8 წინა დავალებაში მიღებული მონაცემი ჩაწერეთ json ტიპის ფაილში

import json
def write_json_file(data):
    json_file = "result_data.json"
    with open(json_file, "w") as json_file:
        json.dump(data, json_file, indent=2)
        return f" data is written {json_file} in the file"

my_data = {
    "letters": 31,
    "symbols": 8
}
print(write_json_file(my_data))










