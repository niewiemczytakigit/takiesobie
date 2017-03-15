#!/usr/bin/python3

liczba = 123

tekst = 'sto dwadzieścia trzy'

teksty = {
'0': '',
'100': 'sto',
'200': 'dwieście',
'20': 'dwadzieścia',
'3': 'trzy',
'5': 'pięć'
}


def zamiana(liczba):


    setki = int(liczba / 100)
    dzies = int((liczba - setki * 100) / 10)
    jedn = liczba - dzies * 10 - setki * 100
    return ' -- '.join(
        [
            teksty[str(setki*100)],
            teksty[str(dzies*10)],
            teksty[str(jedn)]
        ]
     )

print(zamiana(100))
print(zamiana(223))

#assert zamiana(200) == 'sto', "nie udało się"