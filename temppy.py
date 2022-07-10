# A simple temperature converter
# Exercises in programming


def ftoc(temp):
    print("Converted temp is ", (temp - 32) * 5/9)

def ctof(temp):
    print("Converted temp is ", (temp * 9/5) + 32)


while True:
    menu = input("(F)ahrenheit to Celsius, (C)elsius to Fahrenheit or E(x)it ").lower()

    if menu == 'f':
        temp = input("Enter temperature to convert: ")
        ftoc(float(temp))
    elif menu == 'c':
        temp = input("Enter temperature to convert: ")
        ctof(float(temp))
    elif menu == 'x':
        break
    else:
        print("Invalid option.")

print("Thank you for using!")


