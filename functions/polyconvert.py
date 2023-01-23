'''Function takes a list containing polynomial roots and returns a list containing polynomial coefficients.
There are many polynomials with the same roots. However, this function returns one of them, 
more specifically, one that has the first coefficient equal to 1'''
def polyconvert(poly):
    if len(poly) == 0:
        return
    if len(poly) == 1:
        return [1, -poly[0]]
    res = []
    help = []
    #Special code for quadratic polynomials. Higher degree polynomials are counted based on this.
    res.append(1)
    res.append(-(poly[0]+poly[1])) 
    res.append(poly[0]*poly[1])
    help[:] = res[:]


    for i in range(2,len(poly)):
        res.append(-poly[i]*res[-1])
        for j in range(1,len(res)-1):
            res[j] = res[j] + (-poly[i] * help[j-1])
        help[:] = res[:]
    return res
