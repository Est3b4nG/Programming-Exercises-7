"""
Created by (Esteban Gómez) in  ${2022}
"""

"""Define a function combine (list1, list2), which given two lists returns a list that
combines both lists, but eliminates duplicates. Example:
list1: [1, 2, 3, 4, 5, 6]
list2: [4, 5, 6, 7, 8, 9]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def combinefunction(list1:list, list2:list)-> list:
    """This function combines two lists and elminate duplicates
    @param list1: a list
    @param list2: a list"""
    if type(list1)== list and type(list2)==list:
        list3=[]
        for elem in list1:
            if elem not in list3:
                list3.append(elem)
        for elem in list2:
            if elem not in list1:
                list3.append(elem)
        return list3

    else:
        raise TypeError("You need to enter a list")
list1=[]
list2=[]
elem1=0
elem2=0
while elem1!="*":
    elem1 = str(input("Enter an element for list1, when you don't want to add "
                     "more elements press * : "))
    if elem1!="*":
        list1.append(elem1)
while elem2!="*":
    elem2 = str(input("Enter an element for list2, when you don't want to add "
                      "more elements press * : "))
    if elem2 != "*":
        list2.append(elem2)

print(combinefunction(list1,list2))