# Geisterspeil
from random import randint
print("Geisterspeil")
du_bist_mutig = True
score = 0
while du_bist_mutig:
    print(du_bist_mutig)
    print("du_bist_mutig")
    print("score")
    print(score)
    geistertuer = randint(1, 3)
    print("Vor dir sind drei türen...")
    print("Hiner einer ist ein Geist.")
    print("Welche tür öffnest du ?")
    tuer_nummer = int(tuer)
    if tuer_numer == geistertuer:
        print("GEIST!")
        du_bist_mutig = False
    else:
        print("Kein Geist")
        print("Du bist ein Zimer weiter.")
        score = score + 1
print("Lauf weg!")
print("Speil vorbei!")
        
    
