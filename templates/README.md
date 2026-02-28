# Module des Templates

## Raison d'être

Ce répertoire contient les modèles HTML utilisés par Flask pour générer les pages web de manière dynamique. Le moteur de template Jinja2 traite ces fichiers pour y insérer des données provenant du serveur avant de les envoyer au client.

## Fichiers Principaux

- `index.html`:
  - **Responsabilité**: C'est le seul modèle de l'application. Il définit la structure HTML de la page de la calculatrice, y compris le formulaire, l'écran d'affichage et les boutons. Il contient des espaces réservés (comme `{{ result }}`) que Flask remplit avec des données dynamiques.

## Dépendances

- **Jinja2**: Le moteur de templates utilisé par Flask. La syntaxe des modèles (par exemple, `{{ ... }}` ou `{% ... %}`) est spécifique à Jinja2.

## Hypothèses

- Flask est configuré pour rechercher les templates dans ce répertoire. C'est le comportement par défaut lorsque les templates sont dans un dossier nommé `templates`.
- Le code serveur (dans `app.py`) passe un contexte au template (par exemple, la variable `result`) que celui-ci s'attend à recevoir.
