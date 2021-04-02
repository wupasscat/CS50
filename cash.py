while (True):
    coins = 0
    changeInput = input("Change owed: ")
    inputCheck = changeInput.replace('.', '')
    inputCheck = inputCheck.replace('$', '')
    changeInput = changeInput.replace('$', '')
    print("input: ", changeInput)
    print("strip: ", inputCheck)
    if inputCheck.isnumeric():
        floatInput = float(changeInput)
        print("floatinput: ", floatInput)
        if floatInput > 0.00:
            cents = int(floatInput * 100)
            print("cents: ", cents)
            while(cents >= 25):
                cents -= 25
                coins += 1
            while(cents >= 10):
                cents -= 10
                coins += 1
            while(cents >= 5):
                cents -= 5
                coins += 1
            while(cents >= 1):
                cents -= 1
                coins += 1
            print("Coins: ", coins)
        else:
            print("(!) Please input a number above 0")
    else:
        print("(!) Please input a valid number")