"""
Created by (Esteban Gómez) in  ${2022}
"""
""" Implement again the functions of the former exercise that modify the list (append, insert, etc.)
but in this case modifications must be done to the original list."""


def count(list_elements=list, element=str):
    """This function count how many of a kind there are in a function"""
    count=0
    for elem in list_elements:
        if elem== element:
            count=count+1
    return count

def index(list_elements=list, elem2=int):
    """This function tells where an element is"""
    index=0
    for i in range(len(list_elements)):
        if index==0:
            if elem2==list_elements[i]:
                index=i
    return index

def append(list_elements=list, elem1=int):
    """This function add an element to a list"""
    list_elements+=[elem1]
    return list_elements

def insert(list_elements=list, elem_to_insert=str, position=int):
    """This function add an element to a list"""
    list_elements3=list_elements.copy()
    list_elements=[]
    for elem in range(0,len(list_elements3)):
        if elem != position:
            list_elements+=[list_elements3[elem]]
        else:
            list_elements += [elem_to_insert]
    return list_elements

def remove(list_elements=list, elem=int):
    """This function the first element that the user said"""
    reps=0
    list_elements2 = list_elements.copy()
    list_elements=[]
    for i in list_elements2:
        if elem != i and reps==0:
            list_elements.append(i)
        else:
            reps=1
    return list_elements

def removeall(list_elements=list, elem=int):
    """This function remove all the elements of a kind of a list"""
    list_elements4 = list_elements.copy()
    list_elements=[]
    for i in list_elements4:
        if elem!= i:
            list_elements.append(i)
    return list_elements

def clear(list_elements=list):
    """This function delete all the values of the function"""
    list_elements=[]
    return list_elements

def pop(list_elements=list):
    """This function pop the last element of a list"""
    list_elements_for_pop = list_elements.copy()
    list_elements = []
    for i in range(0,len(list_elements_for_pop)-1):
        list_elements.append(list_elements[i])
    return list_elements

elem=0
list_elements=[]
while elem!="*":
    elem = str(input("Introduce the elements to your list: "))
    if elem!="*":
        list_elements.append(elem)

decision=0
while decision!="*":
    decision=str(input("What do you want to do, press * when you want to stop: "
                       "")).lower()

    if decision=="count":
        elem_to_count= str(input("Introduce the element you want to count: "))
        count=count(list_elements,elem_to_count)
        print(count)

    elif decision=="index":
        elem_to_index= str(input("Introduce the element you want to index: "))
        index=index(list_elements,elem_to_index)
        print(index)


    elif decision=="append":
        elem1=str(input("Introduce the element you want to append: "))
        list_elements= append(list_elements, elem1)
        print(list_elements)

    elif decision=="insert":
        elem_to_insert= str(input("Introduce the element you want to insert: "))
        position=int(input("What position: "))
        insert=insert(list_elements,elem_to_insert,position)
        print(list_elements)

    elif decision=="remove":
        elem_to_remove=str(input("Which value you want to eliminate: "))
        list_elements=remove(list_elements, elem_to_remove)
        print(list_elements)

    elif decision=="removeall":
        elems_to_remove=str(input("Which value you want to eliminate: "))
        list_elements=removeall(list_elements, elems_to_remove)
        print(list_elements)

    elif decision=="clear":
        list_elements=clear(list_elements)
        print(list_elements)

    elif decision=="pop":
        list_elements = pop(list_elements)
        print(list_elements)