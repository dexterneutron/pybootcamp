"""Project: The objective is to write an interactive calculator.
 User input is assumed to be a formula that consists of a number,
  an operator (at least + and -), and another number, 
  separated by white space (e.g. 1 + 1). Split user input and check whether the resulting list is valid:
  If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
  Convert the first and third input to a float. Handle any ValueError 
  that occurs, and instead raise a FormulaError.
  If the second input is not '+' or '-', again raise a FormulaError.
  If the input is valid, perform the calculation and print out the result. 
  The user is then prompted to provide new input, and so on, until the user enters quit.
"""
class FormulaError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
while True:
    operation = input("Please, write a formula: \n")
    if operation == "quit":
        print("Program exited")
        break
    else:
        if "+" in operation:
            numbers_array = operation.split("+")
            if len(numbers_array) != 2:
                raise FormulaError("Invalid Number of Arguments")
            n1, n2 = numbers_array
            if (n1.strip().isnumeric() and n2.strip().isnumeric()):
                print(float(n1) + float(n2))
            else:
                raise FormulaError("Invalid Input")
        elif "-" in operation:
            numbers_array = operation.split("-")
            if len(numbers_array) != 2:
                raise FormulaError("Invalid Number of Arguments")
            n1, n2 = numbers_array
            if (n1.strip().isnumeric() and n2.strip().isnumeric(2)):
                print(float(n1.strip()) - float(n2.strip()))
            else:
                raise FormulaError("Invalid Input")
        else:
            raise FormulaError("Not an addition or substraction operation")
