"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Create a Dice class with fields name and rolls, to simulate a dice game. The rolls field
must be a list. Create an init method that receives the name of the player and an integer n,
which represents the number of rolls. It must assign the name to the corresponding field and
create a list of n elements randomly filled with numbers from 1 to 6. Create a two-player game
asking each player his/her name. It must print the results for each one and calculate the winner,
which will be the one with the highest number of equal dices. In case of a tie, the one with the
highest total score will win.
"""
import random

class Dice:
    """This simulates a game"""

    puntuation = 0
    count=0
    def __init__(self, name=str, number=int ):
        self.name=name
        self.roll=[]
        count=0
        for i in range(number):
            numbers=random.randint(1,6)
            self.roll.append(numbers)
        for element in self.roll:
            self.puntuation+= element
            count1= self.roll.count(element)
            if count1>count:
                count = count1
        self.count=count-1

name1=str(input("Player1 name: "))
name2=str(input("Player2 name: "))
rolls=int(input("Introduce number of rolls: "))

player1=Dice(name1,rolls)
player2=Dice(name2,rolls)

print(player1.name, player1.roll, "\n Puntuation: ", player1.puntuation,
      "\nCount:", player1.count)
print(player2.name, player2.roll, "\n Puntuation: ", player2.puntuation,
      "\nCount:",  player2.count)

if player1.count != player2.count:
    if player1.count>player2.count:
        print(player1.name,"wins")
    else:
        print(player2.name, "wins")
else:
    if player1.puntuation > player2.puntuation:
        print(player1.name, "wins")
    else:
        print(player2.name, "wins")
