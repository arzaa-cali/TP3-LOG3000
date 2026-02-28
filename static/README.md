# Module Statique

## Raison d'être

Ce répertoire contient tous les fichiers statiques qui sont servis directement au navigateur sans traitement côté serveur. Cela inclut les feuilles de style, les images, et les scripts JavaScript côté client.

## Fichiers Principaux

- `style.css`:
  - **Responsabilité**: Cette feuille de style CSS définit l'apparence et la mise en page de l'application de la calculatrice. Elle est responsable de tous les aspects visuels, comme les couleurs, les polices, la disposition des boutons et le design général de l'interface.

## Dépendances

- Aucune.

## Hypothèses

- Le framework Flask est configuré pour servir les fichiers de ce répertoire à partir de l'URL `/static`. C'est le comportement par défaut de Flask, mais il est essentiel au bon fonctionnement de l'application.
