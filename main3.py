# Part 3-Messages from a File (question1-4)
import os
import random
mad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
MAD = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def keepLetters(word):
    ans=[]
    for i in word:
        if i in mad or i in MAD:
            ans.append(i)
    return ''.join(ans)
def writeInTxt(path,s):
    with open(path,"w") as f:
        f.write(s)
def analyze(text):
    ans = {
    'total':0,
    'word_num':0,
    'words':[],
    'words_ten':[],
    'minWord_len':-1,
    'maxWord_len':-1,
    'maxLetter':''
    }
    data = text.split()
    words = []
    number = []
    for i in data:
        if i in words:
            number[words.index(i)] = number[words.index(i)]+1
        else:
            words.append(keepLetters(i))
            number.append(1)
    datas = []
    letter_num =[0]*26
    for i in range(len(words)):
        if words[i]=='':continue
        datas.append((words[i],number[i]))
        lennum = len(words[i])
        if lennum > ans["maxWord_len"] or ans["maxWord_len"] ==-1:
            ans["maxWord_len"]=lennum
        if lennum < ans["minWord_len"] or ans["minWord_len"] ==-1:
            ans["minWord_len"]=lennum
    datas = sorted(datas,key=lambda x:x[1],reverse=True)
    ans["total"] = len(data)
    ans["word_num"] = len(datas)
    ans["words"] = datas
    for i in range(len(datas)):
        if i <10 :
            ans["words_ten"].append(datas[i])
        for j in datas[i][0]:
            if j in MAD:
                letter_num[MAD.index(j)] = letter_num[MAD.index(j)]+datas[i][1]
            else:
                letter_num[mad.index(j)] = letter_num[mad.index(j)]+datas[i][1]
    letters = []
    for i in range(26):
        letters.append((MAD[i],letter_num[i]))
    letters = sorted(letters,key=lambda x:x[1],reverse=True)
    ans["maxLetter"] = letters[0][0]
    writeThings=[]
    writeThings.append("total number of words:")
    writeThings.append(str(ans["total"]))
    writeThings.append("\n")
    writeThings.append('number of unique words:')
    writeThings.append(str(ans["word_num"]))
    writeThings.append("\n")
    writeThings.append("minimum word length:")
    writeThings.append(str(ans["minWord_len"]))
    writeThings.append("\n")
    writeThings.append("maximum word length:")
    writeThings.append(str(ans["maxWord_len"]))
    writeThings.append("\n")
    writeThing = ''.join(writeThings)
    writeInTxt("./main2.txt",writeThing)
    return ans
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
textMod = ""
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

while True:
    textMod = input("A message entry mode('manual entry' or 'read from file'):")
    if textMod=="read from file" or textMod=="manual entry": break
    print("Please enter 'manual entry' or 'read from file'!")

if textMod=="manual entry":
    text = input("A message:")
else:
    while True:
        textName = input("filename(including file path):")
        err = os.path.exists(textName)
        if err:
            f = open(textName)
            text = f.read() 
            f.close()
            break
        else :
            print("File("+textName+") does not exist!")

if num=="random":
    num = random.randint(0,25)
else:
    num = int(num)
    
data = ""
if modType=="encrypt":
    data = encrypt(text,num)
    print("Encrypted message:")
    ans = analyze(text)
else :
    data = decode(text,num)
    print("Decrypted message:")
    ans = analyze(data)
print(data)
print("Total number of words:"+str(ans["total"]))
print("Number of unique words:"+str(ans["word_num"]))
print("(Up to)The ten most common words:")
for i in ans["words_ten"]:
    print(i[0]+"::"+str(i[1]))
print("Minimum word length:"+str(ans["minWord_len"]))
print("Maximum word length:"+str(ans["maxWord_len"]))
print("Most common letter:"+ans["maxLetter"])
