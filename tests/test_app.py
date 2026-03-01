"""
Tests unitaires pour la fonction calculate du module app.

Ce module vérifie le bon fonctionnement de l'analyse et de l'évaluation
des expressions arithmétiques par la fonction calculate.
"""
import pytest
from app import calculate


# --- Analyse d'expressions valides ---

def test_calculate_basic_expression():
    """Vérifie qu'une expression simple avec addition est correctement évaluée."""
    assert calculate("1+2") == 3.0

def test_calculate_with_spaces():
    """Vérifie que les espaces dans l'expression sont ignorés."""
    assert calculate("  1 + 2  ") == 3.0

def test_calculate_floats():
    """Vérifie que les nombres à virgule flottante sont supportés."""
    assert calculate("1.5+2.5") == 4.0

# --- Cas d'erreur ---

def test_calculate_empty_string():
    """Vérifie qu'une expression vide lève une ValueError."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate("")

def test_calculate_none():
    """Vérifie qu'une valeur None lève une ValueError."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate(None)

def test_calculate_no_operator():
    """Vérifie qu'une expression sans opérateur lève une ValueError."""
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("123")

def test_calculate_operator_at_end():
    """Vérifie qu'un opérateur en fin d'expression lève une ValueError."""
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("1+")

def test_calculate_non_numeric_operands():
    """Vérifie que des opérandes non numériques lèvent une ValueError."""
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("abc+def")

def test_calculate_division_by_zero():
    """Vérifie que la division par zéro lève une ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calculate("1/0")

def test_calculate_multiple_operators():
    """Vérifie que plus d'un opérateur dans l'expression lève une ValueError."""
    with pytest.raises(ValueError, match="only one operator is allowed"):
        calculate("1+2+3")
