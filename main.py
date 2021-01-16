"""
nome = "Luca"
testo = "il mio nome è "
print(testo + nome)
età = 18
print("ciaooo " + str(età))
||||||||||||||||||||||||||||||||||||||||||
nome= input("inserisci il tuo nome: ")
print(nome)
eta= input("inserisci il tuo eta: ")
print(eta)


eta= input("inserisci il tuo eta: ")
eta = int(eta)
if eta>18:
    print("Magg")
else:
    print("Nope")

Num1= input("inserisci n1: ")
Num2= input("inserisci n2: ")
Num1=int(Num1)
Num2=int(Num2)
if Num1==Num2:
    print("Sono uguali")
else:
    if Num1 > Num2:
        print(str(Num1) + " è il piu grande")
    else:
        print(str(Num2) + " è il piu grande")

Num1= input("inserisci n1: ")
Num2= input("inserisci n2: ")
Num1=int(Num1)
Num2=int(Num2)
somma=Num1+Num2
divisione= Num1/Num2
sottrazione= Num1-Num2
prodotto=Num1*Num2

print("la somma dei due numeri vale: " + str(somma))
print("la divisone dei due numeri vale: " + str(divisione))
print("la sottrazione dei due numeri vale: " + str(sottrazione))
print("il prodotto dei due numeri vale: " + str(prodotto))

def moltiplicatore():
    try:
        a = int(input("Inserisci il valore di a: "))
        b = int(input("Inserisci il valore di b: "))
        risultato = a * b
        print(risultato)
    except ValueError:
        print("Hey amico! solo caratteri numerici, grazie!")
    finally:
        print("Grazie per aver utilizzato questa applicazione!")

moltiplicatore()
"""
import random
alfa=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","10","+","-","?","'","@","!","£","$","%","&"]
i=0
F=str()
while i<16:
    L=random.randint(0,45)
    F=F+alfa[L]
    i=i+1

print(F)
