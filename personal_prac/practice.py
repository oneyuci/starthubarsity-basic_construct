while True:
    try:
        movie_ticket_price = int(input("What is your age: "))
        movie_ticket_price2 = int(input("What is the time: "))


        if movie_ticket_price <= 0:
            print("Invalid input - Please Input A Valid Age")

        elif movie_ticket_price  < 2 or movie_ticket_price == 2:
            print("The Ticket Is Free")

            while True:
                true1 = input("Do you wish to continue: ").lower()
                if true1 == "no":
                    print("Goodbye!")
                    break
                elif true1 == "yes":
                    break
                else:
                    print("Invalid Input - Please Input Yes or No")
            if true1 == "no":
                break
                    

        elif movie_ticket_price == 12 or movie_ticket_price < 12:
            print("The ticket is $10")
            while True:
                true1 = input("Do you wish to continue: ").lower()
                if true1 == "no":
                    print("Goodbye!")
                    break
                elif true1 == "yes":
                    break
                else:
                    print("Invalid Input - Please input Yes or No")
            if true1 == "no":
                break

        elif movie_ticket_price > 12:
            print("The ticket is $15")
            while True:
                true1 = input("Do you wish to continue: ").lower()
                if true1 == "no":
                    print("Goodbye!")
                    break
                elif true1 == "yes":
                    break
                else:
                    print("Invalid Input - Please input Yes or No")

            if true1 == "no":
                break

                

    except (ValueError):
        print("Invalid Input - Please Input a valid number")

   

