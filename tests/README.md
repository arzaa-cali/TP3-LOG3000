# Module de tests

Ce répertoire contient les tests unitaires pour l'application de calculatrice.

## Exécution des tests

Depuis la racine du projet, avec l'environnement virtuel activé (`venv\Scripts\activate` sur Windows ou `source venv/bin/activate` sur macOS/Linux) :

```bash
# Exécuter tous les tests
pytest

# Exécuter un fichier de test spécifique
pytest tests/test_app.py -v
pytest tests/test_operators.py -v
```

## Couverture des tests

### `test_app.py` — Fonction `calculate`

Teste l'analyse et l'évaluation des expressions arithmétiques :

- **Expressions valides** : expression simple, espaces, nombres décimaux, nombres négatifs.
- **Cas d'erreur** : expression vide, valeur `None`, absence d'opérateur, opérateur en fin d'expression, opérandes non numériques, division par zéro, opérateurs multiples.

### `test_operators.py` — Fonctions arithmétiques

Teste les quatre opérations de base du module `operators` :

- `add(a, b)` — addition
- `subtract(a, b)` — soustraction
- `multiply(a, b)` — multiplication
- `divide(a, b)` — division
