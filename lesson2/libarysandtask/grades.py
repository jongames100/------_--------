def grades_avr(gradearr):
    print("hi")
    sum=0
    for i in gradearr:
        sum=sum+i
        print(sum)
    return sum/(len(gradearr))