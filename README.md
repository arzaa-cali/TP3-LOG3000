# Projet de Calculatrice Web avec Flask - Équipe 61

## 1. Description du Projet

Ce projet est une application web de calculatrice simple développée avec le micro-framework Python Flask. L'objectif est de fournir une interface utilisateur basique permettant d'effectuer des calculs arithmétiques simples directement depuis un navigateur web.

**Portée du projet :**

- Interface web simple pour la saisie et l'affichage.
- Gestion des calculs sur le serveur.
- Support pour les opérations arithmétiques de base sur des expressions à deux opérandes et un opérateur.
- Structure de projet modulaire séparant la logique de l'application, les templates HTML et les fichiers statiques.

## 2. Guide d'Installation

Suivez ces étapes pour mettre en place l'environnement de développement et lancer le projet.

**Prérequis :**

- Python 3.6+
- `pip` (le gestionnaire de paquets de Python)
- `git` (pour cloner le dépôt)

**Étapes d'installation :**

1.  **Clonez le dépôt :**

    ```bash
    git clone <URL_DU_DÉPÔT>
    cd TP3---LOG3000
    ```

2.  **(Optionnel) Créez un environnement virtuel :**
    Cela permet d'isoler les dépendances du projet.

    ```bash
    # Pour Windows
    python -m venv venv
    venv\Scripts\activate

    # Pour macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Installez les dépendances :**
    ```bash
    pip install Flask pytest
    ```

## 3. Instructions d'Utilisation

Une fois l'installation terminée, vous pouvez lancer l'application.

1.  **Démarrez le serveur de développement Flask :**
    Assurez-vous d'être à la racine du projet (`TP3---LOG3000`) et que votre environnement virtuel est activé.

    ```bash
    python app.py
    ```

2.  **Accédez à l'application :**
    Ouvrez votre navigateur web et allez à l'adresse suivante :
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

3.  **Utilisez la calculatrice :**
    - Cliquez sur les boutons pour former une expression (par exemple, `6+7`).
    - L'expression apparaît dans la zone d'affichage.
    - Appuyez sur `=` pour soumettre le calcul.
    - Le résultat s'affichera dans la zone d'affichage.
    - Le bouton `C` efface l'entrée actuelle.

## 4. Tests

Les tests unitaires se trouvent dans le répertoire `tests/` et utilisent le framework `pytest`.

Assurez-vous que l'environnement virtuel est activé, puis exécutez :

```bash
pytest
```

Les tests couvrent :

- **`tests/test_app.py`** : analyse d'expressions par la fonction `calculate` (espaces, nombres décimaux, nombres négatifs, cas d'erreur).
- **`tests/test_operators.py`** : opérations arithmétiques de base (`add`, `subtract`, `multiply`, `divide`).

Pour plus de détails, consultez le fichier [`tests/README.md`](tests/README.md).

## 5. Flux de Contribution

Pour contribuer au projet, veuillez suivre les étapes ci-dessous.

1.  **Signaler un problème (Issue) :**
    - Si vous trouvez un bug ou si vous avez une idée d'amélioration, créez une "Issue" sur le dépôt GitHub.
    - Décrivez le problème ou la fonctionnalité aussi précisément que possible.

2.  **Proposer une modification (Pull Request) :**
    - Faites un "Fork" du dépôt sur votre propre compte GitHub.
    - Créez une nouvelle branche pour vos modifications : `git checkout -b feature/nom-de-la-feature` ou `fix/description-du-bug`.
    - Effectuez vos modifications et "commitez-les" avec des messages clairs.
    - Poussez votre branche vers votre fork : `git push origin feature/nom-de-la-feature`.
    - Ouvrez une "Pull Request" (PR) depuis votre fork vers la branche `main` du dépôt original.
    - Assurez-vous que votre PR est liée à une "Issue" existante si possible.
