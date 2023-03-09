# Part 1-Encryption and Decryption (question1-6)
import random
mad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
MAD = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(data,num):
    ans = []
    for i in range(len(data)):
        if data[i] in MAD:
            temp_num = MAD.index(data[i])+num
        elif data[i] in mad:
            temp_num = mad.index(data[i])+num
        else:
            ans.append(data[i])
            continue
        temp_num = temp_num%26
        ans.append(MAD[temp_num])
    return ''.join(ans)

def decode(data,num):
    ans = []
    for i in range(len(data)):
        if data[i] in MAD:
            temp_num = MAD.index(data[i])-num
        elif data[i] in mad:
            temp_num = mad.index(data[i])-num
        else:
            ans.append(data[i])
            continue
        temp_num = temp_num%26
        ans.append(MAD[temp_num])
    return ''.join(ans)

modType = ""
num = 0
text = ""
while True:
    modType = input("The cipher mode('encrypt' or 'decrypt'):")
    if modType=="encrypt" or modType=="decrypt": break
    print("Please enter 'encrypt' or 'decrypt'!")

while True:
    num = input("A rotation value(a integer or 'random'):")
    if num.isdigit(): break
    if num[0]=="-" and num[1::].isdigit:break
    if num=="random": break
    print("Please enter a integer or 'random'!")

text = input("A message:")

if num=="random":
    num = random.randint(0,25)
else:
    num = int(num)
    
data = ""
if modType=="encrypt":
    data = encrypt(text,num)
else :
    data = decode(text,num)
print(data)
