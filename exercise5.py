"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Create a program that creates functions which are your own versions of the list methods. Do not
make use of any built-in list methods to implement them. Your program must do all the
necessary checks to make sure that all the functions work. For functions modifying the original
list, the list must not be changed, but a modified version of it must be returned.
count(list1, x): returns the number of elements with the specified value.
index(list1, x): returns the index of the first element with the specified value. If the value
does not exist, the function returns None.
append(list1, x): adds an element at the end of the list.
insert(list1, x, index): adds an element at the specified position.
remove(list1, x): removes the first element in the list with the specified value.
removeAll(list1, x): removes all the elements in the list with the specified value.
clear(list1): removes all the elements from the list.
pop(list1): removes the last element of the list and returns its value."""

def count(list_elements=list, element=str):
    """This function count how many of a kind there are in a function"""
    count=0
    for elem in list_elements:
        if elem== element:
            count=count+1
    return count

def index(list_elements=list, elem2=int):
    """This function tells where an element is"""
    for i in range(len(list_elements)):
        if elem2==list_elements[i]:
            index=i
    return index

def append(list_elements=list, elem1=int):
    """This function add an element to a list"""
    list_elements+=[elem1]
    return list_elements

#def insert(list_elements=list, elem_to_insert=str):
#    """This function add an element to a list"""

 #   return index

def remove(list_elements=list, elem=int):
    """This function the first element that the user said"""
    list_elements=[]
    reps=0
    list_elements2 = list_elements.copy()
    for i in list_elements2:
        if elem != i and reps==0:
            list_elements.append(i)
        else:
            reps=1
    return list_elements

def removeall(list_elements=list, elem=int):
    """This function remove all the elements of a kind of a list"""
    list_elements=[]
    for i in list_elements:
        if elem!= i:
            list_elements.append(i)
    return list_elements

def clear(list_elements=list):
    """This function delete all the values of the function"""
    list_elements=[]
    return list_elements

def pop(list_elements=list):
    """This function pop the last element of a list"""
    list_elements1 = list_elements.copy()
    list_elements = []
    for i in range(len(list_elements1)-1):
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
        insert=index(list_elements,elem_to_index)
        print(insert)

    elif decision=="append":
        elem1=str(input("Introduce the element you want to append: "))
        final_list=[2,3]
        final_list= append(list_elements, elem1)
        print(final_list)

    elif decision=="insert":
        elem_to_insert= str(input("Introduce the element you want to insert: "))
        index=index(list_elements,elem_to_insert)
        print(index)

    elif decision=="remove":
        elem_to_remove=str(input("Which value you want to eliminate: "))
        remove=remove(list_elements, elem_to_remove)
        print(remove)

    elif decision=="removeall":
        elems_to_remove=str(input("Which value you want to eliminate"))
        remove=removeall(list_elements, elems_to_remove)
        print(remove)

    elif decision=="clear":
        remove=removeall(list_elements)
        print(remove)

    elif decision=="pop":
        pop = pop(list_elements)
        print(pop)