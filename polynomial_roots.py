
def zero(wielomian,x): # funkcja pomocniczna zwracajaca wartosc wielomianu w punkcie x
    wart = 0
    for i in range(len(wielomian)):
        wart = wart + (wielomian[i] * (x ** (len(wielomian) - 1 - i)))
    return wart

def miejsca_zerowe(wielomian,od,do,dokladnosc):
    epsilon = 0.000001 # przyblizenie bledu wynikacja z niedokladnej reprezentacji niektorych ulamkow
    wynik = [] # tablica przechowujaca wszystkie przyblizone wartosci pierwiastkow wielomianu
    koncowywynik = [] # tablia zawierajaca po jednym przyblizonym wyniku odpowiadajacym jednemu pierwiastkowi

    while(od<=do): # przegladanie liczb od , od +dokladnosc, od + 2*dokladnosc ...od + n*dokladnosc gdzie (od + n*dokladnosc) najmniejsze takie ze (od + n*dokladnosc)>do jako kandydatow na pierwiastki wielomianu
        if abs(zero(wielomian,od))<epsilon:
            wynik.append(od)
        od = od + dokladnosc

    for i in range(1,len(wynik)): # odfiltrowanie wynikow rozniacych sie od siebie o okreslone przyblizenie
        if abs(wynik[i] - wynik[i-1])>epsilon:
            koncowywynik.append(wynik[i-1])

    if abs(wynik[len(wynik)-1] - wynik[len(wynik)-2]) > epsilon: # przypadek w ktorym ostatnia liczba w talicy wynik bedzie dobrym pierwiastkiem
        koncowywynik.append(wynik[len(wynik)-1])

    return koncowywynik


w = [1,-3,-29,3,28,0] # dane testowe
k = [1,-2,-1,2] # dane testowe
t = [1,0,-4] # dane testowe

print((miejsca_zerowe(k,-8,8,0.00001)))


