"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():
    assert Calculator().addition(2, 3) == 5

def test_addition_erreur_volontaire():
    assert Calculator().addition(2, 3) == 99  # erreur volontaire : le résultat attendu est faux