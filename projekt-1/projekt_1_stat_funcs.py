#!/usr/bin/python

"""
modul s funkcemi pro zpracování textu v projekt_1.py 

autor:    Daniel Mazur
e-mail:   daniel.mazur.cz@gmail.com
discord:  daniel_67828

"""

def wcountLowercase(wlist):
    # counts lowercase words in word list 'wlist'
    c = 0
    for w in wlist: 
        if w.islower():
            c += 1
        # endif
    # endfor
    return c
# enddef

def wcountUppercase(wlist):
    # counts uppercase words in word list 'wlist'
    c = 0
    for w in wlist: 
        if w.isupper():
            c += 1
        # endif
    # endfor
    return c
# enddef

wsum = 0.0

def wcountNumeric(wlist):
    # counts numeric words (i.e. numbers) in word list 'wlist' and sums them up in a global var
    global wsum
    wsum = 0.0   # nutné resetovat před každou další kompletní analýzou
    c = 0
    for w in wlist: 
        if w.isdigit():
            c += 1
            wsum += float(w)
        # endif
    # endfor
    return c
# enddef

def wcountNames(wlist):
    # counts names (i.e. words with capital first letter and NOT all-caps) in word list 'wlist'
    c = 0
    for w in wlist: 
        if w.isalpha() and w[0].isupper():
            c += 1
        # endif
    # endfor
    return c
# enddef

def wsumNumeric():
    global wsum
    return wsum # funguje dobře, pokud je předtím zavolaná fce wcountNumeric()
# enddef

def getCharcountHistogram(wlist):
    # counts characters in every word in word list 'wlist', fills histogram list of int and
    # transforms this list into multiline str sout, eg.
    # '''
    # 7| * 1
    # 8| *********** 11
    # 9| *************** 15
    # 10| ********* 9
    # 11| ********** 10
    # '''

    c = 0
    #longest = 0
    lhist = []
    for w in wlist: 
        
        if len(lhist) <= len(w):
            for ii in range(len(lhist),len(w)+1): # prodlužujeme histogram, aby se vešel zápočet aktuálně nejdelšího slova
                lhist.append(0)
            #endfor
        # endif
        lhist[len(w)] += 1
    # endfor

    # najdi nejvyšší hodnotu v histogramu, potřebujeme ji pro graf. alignment
    hmax = 0
    for x in lhist:
        if x > hmax:
            hmax = x
        # endif
    # endfor
    # hmax obsahuje nejvyšší hodnotu histogramu
    if hmax <= 8:
        just = 10
    elif (hmax % 2) > 0:    # zarovnání just chci mít sudou hodnotu
        just = hmax + 3
    else:
        just = hmax + 2
    # endif

    sout = str()
    c = 0
    trig = False
    for x in lhist:
        if trig:
            sout += str(c).rjust(3,' ')+'|'
            stars = ""
            if x > 0:
                stars = ('*' * x) # nevím, jestli to funguje pro x==0, proto ten 'if'
            #endif
            sout += stars.ljust(just,' ')+'|'+str(x) 
        else:
            if x > 0: # toto je pro první nenulovou položku histogramu
                trig = True
                sout = str(c).rjust(3,' ')+'|'
                stars = ('*' * x)
                sout += stars.ljust(just,' ')+'|'+str(x)
            # endif
        #endif
        c += 1
        sout += '\n'
        #if c < len(lhist):
        #    sout += '\n'
        #endif
    # endfor
    
    # sout ještě třeba doplnit 'hlavičkou tabulky' ve tvaru
    #----------------------------------------
    #LEN| OCCURENCES |NR.
    #----------------------------------------
    hdr = "-" * 40
    hdr += '\n'
    if hmax <= 8:
        hdr += "LEN|OCCURENCES|NR."
    else:
        hdr += "LEN|"
        occ = "OCCURENCES".rjust(int((just+10)/2),' ').ljust(int(just),' ') # symetrické odsazení, když len("OCCURENCES")==10
        hdr += occ
        hdr += "|NR.\n"
    hdr += "-" * 40
    hdr += '\n'
    sout = hdr+sout
    sout += "-" * 40
    sout += '\n\n'

    return sout
# enddef

# t = 'modul s funkcemi pro zpracování textu v projekt_1.py '
# wl = t.split()
# print(*wl, sep= '\n')

#print(str(wcountLowercase(wl)))

# c = 0
# for w in wl: 
#     if w.islower():
#         c += 1
#     # endif
# # endfor

# print(c)
# print(str(wcountLowercase(wl)))











#end