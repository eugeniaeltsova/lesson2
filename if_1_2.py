age = int(input("your age, please, "))
if age < 0:
    print ("you must be joking")
elif age < 6:
    print ("you belong to a kindergarten")
elif age < 18:
    print ("school is your place")
elif age < 23:
    print ("it's party time, bro")
else:
    print ("arbeit macht frei")

def compare(a,b):
    if a== b:
        return 1
    elif a != b and b == "learn":
        return 3
    elif a != b and len(a) > len(b):
        return 2
    
print (compare(input(), input()))

#какой приоритет условий? длина или значение строки b?
