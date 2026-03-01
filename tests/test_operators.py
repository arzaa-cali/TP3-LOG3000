"""
Tests unitaires pour les fonctions arithmétiques du module operators.

Ce module vérifie le bon fonctionnement des quatre opérations de base :
addition, soustraction, multiplication et division.
"""
import pytest
from operators import add, subtract, multiply, divide


def test_add():
    """Vérifie que la fonction add retourne la somme de deux nombres."""
    assert add(1, 2) == 3
    assert add(-1, 2) == 1

def test_subtract():
    """Vérifie que la fonction subtract retourne la différence (a - b)."""
    assert subtract(2, 1) == 1
    assert subtract(1, 2) == -1

def test_multiply():
    """Vérifie que la fonction multiply retourne le produit de deux nombres."""
    assert multiply(1, 2) == 2
    assert multiply(-1, 2) == -2

def test_divide():
    """Vérifie que la fonction divide retourne la division (a / b)."""
    assert divide(1, 2) == 0.5
    assert divide(2, -1) == -2
