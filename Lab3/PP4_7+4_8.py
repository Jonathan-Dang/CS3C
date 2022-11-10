import random

print("Processing PP4-7")#------------------------------------------------------------
#Recieve input and then process i and t
str = input("Please input a single word:")
i = -1
while (i == -1 and i != str.__len__() - 1):
    i = random.randint(0,str.__len__() - 1)
t = -1
while (t == -1 and t > i):
    t = random.randint(i,str.__len__() - 1)

stri = str[i]
strt = str[t]
#Substrings are written with the : operator to indicate Start and Stopping indexies.
#If a 3rd one is implemented, then the steps would be changes, as is to say that 
#we would get that interval of character
front = str[0:int(i)]
mid = str[i:t]
end = str[t:(str.__len__() - 1)]

print(front + strt + mid + stri + end)

print("Processing PP4-8")#-------------------------------------------------------------
for i in range(str.__len__()):
    print(str[i])
    
    
'''
Processing PP4-7
Please input a single word:Linguist
Lingutisi
Processing PP4-8
L
i
n
g
u
i
s
t
'''