def aux(tekst):
    lista_wyrazow = []
    wyraz = ''
    if '(' in tekst:
        i = 0
        otwarte = 0
        while i < len(tekst):
            if tekst[i] == '(':
                if wyraz != '':
                    lista_wyrazow.append(wyraz)
                wyraz = '('
                otwarte += 1
            elif tekst[i] == ')':
                wyraz += ')'
                if i < len(tekst) - 1:
                    if tekst[i+1] =='x':
                        lista_wyrazow.append(wyraz)
                        i += 1
                        wyraz = tekst[i]
                        i += 1
                        continue
                    if tekst[i+1] == '^':
                        i += 1
                        wyraz += tekst[i]
                        i += 1
                        while i < len(tekst):
                            if tekst[i] == 'x':
                                lista_wyrazow.append(wyraz)
                                wyraz = 'x'
                                break
                            elif tekst[i] == '(':
                                lista_wyrazow.append(wyraz)
                                wyraz = '('
                                break
                            wyraz += tekst[i]
                            i += 1
                else:
                    lista_wyrazow.append(wyraz)
                    wyraz = ''
                    otwarte -= 1
            else:
                wyraz += tekst[i]
            i += 1
        lista_wyrazow.append(wyraz)
        return ' '.join(lista_wyrazow)
    else:
        i = 0
        while i < len(tekst):
            if tekst[i] in ['+', '-']:
                lista_wyrazow.append(wyraz)
                wyraz = tekst[i]
                i += 1
                continue
            wyraz += tekst[i]
            i += 1
        lista_wyrazow.append(wyraz)
        return ' '.join(lista_wyrazow)
    

def parsing_string(tekst):
    if tekst == '0':
        return ('pierwiastkowo', [0])
    tekst = aux(tekst)
    wspolczynnikowo = False
    pierwiastkowo = False
    lista = []
    tekst = tekst.strip()
    lista_tekst = tekst.split()
    indeks_lista = 0
    potega_poprzednia = -2
    for element in lista_tekst:
        if indeks_lista == 0 and element[0] == '+':
            return ('błąd parsowania', [])

        elif element[0] in ['+', '-'] + [str(i) for i in range(1, 9)]:
            wspolczynnikowo = True
            i = 0
            liczba = ''
            if element[0] in ['+', '-']:
                if element[0] == '-':
                    liczba = '-'
                i = 1
            while i < len(element) and element[i] != 'x':
                liczba += element[i]
                i += 1

            if liczba == '':
                liczba = '1'
            elif liczba == '-':
                liczba = '-1'

            try:
                liczba_int = int(liczba)
            except:
                return ('błąd parsowania', [])

            if i == len(element):
                potega_obecna = 0
                if potega_poprzednia != -2:
                    if potega_obecna >= potega_poprzednia:
                        return ('błąd parsowania', [])
                    while potega_obecna != potega_poprzednia - 1:
                        lista.append(0)
                        potega_poprzednia -= 1
                    potega_poprzednia = 0
                    lista.append(liczba_int)
                else:
                    potega_poprzednia = 0
                    lista.append(liczba_int)

            elif element[i] == 'x':
                if i == len(element) - 1:
                    potega_obecna = 1
                    if potega_poprzednia != -2:
                        if potega_obecna >= potega_poprzednia:
                            return ('błąd parsowania', [])
                        while potega_obecna != potega_poprzednia - 1:
                            lista.append(0)
                            potega_poprzednia -= 1
                        potega_poprzednia = 1
                        lista.append(liczba_int)
                    else:
                        potega_poprzednia = 1
                        lista.append(liczba_int)
                elif i == len(element) - 2:
                    return ('błąd parsowania', [])
                else:
                    i += 1
                    if element[i] == '^':
                        liczba_pot = element[i+1:]
                        try:
                            liczba_pot_int = int(liczba_pot)
                        except:
                            return ('błąd parsowania', [])

                        potega_obecna = liczba_pot_int
                        if potega_poprzednia != -2:
                            if potega_obecna >= potega_poprzednia:
                                return ('błąd parsowania', [])
                            while potega_obecna != potega_poprzednia - 1:
                                lista.append(0)
                                potega_poprzednia -= 1
                            potega_poprzednia = potega_obecna
                            lista.append(liczba_int)
                        else:
                            potega_poprzednia = potega_obecna
                            lista.append(liczba_int)


                    else:
                        return ('błąd parsowania', [])

            else:
                return ('błąd parsowania', [])

        elif element[0] == 'x':
            if len(lista_tekst) == 1:
                if len(element) == 1:
                    return ('pierwiastkowo', [0])
                if len(element) == 2:
                    return ('błąd parsowania', [])
                if element[1] == '^':
                    liczba = element[2:]
                    try:
                        liczba_int = int(liczba)
                    except:
                        return ('błąd parsowania', [])
                    for i in range(liczba_int):
                        lista.append(0)
                    return ('pierwiastkowo', lista)
                else:
                    return ('błąd parsowania', [])

            elif (lista_tekst[1][0] in ['+', '-']) and indeks_lista == 0:
                wspolczynnikowo = True

                if len(element) == 1:
                    lista.append(1)
                    potega_poprzednia = 1
                elif len(element) == 2:
                    return ('błąd parsowania', [])
                elif element[1] == '^':
                    liczba = element[2:]
                    try:
                        liczba_int = int(liczba)
                    except:
                        return ('błąd parsowania', [])
                    lista.append(1)
                    potega_poprzednia = liczba_int
                else:
                    return ('błąd parsowania', [])

            elif lista_tekst[1][0] == '(' and indeks_lista == 0:
                if len(element) == 1:
                    lista.append(0)
                elif len(element) == 2:
                    return ('błąd parsowania', [])
                elif element[1] == '^':
                    liczba = element[2:]
                    try:
                        liczba_int = int(liczba)
                    except:
                        return ('błąd parsowania', [])
                    for i in range(liczba_int):
                        lista.append(0)
                else:
                    return ('błąd parsowania', [])

            if indeks_lista != 0 and wspolczynnikowo:
                return ('błąd parsowania', [])

            if indeks_lista != 0:
                pierwiastkowo = True

                if len(element) == 1:
                    lista.append(0)
                if len(element) == 2:
                    return ('błąd parsowania', [])
                if element[1] == '^':
                    liczba = element[2:]
                    try:
                        liczba_int = int(liczba)
                    except:
                        return ('błąd parsowania', [])
                    for i in range(liczba_int):
                        lista.append(0)
                else:
                    return ('błąd parsowania', [])
                    
            elif len(element) == 2:
            	return ('błąd parsowania', [])

        elif element[0] == '(':
            pierwiastkowo = True
            if element == '(x)':
                lista.append(0)
                continue
            if len(element) < 5:
                return ('błąd parsowania', [])
            if element[1] != 'x':
                return ('błąd parsowania', [])
            if element[2] not in ['+', '-']:
                return ('błąd parsowania', [])
            liczba = ''
            if element[2] == '+':
                liczba = '-'
            if element[-1] == ')':
                liczba += element[3:-1]
                try:
                    liczba_int = int(liczba)
                except:
                    return ('błąd parsowania', [])
                lista.append(liczba_int)
            else:
                if ')' not in element or element[3] not in [str(j) for j in range(1, 9)]:
                    return ('błąd parsowania', [])
                i = 3
                while element[i] != ')':
                    liczba += element[i]
                    i += 1
                try:
                    liczba_int = int(liczba)
                except:
                    return ('błąd parsowania', [])
                if i == len(element) - 1:
                    return ('błąd parsowania', [])
                i += 1
                if element[i] == '^':
                    liczba_pot = element[i+1:]
                    try:
                        liczba_pot_int = int(liczba_pot)
                    except:
                        return ('błąd parsowania', [])
                    for i in range(liczba_pot_int):
                        lista.append(liczba_int)
                else:
                    return ('błąd parsowania', [])

        else:
            return ('błąd parsowania', [])

        if wspolczynnikowo and pierwiastkowo:
            return ('błąd parsowania', [])

        indeks_lista += 1

    if potega_poprzednia > 0:
        while potega_poprzednia != 0:
            lista.append(0)
            potega_poprzednia -= 1

    if wspolczynnikowo:
        return ('współczynnikowo', lista)
    elif pierwiastkowo:
        return ('pierwiastkowo', lista)
