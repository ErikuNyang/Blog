def isPrime(number):
    flag = 0
    if number == 0 or number == 1:
        flag = 1
    else:
        for i in range (2, int(number/2)+1):
            if (number % i == 0):
                flag = 1
                break
        
    if flag == 0:
        return True
    else:
        return False

def updateList(number, nList):
    try:
        for i in range(int(len(nList)/number)):
            temp = i*number
            nList.remove(temp)
    except:
        pass
        

if __name__ == "__main__":
    n=100
    nList = []
    pNums = []

    for i in range (0, n+1):
        nList.append(i)   

    for item in nList:
        if isPrime(item):
            print(item, "is a prime number")
            pNums.append(item)
            updateList(item, nList)

        else:
            print(item, "is not a prime number")

    print(f"here is the list of Prime number between 1 and {n}\n", nList)