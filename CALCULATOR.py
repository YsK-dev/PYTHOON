import math

print(" --------------------------------","\nWelcome to my ultimate calculator\n"," -------------------------------")

firstNumber=int(input("What is first Number: "))
operration=int(input("What do you wanna do ı mean for instance\n"
                 "1 For addition\n"
                 "2 for extarction\n"
                 "3 for multiplication\n"
                 "4 for division\n"
                     "so what: "))
secondNumber=int(input("What is second number: "))



match operration:

    case 1 :
        sum= firstNumber+secondNumber
        print("Here's the summation",sum)

    case 2 :

        ext = firstNumber - secondNumber
        print("Here's the summation", ext)

    case 3:
        mlt = firstNumber ** secondNumber
        print("Here's the summation", mlt)

    case 4:
        div = firstNumber / secondNumber
        print("Here's the summation",div)

    case _:
        print("Beo where ıs operatıon amk")















