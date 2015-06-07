# bento
### Projet Django Master 2 ISIDIS

Nous avons rencontr� des probl�mes lors de l'utilisation des fixtures (probl�me de `no such table: auth_user`).

Afin de r�gler ce probl�me, nous avons d� commenter l'utilisation des fixtures lors de la cr�ation de la base, puis de
refaire un `migrate` avec les fixtures activ�s.

Voici la marche � suivre :

1. Faire le `makemigrations`

2. Faire le `migrate`

3. Dans settings.py, d�commenter les lignes suivantes (97 � 100)
```python
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
FIXTURE_DIRS = (
    os.path.join(PROJECT_DIR, '../bento/fixtures'),
)
```
4. Refaire le `migrate`


### Requirements

Voici les d�pendances n�cessaires pour utiliser le site :

- Django == 1.8.1

- django-debug-toolbar == 1.3.0

- pip == 1.5.6

- setuptools == 3.6

- sqlparse == 0.1.15