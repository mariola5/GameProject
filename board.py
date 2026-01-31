#board.py

import random
class Pozycja:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Plansza:
    def __init__(self, rozmiar):
        if rozmiar <= 0:
            raise ValueError("Rozmiar planszy musi być dodatnią liczba")
        self.rozmiar = rozmiar
        self.pozycje = {}
        self.skarb = None

    def w_srodku(self, p: Pozycja) -> bool:
        return 0 <= p.x < self.rozmiar and 0 <= p.y < self.rozmiar

    def ustaw(self, postac, pozycja: Pozycja) -> None:
        if not self.w_srodku(pozycja):
            raise ValueError("Pozycja poza plansza")
        self.pozycje[postac] = pozycja


    def render(self):
        n = self.rozmiar
        grid = [["." for _ in range(n)] for _ in range(n)]

        if self.skarb is not None:
            grid[self.skarb.y][self.skarb.x] = "S"

        for postac, pos in self.pozycje.items():
            znak = getattr(postac, "imie", str(postac))[0]
            grid[pos.y][pos.x] = znak
            #y wiesz, x kolumna
        return "\n".join(" ".join(wiersz) for wiersz in grid)

    def przesun(self, postac, dx, dy):
        p = self.pozycje[postac]
        nowa = Pozycja(p.x + dx, p.y + dy)

        if not self.w_srodku(nowa):
            return False
        self.pozycje[postac] = nowa
        return True
    def kto_na_polu(self, pozycja):
        return [postac for postac, p in self.pozycje.items() if p.x == pozycja.x and p.y == pozycja.y]

    def czy_spotkanie(self):

        postacje = list(self.pozycje.keys())
        for i in range(len(postacje)):
            for j in range(i + 1, len(postacje)):
                a, b = postacje[i], postacje[j]
                pa, pb = self.pozycje[a], self.pozycje[b]
                if pa.x == pb.x and pa.y == pb.y:
                    return a, b
        return None

    def ustaw_skarb(self, pozycja: Pozycja) -> None:
        if not self.w_srodku(pozycja):
            raise ValueError("Skarb poza planszą")
        if any(p.x == pozycja.x and p.y == pozycja.y for p in self.pozycje.values()):
            raise ValueError("Nie można ustawić skarbu na polu zajętym przez postać")
        self.skarb = pozycja

    def losuj_skarb(self, force=False) -> Pozycja:
        # zajęte pola przez postacie
        if self.skarb is not None and not force:
            return self.skarb
        zajete = {(p.x, p.y) for p in self.pozycje.values()}

        while True:
            x = random.randrange(self.rozmiar)
            y = random.randrange(self.rozmiar)
            if (x, y) not in zajete:
                self.skarb = Pozycja(x, y)
                return self.skarb

    def czy_skarb_zebrany(self, postac) -> bool:
        if self.skarb is None:
            return False
        p = self.pozycje[postac]
        return p.x == self.skarb.x and p.y == self.skarb.y