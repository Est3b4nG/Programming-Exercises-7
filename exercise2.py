"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Create three functions to: (a) ask the user for a positive number in the range (1, 10), (b)
generate a random list of this number of elements and (c) to find the minimum of the list.
Create a program that uses them.
"""
import random
def function_positive(number=int)->int:
    """This function asks for a postive number in range(1,10)
    @param1=int"""
    if type(number)==int:
        while number<0 or number>10:
            number=int(input("Enter a positive number: "))
        return number

    else:
        raise TypeError("You need to introduce a positive number")



def random_list(length=int)->int:
    """Creates random list from the number returned from the first function
    @param1=int"""
    if type(length)==int:
        list1=[]
        for i in range(length):
            element=random.randint(1,10)
            list1.append(element)
        return list1
    else:
        raise TypeError("Introduce a number please")



def minimum_elem(final_list=list)->list:
    if type(final_list)==list:
        minimum=final_list[0]
        for elem in final_list:
            if elem < minimum:
                minimum=elem
        return minimum
    else:
        raise TypeError("Introduce a list please")


print("How many types of Wood do you want?")
number=int(input("Enter a positive number smaller than 10: "))
final_number=function_positive(number)
print(final_number)

print("Which types of wood?")
final_list= random_list(final_number)
print(final_list)

print("The most basic type you want is: ")
minimum=minimum_elem(final_list)
print(minimum)

