#Write functions that add, subtract, and multiply two numbers in their digit-list representation (and return a new digit list).

####################
##Asking for numbers ##
####################
inputConfirm = False
while inputConfirm == False:
    inputA = False
    while inputA == False:
        try:
            print("enter your first integer brah")
            u = int(input())
            inputA = True
        except Exception:
            print("\n\n***INVALID INPUT***")

    inputB = False
    while inputB == False:
        try:
            print("enter your second integer duuuuude")
            t = int(input())
            inputB = True
        except Exception:
            print("\n\n***INVALID INPUT***")

    def numToList(number):
        k = str(number)
        defList = list(k)
        defList = [int(i) for i in defList]
        return defList

    numA = numToList(u)
    numB = numToList(t)

    numAlength = len(numA)
    numBlength = len(numB)

    ##################
    ## choosing method ##
    ##################
    inputC = False
    while inputC == False:
        try:
            print("whacca wanna do with them numbers eh? Add, subtract or multiply?\n\nEnter either one of these:\nadd/subtract/multiply")
            daMethod = str(input())
            assert daMethod == "add" or daMethod == "subtract" or daMethod == "multiply"
            inputC = True
        except Exception:
            print("\n\n***INVALID INPUT***")

    print("\nyour numbers are:\n")
    print(numA, numB)
    print("...and we will do the following with them: ", daMethod)
    print("is this okay for you? (y/n)")
    okayInputQuestion = False
    while okayInputQuestion == False:
        try:
            inpConfAns = str(input())
            assert inpConfAns == "y" or inpConfAns == "n"
            if inpConfAns == "y":
                okayInputQuestion = True
                inputConfirm = True
            else:
                print("*** USER ABORT ***")
                break
        except Exception:
            print("***INVALID INPUT***")

biggerNumber = 0
smallerNumber = 0
if numAlength > numBlength:
    biggerNumber = numA
    smallerNumber = numB
else:
    biggerNumber = numB
    smallerNumber = numA

smallerNumberLength = len(smallerNumber)
biggerNumberLength = len(biggerNumber)

################
## Add method ##
################

    ##
    #### numbers' length are the same

if daMethod == "add":
    wasItBig = False
    addedNumber = []
    addCounterA = -1
    if numAlength == numBlength:
        while addCounterA >= (numAlength * (-1)):
            num = numA[addCounterA] + numB[addCounterA]
            if wasItBig == True:
                num += 1
            if num > 9:
                num -= 10
                wasItBig = True
            else:
                wasItBig = False
            addedNumber.insert(0, num)
            addCounterA -= 1

        if wasItBig == True:
            addedNumber.insert(0, 1)

        print("The sum of the two numbers on digit level is: ", addedNumber)

    ##
    #### numbers' length are NOT the same
    else:


        smallerNumberLength = len(smallerNumber)
        biggerNumberLength = len(biggerNumber)

        while addCounterA >= (smallerNumberLength * (-1)):
            num = numA[addCounterA] + numB[addCounterA]
            if wasItBig == True:
                num += 1
            if num > 9:
                num -= 10
                wasItBig = True
            else:
                wasItBig = False
            addedNumber.insert(0, num)
            addCounterA -= 1

        while addCounterA >= (biggerNumberLength * (-1)):
            num = biggerNumber[addCounterA]
            if wasItBig == True:
                num += 1
            if num > 9:
                num -= 10
                wasItBig = True
            else:
                wasItBig = False
            addedNumber.insert(0, num)
            addCounterA -= 1

        if wasItBig == True:
            addedNumber.insert(0, 1)

        print("The sum of the two numbers on digit level is: ", addedNumber)

#####################
## Multiply method ##
#####################

if daMethod == "multiply":

    multiCounterA = -1
    multiCounterB = -1
    szorzo = 1
    statikSzorzo = 1
    bigCounter = 0
    multiTemp = []

    while multiCounterB >= (smallerNumberLength * (-1)):
        while multiCounterA >= (biggerNumberLength * (-1)):
            mTemp = ((biggerNumber[multiCounterA] * szorzo) * (smallerNumber[multiCounterB]))
            multiTemp.append(mTemp * statikSzorzo)
            multiCounterA -= 1
            szorzo *= 10
        szorzo = 1
        statikSzorzo *= 10
        multiCounterB -= 1
        multiCounterA = (-1)
    print("The result of the two numbers multiplied is: ", numToList(sum(multiTemp)))
