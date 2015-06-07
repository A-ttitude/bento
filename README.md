# bento
### Projet Django Master 2 ISIDIS

Nous avons rencontré des problèmes lors de l'utilisation des fixtures (problème de `no such table: auth_user`).

Afin de régler ce problème, nous avons dû commenter l'utilisation des fixtures lors de la création de la base, puis de
refaire un `migrate` avec les fixtures activés.

Voici la marche à suivre :

1. Faire le `makemigrations`

2. Faire le `migrate`

3. Dans settings.py, décommenter les lignes suivantes (97 à 100)
```python
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, '../bento/fixtures'),
)
```
4. Refaire le `migrate`


### Requirements

Voici les dépendances nécessaires pour utiliser le site :

- Django == 1.8.1

- django-debug-toolbar == 1.3.0

- pip == 1.5.6

- setuptools == 3.6

- sqlparse == 0.1.15