from parsing_string import *
from polyconvert import *
from polynomial_roots import *
from global_min_max import *
import os

os.system('cls')
os.system('clear')
leave_check = 1
while leave_check != 0:
    print("Hello,\nWhich function would you like to run?\n")
    print("1. Convert a factored polynomial to an expanded polynomial.\n2. Generate a graph of a polynomial in a specified range.\n3. Determine the maximum and minimum global values.\n4. Return all the polynomial roots in expanded form within a given range and with a given approximation.\n")
    user_input = input("Type number of function(or type 0 if you want to exit):\n")
    user_input = user_input.replace(" ", "")
    user_input = user_input.replace(".", "")
    if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "0":
        input_check = False
        while input_check == False:
            os.system('cls')
            os.system('clear')
            print("Hello,\nWhich function would you like to run?")
            print("1. Convert a factored polynomial to an expanded polynomial.\n2. Generate a graph of a polynomial in a specified range.\n3. Determine the maximum and minimum global values.\n4. Return all the polynomial roots in expanded form within a given range and with a given approximation.\n")

            user_input = input("Wrong input! Type function number again(or type 0 if you want to exit).\n")
            user_input = user_input.replace(" ", "")
            user_input = user_input.replace(".", "")
            if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "0":
                input_check = False
            else:
                input_check = True

    os.system('cls')
    os.system('clear')

    if user_input == "1":
        n = int(input("Type a number of polynomial roots.\n"))
        roots = []
        for i in range(0,n):
            num_check = False
            dot_ind = 0
            user_arg = input("Type polynomial root:\n")
            if user_arg.isnumeric() == True or (user_arg[0] == "-" and      user_arg[1:].isnumeric() == True):
                    roots.append(int(user_arg))
                    num_check = True
            elif (user_arg[0].isnumeric() or user_arg[0] == "-") and user_arg.count(".") == 1:
                    dot_ind = 0
                    for i in range(0,len(user_arg)-1):
                        if user_arg[i] == ".":
                            dot_ind = i
                            break
                    if user_arg[(dot_ind + 1):].isnumeric() == True:
                        roots.append(float(user_arg))
                        num_check = True

            while num_check == False:
                user_arg = input("Wrong! Type Root again:\n")
                if user_arg.isnumeric() == True or (user_arg[0] == "-" and      user_arg[1:].isnumeric() == True):
                    roots.append(int(user_arg))
                    num_check = True
                elif (user_arg[0].isnumeric() or user_arg[0] == "-") and user_arg.count(".") == 1:
                    dot_ind = 0
                    for i in range(0,len(user_arg)-1):
                        if user_arg[i] == ".":
                            dot_ind = i
                            break
                    if user_arg[(dot_ind + 1):].isnumeric() == True:
                        roots.append(float(user_arg))
                        num_check = True
        os.system('cls')
        os.system('clear')
        print("Based on your roots, expanded polynomial is:\n",polyconvert(roots))
        continue_check = input("\nIf you want to exit type 0, otherwise type any sign: ")
        if continue_check == "0":
            break
        os.system('cls')
        os.system('clear')
        
    elif user_input == "2":
        exec(open("graph.py").read())
        continue_check = input("\nIf you want to exit type 0, otherwise type any sign: ")
        if continue_check == "0":
            break
        os.system('cls')
        os.system('clear')

    elif user_input == "3":
        print("Polynomial should be in the form of space-separated monomials in descending order of the degree of the monomial, or parentheses raised to a certain power separated by a space. The ^ character should be used as a power symbol. For example:\n\nCorrect input: '(x-7) x^3 (x+2)^3 (x+6)^2', '2x^6 -x^4 +13x^3 +278x^2 +9'\nIncorrect input: '2x-3', 'x^7 -(x+2)', '(x-1)(x+9)'\n")
        poly = input("Type polynomial:\n")
        if parsing_string(poly)[0] == "błąd parsowania":
            check = False
        else:
            check = True
        while check == False:
            os.system('cls')
            os.system('clear')
            print("Polynomial should be in the form of space-separated monomials in descending order of the degree of the monomial. The ^ character should be used as a power symbol. For example:\n\nCorrect input: '2x^6 -x^4 +13x^3 +278x^2 +9'\nIncorrect input: '2x-3', 'x^7 -(x+2)', '(x-1)(x+9)'\n")
            poly = input("Incorrect input. Type polynomial again:\n")
            if parsing_string(poly)[0] == "błąd parsowania":
                check = False
            else:
                check = True
        os.system('cls')
        os.system('clear')
        polynomial = parsing_string(poly)[1]
        print(f"Minimum and maximum global values are: {max_min(poly)}")
        continue_check = input("\nIf you want to exit type 0, otherwise type any sign: ")
        if continue_check == "0":
            break
        os.system('cls')
        os.system('clear')

    elif user_input == "4":
        print("Polynomial should be in the form of space-separated monomials in descending order of the degree of the monomial, or parentheses raised to a certain power separated by a space. The ^ character should be used as a power symbol. For example:\n\nCorrect input: '(x-7) x^3 (x+2)^3 (x+6)^2', '2x^6 -x^4 +13x^3 +278x^2 +9'\nIncorrect input: '2x-3', 'x^7 -(x+2)', '(x-1)(x+9)'\n")
        poly = input("Type polynomial:\n")
        if parsing_string(poly)[0] == "błąd parsowania":
            check = False
        else:
            check = True
        while check == False:
            os.system('cls')
            os.system('clear')
            print("Polynomial should be in the form of space-separated monomials in descending order of the degree of the monomial. The ^ character should be used as a power symbol. For example:\n\nCorrect input: '2x^6 -x^4 +13x^3 +278x^2 +9'\nIncorrect input: '2x-3', 'x^7 -(x+2)', '(x-1)(x+9)'\n")
            poly = input("Incorrect input. Type polynomial again:\n")
            if parsing_string(poly)[0] == "błąd parsowania":
                check = False
            else:
                check = True
        poly = parsing_string(poly)[1]
        os.system('cls')
        os.system('clear')
        print("Tell me what range would you like to have.\n\n")
        range_from = int(input("From: "))
        range_to = int(input("To: "))
        os.system('cls')
        os.system('clear')
        print("Tell me what approximation would you like to have.\n\n")
        approx = float(input("Approximation: "))
        os.system('cls')
        os.system('clear')

        print(f"Roots: {miejsca_zerowe(poly, range_from, range_to, approx)}")
        continue_check = input("\nIf you want to exit type 0, otherwise type any sign: ")
        if continue_check == "0":
            break
        os.system('cls')
        os.system('clear')
    elif user_input == "0":
        leave_check = 0





