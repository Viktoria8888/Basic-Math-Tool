import numpy as np

def max_min(poly):

    while poly[0] == 0:
        poly = poly[1:]

    if len(poly)%2 == 0:         
        return("-infinity","+infinity")        
    if len(poly) == 1:
        return(poly[0],poly[0])

    deriv_roots = roots(derivative(poly)) ### Finding roots of the derivative to determine potential max/min
    potential_values = [value(poly,x) for x in deriv_roots] 


    if poly[0]<0:
        return("-infinity",max(potential_values))
    return(min(potential_values),"+infinity")


def value(poly,x): ### Returns the polynomial's value for a given x
    res = 0
    for i in range(len(poly)):
        res += poly[i]*(x**(len(poly)-i-1))
    return res
    
def derivative(poly):  
    degree = len(poly)-1
    res = []
    for i in range(degree):
        res.append(poly[i]*(degree-i))
    return res

def roots(poly):  ### Returns polynomial's roots, doesnt return imaginary
    return [i.real for i in np.roots(poly) if np.isreal(i)] 
    

### test ###

a = [0,1,6,3]
b = [-4,2,-6,1]
c = [1]
d = [5,3,1]

for i in (a,b,c,d):
    extremes = max_min(i) 
    print(f"Minimum: {extremes[0]}   Maksimum: {extremes[1]}\n")

