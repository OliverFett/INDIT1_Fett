

import random

i = 0
Lotto =[]


Tipps = int(input("Wie viele Tipps möchten sie eingeben?"))

if Tipps > 0:
    
    while i < Tipps:
        Zahl = random.sample(range(1,45),6)
        if Zahl in Lotto:
            i = i
        else:
            Lotto.append(Zahl)
            i+=1

    print(Lotto)




