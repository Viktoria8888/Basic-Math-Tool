def polyconvert(poly):
    if len(poly) == 1:
        return [1, -poly[0]]
    res = []
    help = []
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
 