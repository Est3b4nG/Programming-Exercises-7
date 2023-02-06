"""
Created by (Esteban Gómez) in  ${2022}
"""
""". Create classes to represent the objects needed for the final project. Create init methods for all
of them"""

class player:
    """This class will have all the functions related to the players
    aircraft"""

    def __int__(self, image, position,lives, bullets, buffs):
        self.image=image
        self.position=position
        self.lives=lives
        self.bullets=bullets
        self.buffs=buffs

class enemy:
    """This class have all the functions related to the enemies"""

class puntutation:
    """This class have all the funtions related to the puntuation"""
    def __int__(self, puntuation, aircrafts_destroyed ):
        self.puntuation= puntuation
        self.aircrafts_destroyed=aircrafts_destroyed

class background:
    """This class will have all the functions related to the background"""
    def __int__(self, image, dimension):
        self.image=image
        self.dimension=dimension