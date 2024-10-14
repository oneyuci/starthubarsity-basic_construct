import json
def int_converter(value, value2):
        print(type(value))
        print(type(value2))
        try:
            if type(value) == int: 
                type(value2) == int
                print(value + value2)

            elif type(value) == int:
                 type(value2) == float
                 print(value + int(value2))

            elif type(value) == int:
                 type(value2) == str
                 number = json.loads(value2)
                 print(value + int(number) )

            elif type(value) == float:  
                type(value2) == float
                print(int(value) + int(value2))

            elif type(value) == float:
                 type(value2) == str
                 number = json.loads(value2)
                 print(int(value) + int(number))

            elif type(value) == float:
                 type(value2) == int
                 print(int(value) + value2)

            elif type(value) == str: 
                type(value2) == str
                number = json.loads(value) 
                number2 = json.loads(value2)
                print(int(number) + int(number2))

            elif value == True:
                print(1)
            elif value == False:
                print(0)
        except(TypeError, ValueError, NameError):
            print("Cannot be converted")
                    
int_converter(2.5, "34")
