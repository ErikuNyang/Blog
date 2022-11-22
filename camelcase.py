import re

def splitWords(Ops, MCV, Words):
    indexes = []
    Temp = ""
    lenWords = len(Words)
    if MCV.upper() == 'M':
        for i in re.search("[A-Z]", Words):
            Words = Words.replace(i, " "+i)
        Words = Words[:-2]

    elif MCV.upper() == 'C':
        for i in re.search("[A-Z]", Words)[1:]:
            Words = Words.replace(i, " "+i)
        
    elif MCV.upper() == 'V': 
        for i in re.search("[A-Z]", Words):
            Words = Words.replace(i, " "+i)

    else:
        print("unknown type," MCV)

    Words = Words.lower()
    return Words

def combineWords(Ops, MCV, Words):
    lenWords = len(Words)
    if MCV.upper() == 'M':
        for i in re.search("\s", Words):
            Words = Words.replace(i,"")
        Words = Words[:-2]
    elif MCV.upper() == 'C':
        for i in range (lenWords):
            if Words[i] == " ":
                Temp = Words[0].upper() + Words[1:i] + Words[i+1].upper() + Words[i+2:]
    else: 
        for i in range (lenWords):
            if Words[i] == " ":
                Temp = Words[:i] + Words[i+1].upper() + Words[i+2:]
    Words = Temp
    return Words

if __name__ == '__main__':
    while True:
        try:
            userInput = input().rstrip()
            Ops, MCV, Words = userInput.split(";")
            if Ops.upper() == 'S':
                print(splitWords(Ops, MCV, Words))
            elif Ops.upper() == 'C':
                print(combineWords(Ops, MCV, Words))
            else:
                print("Wrong Operation: ", Ops) 
        except:
            pass