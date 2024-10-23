while True:
        number1 = (input("Enter The First number: Type q to Quit  " ))
        if number1 == "q":
            break
        number2 = input("Choose Operation: Type q to Quit ")
        if number2 == "q":
            break
        number3 = (input("Enter Second Number: Type q to quit "))
        if number3 == "q":
            break
        

        if number2 == "/":
            div = float(number1) / float(number3)
            print(div)
            while True:
                true1 = input("Do you wish to continue: ").lower()
                if true1 == "no":
                    break
                elif true1 == "yes":
                    break
                else:
                    print("Invalid Input - Please Input Yes or No: ")
            if true1 == "no":
                break

        elif number2 == "*":
            multi = float(number1) * float(number3)
            print(multi)
            while True:
                true1 = input("Do you wish to continue: ").lower()
                if true1 == "no":
                    break
                elif true1 == "yes":
                    break
                else:
                    print("Invalid Input - Please Input Yes or No: ")
            if true1 == "no":
                break

        elif number2 == "+":
            sum1 = float(number1) + float(number3)
            print(sum1)
            while True:
                true1 = input("Do you wish to continue: ").lower()
                if true1 == "no":
                    break
                elif true1 == "yes":
                    break
                else:
                    print("Invalid Input - Please Input Yes or No: ")
            if true1 == "no":
                break

        elif number2 == "-":
            sub = float(number1) - float(number3)
            print(sub)
            while True:
                true1 = input("Do you wish to continue: ").lower()
                if true1 == "no":
                    break
                elif true1 == "yes":
                    break
                else:
                    print("Invalid Input - Please Input Yes or No: ")
            if true1 == "no":
                break

    
        