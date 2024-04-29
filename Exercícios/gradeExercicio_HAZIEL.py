import os

def printf(self):
    print(self,end="")

def grade_x(x):
    printf(x)
def grade_y(y):
    printf(y)

def grade_completa():
    os.system('cls')
    j=0
    for x in range(11):
        if j%5 ==0 or j == 0 :
            for x in range(2):
                grade_x(x="+")
                grade_x(x=4*" - ")
            grade_x(x="+\n")
        j+=1    
        if j < 11:
            for y in range(2):
                grade_y(y="|")
                grade_y(y=4*"   ")
            grade_y(y="|\n")
grade_completa()