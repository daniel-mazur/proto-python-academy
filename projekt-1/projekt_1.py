#!/usr/bin/python

"""
projekt_1.py:

autor:    Daniel Mazur
e-mail:   daniel.mazur.cz@gmail.com
discord:  daniel_67828

"""
import task_template
# print(len(task_template.TEXTS))
from projekt_1_stat_funcs import wcountLowercase, wcountUppercase
from projekt_1_stat_funcs import wcountNumeric, wsum, wcountNames
from projekt_1_stat_funcs import wsumNumeric, getCharcountHistogram

#projekt_1_stat_funcs.wsum

# blok autorizace přístupu
iddb = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

while True:
    mid = input("Zadej uživatelské jméno> ")
    mpw = input("Zadej heslo> ")
    if mpw == iddb.get(mid):
        break
    else:
        print("....Nesprávné už. jméno nebo heslo.")
#end-while

print("Vítej v programu Textový analyzátor!")
print("")
print("Báze TEXTS obsahuje "+str(len(task_template.TEXTS))+" texty.")
print("Vybírejte mezi nimi indexy, tj. 0 až "+str(len(task_template.TEXTS)-1)+".")
print("Pozor: Výběrem jiné hodnoty program skončí.")
print("")

num = 0

while True:
    # výběr textu pro analýzu
    ind = input("Vyberte text ze seznamu>  ")
    if not(ind.isnumeric()):
        print("")
        print("... Vybraná jiná než číselná hodnota, program teď skončí.")

        break
    elif not int(ind) in range(0,len(task_template.TEXTS)):        
        print("")
        print("... Vybraná číselná hodnota je mimo rozsah, program teď skončí.")
        break
    else:
        # text vybraný, můžeme s ním pracovat
        wtx = task_template.TEXTS[int(ind)]
        print("*" * 30)
        print("Vybrán text:")
        print("*" * 30)
        print(wtx)
        print("*" * 30)
        # máme na výběr z několika postupů:
        #    https://www.geeksforgeeks.org/iterate-over-words-of-a-string-in-python/
        # začneme tím, který NEpotřebuje regex
        wlist = wtx.split()
        print("")
        print("TEXT STATS:")
        print("")
        print("1. Počet slov: ".ljust(48,' ')+str(len(wlist)).rjust(6,' ')+" *")
        print("2. Počet slov začínajících Velkým písmenem: ".ljust(48,' ')+str(wcountNames(wlist)).rjust(6,' ')+" *")
        print("3. Počet slov psaných VELKÝM písmem: ".ljust(48,' ')+str(wcountUppercase(wlist)).rjust(6,' ')+" *")
        print("4. Počet slov psaných malým písmem: ".ljust(48,' ')+str(wcountLowercase(wlist)).rjust(6,' ')+" *")
        print("5. Počet čísel (ne cifer): ".ljust(48,' ')+str(wcountNumeric(wlist)).rjust(6,' ')+" *")
        print("6. Suma všech čísel (ne cifer) v textu: ".ljust(48,' ')+str(int(wsumNumeric())).rjust(6,' ')+" *")
        print("*" * 56)
        print("Histogram délek slov v textu:")
        print("")
        print(getCharcountHistogram(wlist))

#end-while



















#---------------------------------------------------------
