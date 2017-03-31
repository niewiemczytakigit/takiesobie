#!/usr/bin/python3

def liczba_slownie(liczba, suffix=None):
    liczba = str(liczba)
    liczba1 = list(liczba)
    liczba1.reverse()
    tysiace = ('tysiąc','tysiące','tysięcy')
    miliony = ('milion','miliony','milionów')
    miliardy = ('miliard','miliardy','miliardów')
    setki = ('sto','dwieście','trzysta','czterysta','pięćset','sześćset','siedemset','osiemset','dziewięćset')
    cyfry = ('zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć','dziesięć','jedenaście','dwanaście','trzynaście','czternaście','piętnaście','szesnaście','siedemnaście','osiemnaście','dziewiętnaście')
    dziesiatki = ('dziesięć','dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt','sześćdziesiąt','siedemdziesiąt','osiemdziesiąt','dziewięćdziesiąt')
    print('-'*100)
    print(liczba)
    print(liczba1)
    if suffix:

        slownie = [suffix]
    else:
        slownie = []
    for nr, cyfra in enumerate (liczba1):
        print('nr:', nr)
        print('cyfra:', cyfra)
        if nr%3 == 0:
            if nr == 3 and int (cyfra) != 1:#sprawdza czy tysiące
                if 1 < int (cyfra) < 5:
                    slownie.insert (0, tysiace[1])
                else:
                    slownie.insert (0, tysiace[2])
            elif nr == 6 and int (cyfra) != 1:#sprawdza czy miliony
                if 1 < int (cyfra) < 5:
                    slownie.insert (0, miliony[1])
                else:
                    slownie.insert (0, miliony[2])
            elif nr == 9 and int (cyfra) != 1:#sprawdza czy miliardy
                if 1 < int (cyfra) < 5:
                    slownie.insert (0, miliardy[1])
                else:
                    slownie.insert (0, miliardy[2])
            if nr+1 < len (liczba1): # Sprawdzam czy to ostatni cyfra
                if int (liczba1[nr+1]) > 1:#sprawdza czy liczba dziesiętna jest powyżej 20
                    slownie.insert (0, cyfry[int (cyfra)])#wpisuje pojedynczą cyfre
                else:# liczby poniżej 20
                    if int (cyfra) == 0:
                        continue
                    else:# liczby od 1 do 19
                        slownie.insert (0, cyfry[ int(liczba1 [nr+1]+ liczba1 [nr])])
            else:# jeśli to ostatnia cyfra
                if nr > 0 and int (cyfra) == 1:
                    if nr == 3:
                        slownie.insert (0, tysiace[0])
                    elif nr == 6:
                        slownie.insert (0, miliony[0])
                    elif nr == 9:
                        slownie.insert (0, miliardy[0])
                else:
                    slownie.insert (0, cyfry [int (cyfra)])
        elif nr%3 == 1: # reguły dla dziesiątek
            if int(cyfra) == 1 or int (cyfra) == 0:# dla cyfry 0 i 1 nie pisze nic (dla jedynki już wypisano przy poprzednim przebiegu)
                continue
            else: # wypisuje dziesiątki
                slownie.insert (0, dziesiatki[ int (cyfra)-2])
        elif nr%3 == 2:
            if int (cyfra) == 0:
                continue
            else: # wypisuje setki
                slownie.insert (0, setki[ int (cyfra)-1])
    # print("Słownie:", end=' ')
    # for i in slownie:
    #     print(i, end=' ')
    return ' '.join(slownie)



print("'%s'" % liczba_slownie(410))


testy = {
    'czterysta dwadzieścia': 420,
    'jedenaście': 11,
    'trzysta dziesięć': 310,
    'sto': 100
}

# assert liczba_slownie(100) == 'sto', 'Nie dało rady ze stówą'
# assert liczba_slownie(201) == 'dwieście jeden', 'Nie dało rady z 201'
# w = liczba_slownie(410)
# assert w == 'czterysta dziesięć', 'Nie dało rady: ' + w

for k in testy.keys():
    w = liczba_slownie(testy[k])
    if w != k:
        print('Błąd: {0} --> "{1}"'.format(testy[k], w))