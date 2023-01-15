import numpy as np

def max_min(poly):

    while poly[0] == 0:
        poly = poly[1:]

    if len(poly)%2 == 0:         
        return("-infinity","+infinity")        
    if len(poly) == 1:
        return(poly[0],poly[0])

    deriv = derivative(poly)
    potential_values = [value(poly,x) for x in roots(deriv)]   ### Finding roots of the derivative to determine potential max/min


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

def roots(poly):  ### Doesn't return imaginary roots
    return [i.real for i in np.roots(poly) if np.isreal(i)] 




