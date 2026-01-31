import pytest
from board import Plansza, Pozycja
from game import Postac


def test_w_srodku():
    plansza = Plansza(5)
    assert plansza.w_srodku(Pozycja(0, 0)) is True
    assert plansza.w_srodku(Pozycja(4, 4)) is True
    assert plansza.w_srodku(Pozycja(5, 0)) is False
    assert plansza.w_srodku(Pozycja(0, 5)) is False


def test_ustaw_poza_plansza_raises():
    plansza = Plansza(5)
    p1 = Postac("A", 10, 20)
    with pytest.raises(ValueError):
        plansza.ustaw(p1, Pozycja(10, 10))


def test_ustaw_i_render_pokazuje_postac():
    plansza = Plansza(3)
    p1 = Postac("A", 10, 20)
    plansza.ustaw(p1, Pozycja(1, 1))

    out = plansza.render()
    # w środku powinno być A
    assert "A" in out


def test_przesun_zmienia_pozycje():
    plansza = Plansza(5)
    p1 = Postac("A", 10, 20)
    plansza.ustaw(p1, Pozycja(1, 1))

    ok = plansza.przesun(p1, 1, 0)
    assert ok is True
    assert plansza.pozycje[p1].x == 2
    assert plansza.pozycje[p1].y == 1


def test_przesun_blokuje_wyjscie_poza_plansze():
    plansza = Plansza(5)
    p1 = Postac("A", 10, 20)
    plansza.ustaw(p1, Pozycja(0, 0))

    ok = plansza.przesun(p1, -1, 0)
    assert ok is False
    assert plansza.pozycje[p1].x == 0
    assert plansza.pozycje[p1].y == 0


def test_spotkanie_gdy_to_samo_pole():
    plansza = Plansza(5)
    p1 = Postac("A", 10, 20)
    p2 = Postac("B", 10, 20)

    plansza.ustaw(p1, Pozycja(2, 2))
    plansza.ustaw(p2, Pozycja(2, 2))

    assert plansza.czy_spotkanie() == (p1, p2)

def test_ustaw_skarb_i_render_pokazuje_T():
    plansza = Plansza(5)
    plansza.ustaw_skarb(Pozycja(2, 2))
    out = plansza.render()
    assert "S" in out


def test_wejscie_na_skarb_daje_wygrana():
    plansza = Plansza(5)
    p1 = Postac("A", 10, 20)

    plansza.ustaw(p1, Pozycja(1, 1))
    plansza.ustaw_skarb(Pozycja(2, 1))

    assert plansza.czy_skarb_zebrany(p1) is False
    plansza.przesun(p1, 1, 0)  # A idzie na (2,1)
    assert plansza.czy_skarb_zebrany(p1) is True



