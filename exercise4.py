"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Define a function that returns a tuple simulating the behaviour of the function
range(start,stop,step), which returns a sequence of numbers between the given start
integer to the stop integer incremented by the given step integer. Configure the function with
optional parameters so it also works to simulate functions range(start, stop) and
range(stop). If the provided range is incorrect an empty tuple will be returned."""

def function_range(start=int, stop=int, step=int)->int:
    """This function simulates the range(start, stop, step) function
    @param start=int
    @param stop=int
    @param step=int
    """
    if type(start)==int and type(stop)==int and type(step)==int:
        list_number=[start]
        element=start
        if stop<start:
            tup=()
        else:
            while element<stop:
                element+= 1*step
                list_number.append(element)
        final_tup=tuple(list_number)
        return final_tup
    else:
        raise TypeError("You introduced the wrong type of element")



start=int(input("Introduce your start value: "))
stop=int(input("Introduce your stop value: "))
step=int(input("Introduce your in which steps: "))

final_function=function_range(start,stop, step)
print(final_function)

