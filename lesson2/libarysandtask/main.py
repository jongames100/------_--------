
from grades import grades_avr
def addgrade():
    gradearr=[]
    amountofgrades=input("how many grades do you are going to input")
    for i in range(int(amountofgrades)):
        gradearr.append(int(input("input a grade")))
    print(gradearr)
    return grades_avr(gradearr)
    

if __name__=='__main__':
    print(f"[blue] the avr of your grades are: {addgrade()}")