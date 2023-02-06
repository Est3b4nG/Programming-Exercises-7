"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Create the Student class, which represents a first year student. Its fields will be: name,
surname, programming mark, algebra mark, calculus mark, physics mark,
skills mark and humanities mark. Create an init method that receives values for all the
fields. Write a program that creates an object of this type, fills the fields asking the user by
keyboard and prints them"""

class Students:
   """Class documentation"""

   def __init__(self, name=str,surname=str, programming_mark=float,
                algebra_mark=float, calculus_mark=float, physics_mark=float,
                skills_mark=float, humanities_mark=float):
       """ This method both declares the attributes of the class and
        receives the initial value of all them"""

       self.name=name
       self.surname=surname
       self.programming_mark=programming_mark
       self.algebra_mark=algebra_mark
       self.calculus_mark=calculus_mark
       self.physics_mark=physics_mark
       self.skills_mark=skills_mark
       self.humanities_mark=humanities_mark

   @property
   def name(self):
         return self.__name

   @name.setter
   def name(self, name: str):
      if type(name) != str:
         raise TypeError("The name must be an str")
      else:
          self.__name= name


   @property
   def surname(self):
      return self.__surname


   @surname.setter
   def surname(self, surname: str):
      if type(surname) != str:
         raise TypeError("The surname must be an str")
      else:
          self.__surname=surname

   @property
   def programming_mark(self):
      return self.__programming_mark


   @programming_mark.setter
   def programming_mark(self, programming_mark: float):
      if type(programming_mark) != float:
         raise TypeError("The mark must be a float")
      if programming_mark>10 or programming_mark<0:
          raise ValueError("The grade must be between 0 and 10")
      else:
          self.__programming_mark=programming_mark


   @property
   def algebra_mark(self):
      return self.__algebra_mark


   @algebra_mark.setter
   def algebra_mark(self, algebra_mark: float):
      if type(algebra_mark) != float:
         raise TypeError("The mark must be an float")
      if algebra_mark>10 or algebra_mark<0:
          raise ValueError("The grade must be between 0 and 10")
      else:
          self.__algebra_mark=algebra_mark

   @property
   def calculus_mark(self):
      return self.__calculus_mark


   @calculus_mark.setter
   def calculus_mark(self, calculus_mark: float):
      if type(calculus_mark) != float:
         raise TypeError("The mark must be an float")
      if calculus_mark>10 or calculus_mark<0:
          raise ValueError("The grade must be between 0 and 10")
      else:
          self.__calculus_mark=calculus_mark


   @property
   def physics_mark(self):
      return self.__physics_mark


   @physics_mark.setter
   def physics_mark(self, physics_mark: float):
      if type(physics_mark) != float:
         raise TypeError("The mark must be an float")
      if physics_mark>10 or physics_mark<0:
          raise ValueError("The grade must be between 0 and 10")
      else:
          self.__physics_mark=physics_mark

   @property
   def skills_mark(self):
       return self.__skills_mark

   @skills_mark.setter
   def skills_mark(self, skills_mark: float):
       if type(skills_mark) != float:
           raise TypeError("The mark must be an float")
       if skills_mark > 10 or skills_mark < 0:
           raise ValueError("The grade must be between 0 and 10")
       else:
           self.__skills_mark = skills_mark

   @property
   def humanities_mark(self):
       return self.__humanities_mark

   @humanities_mark.setter
   def humanities_mark(self, humanities_mark: float):
       if type(humanities_mark) != float:
           raise TypeError("The mark must be an float")
       if humanities_mark > 10 or humanities_mark < 0:
           raise ValueError("The grade must be between 0 and 10")
       else:
           self.__humanities_mark = humanities_mark

   def str(self):
        data=("%s %s: Programming: %f, Algebra: %f, Calculus: %f, Physics: "
              "%f, Skill: %f, Humanities: %f ")%(self.name,self.surname,
              self.programming_mark,self.algebra_mark,self.calculus_mark,
              self.physics_mark, self.skills_mark, self.humanities_mark)
        return data



name=(input("Introduce your name: "))
surname=(input("Introduce your surname: "))
programming_mark= float(input("Introduce your programming grade: "))
algebra_mark= float(input("Introduce your algebra grade: "))
calculus_mark= float(input("Introduce your calculus grade: "))
physics_mark= float(input("Introduce your physics grade: "))
skills_mark= float(input("Introduce your skills grade: "))
humanities_mark= float(input("Introduce your humanities grade: "))


your_data=Students(name, surname,programming_mark,algebra_mark,
                   calculus_mark,physics_mark,skills_mark,humanities_mark)
print(your_data.str())







