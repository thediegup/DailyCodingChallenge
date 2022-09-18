def multiplyList(myList):
    result = 1
    x=0
    a=0
    newList = []
    while a < len(myList):
        for x in range(a+1,len(myList)):
            result = result * myList[x]
        a = a + 1
        newList.append(result)
        result = 1
    return newList

list = [2, 4, 7, 8, 9]
print(multiplyList(list))



