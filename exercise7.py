"""
Created by (Esteban Gómez) in  ${2022}
"""
"""The Fibonacci sequence is defined by the following formula:
if n = 0 f(n) = 0
if n = 1 f(n) = 1
if n > 1 f(n) = f(n - 1) + f(n - 2)
Define a function that prints the Fibonacci sequence from a given number. Example:
fibonacci(7)
Output: [0, 1, 1, 2, 3, 5, 8, 13]
"""

def fibonnaci(number=int) -> int:
    """This function find the fibonnaci sequence for a number
    @param numnber= int"""
    sequence=[]
    if type(number)== int:
        if number==0:
            sequence=0
        elif number==1:
            sequence=1
        elif number>1:
            for i in range(number+1):
                if i==0:
                    sequence.append(0)
                elif i==1:
                    sequence.append(1)
                elif i>1:
                    f_elem= sequence[-1] + sequence[-2]
                    sequence.append(f_elem)

        return sequence
    else:
        raise TypeError("You didn't introduced a number")

number=int(input("introduce a number: "))
print(fibonnaci(number))