import pytest

from task1 import factorial
from task2 import show_result
from task3 import simulate_battle,Warrior,Mage


def test_factorial():
    assert factorial(1)==1
    assert factorial(2)==2
    assert factorial(3)==6
    assert factorial(4)==24
    assert factorial(5)==120

def test_show_result():
    assert show_result()

def test_simulate_battle():
    w = Warrior("Thorgal", 100, 10)
    m = Mage("Merlin", 60, 20)
    w.attack(m)
    assert w.hp==100 and m.hp == 45 and m.mana == 20
    m.attack(w)
    assert w.hp==75 and m.hp == 45 and m.mana == 10
    m.attack(w)
    assert w.hp==50 and m.hp == 45 and m.mana == 0
    m.attack(w)
    assert w.hp==50 and m.hp == 45 and m.mana == 0
    m.attack(w)
    assert w.hp==50 and m.hp == 45 and m.mana == 0




