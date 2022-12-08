print("class_1 exercice 1")

class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        angle_list = [self.angle1, self.angle2, self.angle3]

        if not sum(angle_list) == 180:
            return False

        else:
            return True



my_triangle = Triangle(90, 30, 60)

print(my_triangle.check_angles())
print(my_triangle.number_of_sides)

print()
print("class_2 exercice 2")
#a revoir !
class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for sentence in self.lyrics:
            print(sentence)

happy_bday = Songs(["where are you", "and i'm so sorry", "i can not sleep, i can not dream tonight"])

happy_bday.sing_me_a_song()

print()
print("class_3 exercice 3")

class Lunch:
    def __init__(self,menu: str):
        self.menu = menu

    def menu_price(self):
        if self.menu == "menu 1":
            print(f"Your choice: {self.menu}\nPrice: 12.00")
        elif self.menu == "menu 2":
            print(f"Your choice: {self.menu}\nPrice: 13.40")
        else:
            print("Error in menu")

paul = Lunch("menu 1")

paul.menu_price()

print()
print("ex1")
#j ai du checker comment utiliser join() avec des entiers

all_numbers_list = [number for number in range(2000, 3201) if number%7 == 0 and number%5 == 0]

print("-".join(str(all_numbers) for all_numbers in all_numbers_list))

print()
print("ex2")
#j'ai cherché sur internet, j'avais pas la reponse
def factorielle(n):
    f=1
    numb_list = []
    for numb in range(1, n+1):
        f*=numb
        numb_list.append(numb)
    return ("-".join(str(i) for i in numb_list)+": "+str(f))


print(factorielle(5))

print()
print("ex3")
#je n'ai pas saisi quelle assertion faire ici

class Insert:
    def __init__(self, user_input = None):
        self.user_input = user_input

    def getString(self):
        self.user_input = input("Insert text here")
        assert "salut"==self.user_input


    def printString(self):
        print(self.user_input.upper())


user1 = Insert()

user1.getString()
user1.printString()

print()
print("ex4")

sentence = "hello world! 123"

def get_numbers_letters_in_sentence(user_sentence):
    digits = 0
    letters = 0
    for i in user_sentence:
        if i.isdigit():
            digits +=1
    for l in user_sentence:
        if l.isalpha():
            letters +=1
    return f"LETTERS : {letters}\nDIGITS : {digits}"

print(get_numbers_letters_in_sentence(sentence))

print()
print("ex5")


print()
print("ex7")
#j'ai regardé sur internet pour le slice


def is_palindrome(number):
    my_number_list =  [i for i in str(number)[::-1]]

    new_number = "".join(my_number_list)

    if number == int(new_number):
        return True
    else:
        return False

print(is_palindrome(151))

print()
print("ex8")

print()
print("ex9")
#pas compris

def get_answers(number):
    if number%3 == 0 and number%5 == 0:
        print("fizzbuzz")
    if number%3 == 0:
        print("Fizz")
    if number%5 == 0:
        print("Buzz")
    else:
        print(str(number))

get_answers(15)

print()
print("ex10")

print()
print("ex11")
#pas reussi ...
import random


def shuffling(user_string : str):
    random_user_string = "".join(random.shuffle(user_string))
    print(random_user_string)

shuffling("sdggklkjh")