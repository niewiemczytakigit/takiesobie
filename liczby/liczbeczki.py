#!/usr/bin/python3

print "program generujący: \"słownie\""
liczba = raw_input ("Wprowadź liczbę: ")
liczba1 = list (liczba)
liczba1.reverse ()
tysiace = ('tysiąc','tysiące','tysięcy')
miliony = ('milion','miliony','milionów')
miliardy = ('miliard','miliardy','miliardów')
setki = ('sto','dwieście','trzysta','czterysta','pięćset','sześćset','siedemset','osiemset','dziewięćset')
cyfry = ('zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć','dziesięć','jedenaście','dwanaście','trzynaście','czternaście','piętnaście','szesnaście','siedemnaście','osiemnaście','dziewiętnaście')
dziesiatki = ('dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt','sześćdziesiąt','siedemdziesiąt','osiemdziesiąt','dziewięćdziesiąt')
slownie = ["zł"]
for nr, cyfra in enumerate (liczba1):
    if nr == 0 or nr == 3 or nr == 6 or nr == 9:
    if nr in (0, 3, 6, 9):
    if nr%3 == 0: