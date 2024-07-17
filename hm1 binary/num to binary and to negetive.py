num=int(input(" pick a num"))
bits=input('put a number of bits you want')
binary=[]
for i in range(int(bits)):
    binary.append("0")
print(binary)
sum=0
for i in range (len(binary)-1):
    if num%2!=0:
        binary[i]=1
    num=num//2
binary.reverse()
print(binary)

#antil here is making it a binary number

for k in range(len(binary)):
    if binary[k]==1:
        binary[k]=0
    else:
        binary[k]=1
binary[len(binary)-1]+=1
l=len(binary)-1
while l>-1:
    if binary[l]==2:
        if l!=0:
            binary[l]=0
            l=l-1
            binary[l]+=1
    else:
        l-=1
print(binary)