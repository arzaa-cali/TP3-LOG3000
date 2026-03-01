"""
Application web de calculatrice simple utilisant Flask.

Ce module définit une application Flask qui fournit une interface utilisateur de base pour
une calculatrice. Il gère les requêtes web, traite les entrées utilisateur et utilise
le module 'operators' pour effectuer les calculs arithmétiques.
"""
from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire associant les symboles d'opérateurs aux fonctions correspondantes
# du module 'operators'.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique simple sous forme de chaîne de caractères.

    L'expression doit contenir deux opérandes numériques et un seul opérateur
    parmi +, -, *, /. Les espaces dans l'expression sont ignorés.

    Args:
        expr (str): La chaîne de caractères représentant l'expression à évaluer.

    Returns:
        float: Le résultat du calcul.

    Raises:
        ValueError: Si l'expression est invalide, mal formée, contient des
                    opérandes non numériques ou plus d'un opérateur.
    """
    # Vérifie si l'expression est vide ou non une chaîne de caractères
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Supprime les espaces pour simplifier l'analyse de l'expression
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche l'opérateur dans l'expression
    for i, ch in enumerate(s):
        if ch in OPS:
            # Si un deuxième opérateur est trouvé, lève une exception
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie que l'opérateur n'est pas au début ou à la fin de l'expression
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # Sépare l'expression en deux parties : gauche (avant l'opérateur) et droite (après)
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        # Tente de convertir les opérandes en nombres flottants
        a = float(left)
        b = float(right)
    except ValueError:
        # Lève une exception si les opérandes ne sont pas des nombres
        raise ValueError("operands must be numbers")

    # Appelle la fonction de l'opérateur correspondant et retourne le résultat
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gère la page d'accueil de la calculatrice.

    Pour une requête GET, affiche la calculatrice avec un résultat vide.
    Pour une requête POST, calcule l'expression fournie dans le formulaire
    et affiche le résultat ou un message d'erreur.

    Returns:
        str: Le rendu du modèle HTML 'index.html' avec le résultat.
    """
    result = ""
    if request.method == 'POST':
        # Récupère l'expression du formulaire
        expression = request.form.get('display', '')
        try:
            # Tente de calculer le résultat
            result = calculate(expression)
        except Exception as e:
            # En cas d'erreur, affiche le message d'erreur
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lance l'application en mode débogage
    app.run(debug=True)