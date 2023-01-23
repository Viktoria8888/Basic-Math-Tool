## Polynomials
### To make the program work correctly make sure to do:
```
pip install matplotlib
pip install numpy
```
The program takes different arguments depending on chosen function in the terminal:

 1) Converts a factored polynomial to an expanded polynomial. Function takes a list containing polynomial roots and returns a list containing polynomial coefficients.
 There are many polynomials with the same roots. However, this function returns one of them, 
 more specifically, one that has the first coefficient equal to 1.

 2) Generates a graph of a polynomial in a specified range based on user input from GUI.  

 3) Determines the maximum and minimum global values (rounded to 3 decimal places).

 4) Returns all the polynomial roots in expanded form within a given range and with a given approximation.

 5) Operates as a function that parses a string, given as a parameter, as a polynomial in one of the representations and returns a pair of one of three forms:
 - ("współczynnikowa", lista),
 - ("pierwiastkowa", lista), or
 - ("błąd parsowania", [])
 where lista represents the given polynomial in the given way.
 The string given as a parameter should be in the form of monomials in descending order of the degree of the monomial, or parentheses raised to a certain power. 
 The ^ character should be used as a power symbol.
 For example:
 - correct input: '(x-7)x^3(x+2)^3(x+6)^2', '2x^6-x^4+13x^3+278x^2+9'
 - incorrect input: '(2x-3)(x-1)', 'x^7 -(x+2)', '(x-1)(x+9) ^4'
 For monomials of the form x raised to a certain power, the function returns the factored representation. 
 For example, for input 'x^3' the function returns ("współczynnikowa", [0, 0, 0]) rather than ("pierwiastkowa", [1, 0, 0, 0]).
