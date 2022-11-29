from typing import List

print("dict1 exercice 1")
#pas reussi, j'ai du chercher sur  internet

keys = ['ten', 'twenty', 'thirty']
values = [10, 20, 30]

my_dict={}

for i in range(len(keys)):
    my_dict[keys[i]]=values[i]

print(my_dict)

print()
print("dict2 exercice 2")

dict1={'ten': 10, 'twenty': 20, 'thirty': 30}
dict2={'thirty': 30, 'fourty': 40, 'fifty': 50}

for key, value in dict2.items():
    dict1[key] = value

print(dict1)

print()
print("dict3 exercice 5")

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
my_new_dict={}

def add_to_dict(dict_, key1):
    for key, value in dict_.items():
        if key==key1:
            my_new_dict[key]=value
    return my_new_dict

print(add_to_dict(sample_dict, "name"))
print(add_to_dict(sample_dict, "salary"))
print()

print("dict4 exercice 6")

dict_ex4={"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

def remove_to_dict(dict_, key1):
    for key in dict_.keys():
        if key==key1:
            dict_.pop(key)
            break
    return dict_ex4

print(remove_to_dict(dict_ex4, "name"))
print(remove_to_dict(dict_ex4, "salary"))

print()
print("dict5 exercice 9")

sample_dict_ex9 = {'Physic': 82, 'Math': 65, 'History': 75}
get_value=[]
for i in sample_dict_ex9.values():
    get_value.append(i)

min_value=min(get_value)

for key, value in sample_dict_ex9.items():
    if value == min_value:
        print(key)

print()
print("lis1 exercice 5")

numbers_x=[10, 20, 30, 40, 10]
numbers_y=[75, 65, 35, 75, 30]

def is_same_number(numb_list: List):
    if numb_list[0] == numb_list[-1]:
        return True
    else:
        return False

print(is_same_number(numbers_x))
print(is_same_number(numbers_y))

print()
print("list2 exercice 6")

numb_list=[10, 20, 33, 46, 55]


for i in numb_list:
    if i%5 == 0:
        print(i)

print()
print("list3 exercice 10")

list1= [10, 20, 25, 30, 35]
list2=[40, 45, 60, 75, 90]
new_list=[]

for i in list1:
    if i%2 ==1:
        new_list.append(i)
    for n in list2:
        if n%2==0:
            new_list.append(n)

print(set(new_list))

print()
print("str1 exercice 4")

chars_list=[]
def remove_chars(word: str, chars_to_remove: int):
    if chars_to_remove<=len(word):
        for i in word:
            chars_list.append(i)

        for _ in range(chars_to_remove):
            chars_list.pop(0)

        final_word="".join(chars_list)

        return final_word
    else:
        print("n must be less than the lengh of the string")

print(remove_chars("pynative", 4))

print()
print("str2 exercice 9")

s1= "PYnative29@#8496"

int_chars=[]

for i in s1:
    if i.isdigit():
        int_chars.append(int(i))
print(f"Sum is: {sum(int_chars)}\nAverage is: {sum(int_chars) / len(int_chars)}")

print()
print("str3 exercice 10")
#j'ai cherché comment utiliser 'count()', je ne m'en rapellais plus

str1="Apple"
count_dict={}

for i in str1:
    x=str1.count(i)
    count_dict[i]=x

print(count_dict)