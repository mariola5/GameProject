# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#main.py

import time
import random
from board import Plansza, Pozycja
from game import Postac, walka
plansza = Plansza(5)
p1 = Postac("A", 10, 20)
p2 = Postac("B", 10, 20)
plansza.ustaw(p1, Pozycja(1, 1))
plansza.ustaw(p2, Pozycja(2, 1))
dx1, dy1 = 1, 0    # A startuje w prawo
dx2, dy2 = -1, 0   # B startuje w lewo
plansza.losuj_skarb()


tury_bez_skarbu = 0
LIMIT = 30
TURY_BEZ_SKRABU_START = 8  # np. 8 tur skarb jest nieaktywny

while True:
    print(plansza.render())
    # ruch A
    for _ in range(10):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        if plansza.przesun(p1, dx, dy):
            break

    spotkanie = plansza.czy_spotkanie()
    if spotkanie:
        a, b = spotkanie
        print("SPOTKANIE! WALKA!")
        walka(a, b)
        break

    # ruch B
    for _ in range(10):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        if plansza.przesun(p2, dx, dy):
            break

    spotkanie = plansza.czy_spotkanie()
    if spotkanie:
        a, b = spotkanie
        print("SPOTKANIE! WALKA!")
        walka(a, b)
        break

    if tury_bez_skarbu >= TURY_BEZ_SKRABU_START:
        if plansza.czy_skarb_zebrany(p1):
            print(f"🏆 {p1.imie} znalazł skarb! Wygrana!")
            break
        if plansza.czy_skarb_zebrany(p2):
            print(f"🏆 {p2.imie} znalazł skarb! Wygrana!")
            break

    tury_bez_skarbu += 1
    if tury_bez_skarbu >= LIMIT:
        plansza.losuj_skarb(force=True)
        tury_bez_skarbu = 0
        print("🔄 Skarb przeniósł się w nowe miejsce!")
    time.sleep(0.5)
    print()

print(plansza.render())

