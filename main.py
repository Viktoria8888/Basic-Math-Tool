from functions.parsing_string import *
from functions.polyconvert import *
from functions.polynomial_roots import *
from functions.global_min_max import *
import os

def clear():
	os.system('cls')
	os.system('clear')

def main_menu(): 
	funkcje = {"1":funkcja1,"0":clear,"2":funkcja2,"3":funkcja3,"4":funkcja4}
	clear()
	print("Which program would you like to run?\n")
	print("[1] Convert a factored polynomial to an expanded polynomial\n[2] Generate graphs of polynomials in a specified range\n[3] Determine the maximum and minimum global values\n[4] Find polynomial roots in expanded form within a given range and specified approximation\n[0] Exit")
	user_input = input("\nEnter the number: ").replace(" ","")
	if user_input in funkcje:
		return funkcje[user_input]()
	return main_menu()

def sub_menu(f):
	temp_dict = {"1": main_menu, "2":f, "0":clear}
	while True:
		print("[1] Main menu\n[2] Use the function again\n[0] Exit\n")
		choice = input("Enter the number: ").replace(" ","")
		if choice in temp_dict:
			break
		else:
			clear()
	return temp_dict[choice]()

def	funkcja1():
	clear()
	try:
		n = float(input("Enter the number of polynomial roots: "))
		if n <= 0 or n != int(n):
			return funkcja1()
		n = int(n)
	except:
		return funkcja1()
	roots = []
	while n>0:
		usr_root = input("Enter the root: ")
		try:
			float(usr_root)
			roots.append(float(usr_root))
			n -= 1
		except:
			print("Incorrect input")
	clear()
	print(f"Basing on the roots, the expanded polynomial is:\n{[round(i,5) for i in polyconvert(roots)]}\n")
	return sub_menu(funkcja1)

def funkcja2():
	clear()
	try:
		exec(open("functions/graph.py").read(), globals())
	except:
		return funkcja2()
	return sub_menu(funkcja2)

def funkcja3(n=0):
	clear()
	print("Individual monomials should be sorted in descending order; from the highest exponent to the lowest. The '^' character should be used as a power symbol.\nCorrect input: '2x^4-3', 'x^7-x^2+2', 'x^5+x^3-x+9'\n")
	if n == 1:
		print("Incorrect input")
	poly = input("Enter the polynomial:\n")
	pars = parsing_string(poly)
	if pars[0] == "błąd parsowania":
		return funkcja3(1)
	mini_maxi = max_min(pars[1])
	clear()
	print(f"{poly}\nGlobal minimum: {mini_maxi[0]} | Global maximum: {mini_maxi[1]}\n")
	return sub_menu(funkcja3)

def funkcja4(n=0):
	clear()
	print("Individual monomials should be sorted in descending order; from the highest exponent to the lowest. The '^' character should be used as a power symbol. \nCorrect input: '2x^4-3', 'x^7-x^2+2', 'x^5+x^3-x+9'\n")
	if n==1:
		print("Incorrect input")
	poly = input("Enter the polynomial:\n")
	if parsing_string(poly)[0] == "błąd parsowania":
		return funkcja4(1)
	pars = parsing_string(poly)[1]
	clear()
	while True:
		print("Enter the range you would like to search for roots in.\n")
		bot = input("Bottom endpoint of the range: ")
		top = input("Top endpoint of the range: ")
		try:
			bot, top = float(bot), float(top)
			break
		except:
			clear()
			print("Incorrect input")
	if top < bot:
		bot,top = top,bot
	clear()
	while True:
		approx = input("Enter the approximation: ")
		try:
			approx = float(approx)
			clear()
			print(f'{poly}\nRoots: {miejsca_zerowe(pars, bot, top, approx)}\n')
			break
		except:
			clear()
			print("Incorrect input")
	sub_menu(funkcja4)

main_menu()
