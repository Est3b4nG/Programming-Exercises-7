"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Create a function that receives as parameters a list and an element and returns a tuple with the
positions of the element in the list, or the empty tuple if the element is not in the list. Invoking
this function, create another one that receives two lists and an element and returns if any of the
appearances of the element is at the same position in both lists.
"""

def list_funtion(list1=list, element=str)-> list and str:
    """This function recieves a list and returns a tuple with the position
    of the elements in the list
    @param list1: list
    @param number: int"""
    if type(list1)==list and type(element)==str:
        position_list=[]
        for elem in range(len(list1)):
            if list1[elem] == element:
                position_list.append(elem)
        position=tuple(position_list)
        return position
    else:
        raise TypeError("You introduced something different to a list and "
                        "string")


list1=[]
element=0
while element!="*":
    element=str(input("Introduce the elements of the list, press * to stop "
                      "introducing elements: "))
    list1.append(element)

element_to_search= str(input("Introduce the element you want to find the "
                             "position of: "))

final_list= list_funtion(list1, element_to_search)
print(final_list)
print(type(final_list))

final_list1=[]
while type(final_list)==tuple and len(final_list1)==0:
    def lists2_funtion(list1=list, list2=list, element=str)-> list and str:
        """This function recieves two list and compare them to see if they
        have the same elements in the same position
        @param list1: list
        @param list2: list
        @param number: int"""
        if type(list1)==list and type(element)==str:
            position_list1=[]
            for elem in range(min(len(list1),len(list2))):
                if list1[elem] == element and list2[elem] == element and \
                        list1[elem] == list2[elem]:
                    position_list1.append(elem)
            position1=tuple(position_list1)
            return position1
        else:
            raise TypeError("You introduced something different to a list and "
                            "string")

    list1=[]
    list2=[]
    element=0
    while element!="*" :
        element=str(input("Introduce the elements of the list 1, press * to stop "
                          "introducing elements: "))
        list1.append(element)
    element=0
    while element != "*":
        element = str(input("Introduce the elements of the list 2, press * to "
                      "stop introducing elements: "))
        list2.append(element)
    element_to_search1 = str(input("Introduce the element you want to know "
                                   "if have the same postions in both lists: "))

    final_list1= lists2_funtion(list1,list2, element_to_search1)
    print(final_list1)