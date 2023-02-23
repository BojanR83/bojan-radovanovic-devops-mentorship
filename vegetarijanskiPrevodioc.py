unos = input("Unesite željeni tekst: ")
samoglasnik = {'A':'Apa','a':'apa',
           'E':'Epe','e':'epe',
           'I':'Ipi','i':'ipi',
           'O':'Opo','o':'opo',
           'U':'Upu','u':'upu'}
prevod = ''
for slovo in unos:
    if slovo in samoglasnik:
        prevod += samoglasnik[slovo]
    else:
        prevod += slovo
print("Originalni tekst:              ", unos)
print("Prevod na Vegetarijanski :-) : ", prevod)