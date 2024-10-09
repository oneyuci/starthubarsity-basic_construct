import json
def int_converter(value):
        print(type(value))
        try:
            if type(value) == int:
                print(value)

            elif type(value) == float:
                print(int(value))

            elif type(value) == str:
                number = json.loads(value)
                print(int(number))

            elif value == True:
                print(1)
            elif value == False:
                print(0)
        except(TypeError, ValueError, NameError):
            print("Cannot be converted")
                    
int_converter("trtr")
