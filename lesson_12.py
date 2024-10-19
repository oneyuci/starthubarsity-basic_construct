names = [0,1,2,3,4,5,6,7,8,9]
for name in names:

    if name == 4:
        name = "yuci"

    print(name)

while True:
    var_name = "YUCI"
    print(var_name == "Yuci")


    prompt = input("Play game?: ").lower()
    if prompt == "yes":
        print("Playing")
        break

    elif prompt == "no":
        print("Goodbye")
        break

    else:
        print("invalid input, Enter a Valid Input")