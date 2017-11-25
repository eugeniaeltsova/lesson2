#школа
grades = [{"school_class" : "4a", "scores" : [5,5,4,4,3,5,2,3,5,5,4]}, {"school_class" : "5a", "scores" : [5,5,4,4,3,5,2,3,2,4,3,4]}, {"school_class" : "6a", "scores" : [5,3,4,3,4,3,2,4,3,5,2,3,5,5,4]}, {"school_class" : "7a", "scores" : [5,5,4,4,3,5,2,3,5,5,4,2,3,2,4,5,2]}]
summ_school = 0
len_school = 0
for elem in grades:
    summ = 0
    for i in range(len(elem["scores"])):
        summ += float(elem["scores"][i])
    average_grade_class = summ/len(elem["scores"])
    summ_school += summ
    len_school += len(elem["scores"])

   
    
    print("Average grade for " + elem["school_class"] + " is " + str(average_grade_class) + ".")
average_grade_school = summ_school/len_school
print ("Average grade for school is " + str(average_grade_school) + ".")

   
#список
lst = []
import random
for i in range(10):
    lst.append(random.randint(0,1000))
    print (int(lst[i] + 1), end = " ")

#строка
s = input()
for i in s:
    print(i)



