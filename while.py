lst = [ "Маша", "Петя", "Валера", "Саша", "Даша"]
"""i = 0
while lst[i] != "Валера":
    i += 1
    if lst[i] == "Валера":
        print ("Валера нашелся!")

def find_person(lst, person):
    if person in lst:
        print (person + " нашелся!")
    else:
        print ("нет")

       
find_person (lst, input ())"""


def get_answer(a):
    while a != "bye":
        print ("good")
        break

def ask_user():
    print ("how r u?")
    a = input()
    
   
    while a != "fine":
        get_answer(a)
        ask_user()
        break
ask_user()



