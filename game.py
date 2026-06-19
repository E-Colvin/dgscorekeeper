from constants import *

class Round():
    def __init__(self,player = NAME):
        self.player =player

class Course():
    def __init__(self,name,num_holes = 18):
        self.course_name = name
        self.num_holes = num_holes
        self.holes = []
        for i in range(1,self.num_holes+1):
            self.holes.append(Hole(i))

    def __repr__(self):
        rep = f"{self.course_name}:\n\n"
        for i in range(self.num_holes):
            rep += str(self.holes[i]) +"\n"
        
        return rep

class Hole():
    def __init__(self, number, par = 3,distance = -1):
        self.number = number
        self.par = par
        self.distance = distance

    def __str__(self):
        return "Hole {:<4} {:<11} Par = {}".format(self.number, "unknown m" if self.distance <0 else f"{self.distance} m",self.par)

    def set_par(self,par):
        self.par = par

x = Course("New course")
print(x)