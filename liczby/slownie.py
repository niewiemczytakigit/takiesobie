#!/usr/bin/python3

JEDNOSCI = ['Zero', 'Jeden', 'Dwa', 'Trzy', 'Cztery', 'Pięć', 'Sześć', 'Siedem', 'Osiem', 'Dziewięć']
NASTKI = ['Dziesięć', 'Jedenaście', 'Dwanaście', 'Trzynaście', 'Czternaście', 'Piętnaście', 'Szesnaście', 'Siedemnaście', 'Osiemnaście', 'Dziewiętnaście']
DZIESIATKI = ['', 'Dziesięć', 'Dwadzieścia', 'Trzydzieści', 'Czterdzieści', 'Pięćdziesiąt', 'Sześćdziesiąt', 'Siedemdziesiąt', 'Osiemdziesiąt', 'Dziewięćdziesiąt']
SETKI = ['Sto', 'Dwieście', 'Trzysta', 'Czterysta', 'Pięćset', 'Sześćset', 'Siedemset', 'Osiemset', 'Dziewięćset']

POZIOMY = [
    None,
    ('Tysiąc', 'Tysiące', 'Tysięcy'),
    ('Milion', 'Miliony', 'Milionów'),
    ('Miliard', 'Miliardy', 'Miliardów'),
    ('Bilion', 'Biliony', 'Bilionów'),
    ('Biliard', 'Biliardy', 'Biliardów'),
    ]

def po_trzy(napis):
    poczatek = len(napis) % 3
    if not poczatek:
        poczatek = 3
    poziom = (len(napis) - 1) // 3

    yield int(napis[0:poczatek]), poziom

    while poziom > 0:
        poziom -= 1
        yield int(napis[poczatek:poczatek + 3]), poziom
        poczatek += 3

def slownie(wartosc):
    # Jeżeli podano liczbę
    if isinstance(wartosc, int):
        napis = str(wartosc)
    # Jeżeli podano napis (wg mnie funkcja powinna przyjmować jedynie liczby)
    elif isinstance(wartosc, str):
        # Spróbuj zamienić na liczbę
        try:
            wartosc = int(wartosc)
        except ValueError:
            return 'Nieprawidłowa wartość'
        finally:
            napis = str(wartosc)
    else:
        return 'Nieprawidłowa wartość'

    if napis == '0':
        return 'Zero'

    bufor = []

    if napis.lstrip().startswith('-'):
        bufor.append('Minus')
        napis = napis[1:]

    for liczba, poziom in po_trzy(napis):
        if not liczba:
            continue
        if liczba < 10:
            bufor.append( JEDNOSCI[liczba] )
            if poziom:
                if liczba == 1:
                    bufor.append( POZIOMY[poziom][0] )
                elif liczba < 5:
                    bufor.append( POZIOMY[poziom][1] )
                else:
                    bufor.append( POZIOMY[poziom][2] )

        elif liczba < 20:
            bufor.append( NASTKI[liczba - 10] )
            if poziom:
                bufor.append( POZIOMY[poziom][2] )

        elif liczba < 100:
            bufor.append( DZIESIATKI[liczba // 10] )
            reszta = liczba % 10
            if reszta:
                bufor.append( JEDNOSCI[reszta] )
            if poziom:
                if reszta in [2, 3, 4]:
                    bufor.append( POZIOMY[poziom][1] )
                else:
                    bufor.append( POZIOMY[poziom][2] )

        else:
            bufor.append( SETKI[liczba // 100 - 1] )
            reszta = liczba % 100
            if reszta:
                bufor.append( DZIESIATKI[reszta // 10] )
                jednosci = reszta % 10
                if jednosci:
                    bufor.append( JEDNOSCI[jednosci] )
                    if jednosci in [2, 3, 4] and poziom:
                        bufor.append( POZIOMY[poziom][1] )
                        continue
            if poziom:
                bufor.append( POZIOMY[poziom][2] )

    if len(bufor) == 1:
        return bufor[0]
    else:
        return ' '.join(bufor)


if __name__ == "__main__":
    # Testy
    dane_testowe = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
        '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
        '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
        '1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000',
        '1234', '1001', '1010', '1011', '1100', '1101', '1110', '1111',
        '10000', '11000', '12000', '13000', '14000', '15000', '16000', '17000', '18000', '19000',
        '20000', '21000', '22000', '23000', '24000', '25000', '26000', '27000', '28000', '29000',
        '30000', '31000', '32000', '33000', '34000', '35000', '36000', '37000', '38000', '39000',
        '1000000',
        '123456789',
        '123456789123',
        '123456789123456',
        '0000000000000000', '000000000000000001', '00001234',
        '9'*63,
        '100' + '0'*60,
        '1' + '001'*20,

        310, '', '   ', ['abc'], (1,2,3), None,
        3.1415, '   23  ', '-100'
    ]

    for wejscie in dane_testowe:
            print("%s %s" % (wejscie, slownie(wejscie)))
