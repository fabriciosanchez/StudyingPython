#####################################################################################################################
#                                             SIMPLE TWO VALUES CALCULATOR                                          #
#####################################################################################################################
#Receiving the numbers to realize the account
try:
    number1 = input("Please, tell me a first number: ")
    number1 = int(number1)
    number2 = input("Please, tell me a second number: ")
    number2 = int(number2)
except ValueError:
    print("Sorry but, the informed values can't be converted. Nothing else will happen.")

#Receiving the operator
operator = input("Please, tell us the math operator: ")

#Verifies if a valid operator was sent
if operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Something went wrong. The program is being stoped.")
else:
    if number2 == 0 and operator == "/":
        print("Sorry but I can't process an division by zero. The program will be ended.")

#Calculating and printing final result on the screen
if operator == "+": result = number1 + number2
if operator == "-": result = number1 - number2
if operator == "*": result = number1 * number2
if operator == "/": result = number1 / number2

print("The result is: %.2f" %result)