
#📕​📖​📗​📘​📙​📚​📒​ Application Django pour une bibliothèquelivre📕​📖​📗​📘​📙​📚​📒​

Ce projet est une application web Django pour gérer une bibliothèque locale. Vous pouvez suivre les étapes ci-dessous pour démarrer votre propre projet similaire.

## Étapes de configuration

1. Créez un projet Django :
   - Utilisez la commande `django-admin startproject nom_de_votre_projet` pour créer un projet Django.
   - Assurez-vous d'avoir Python et Django installés sur votre système.

2. Créez une application :
   - Dans le répertoire du projet, exécutez `python manage.py startapp bibliotheque` pour créer une nouvelle application.
   - Ajoutez `'bibliotheque'` à la liste `INSTALLED_APPS` dans `settings.py`.

3. Modèles de données :
   - Dans `bibliotheque/models.py`, définissez vos modèles pour les livres, les auteurs, etc.

4. Vues et URL :
   - Dans `bibliotheque/views.py`, créez les vues pour afficher les informations sur les livres, les auteurs, etc.
   - Configurez les URL dans `bibliotheque/urls.py`.

5. Base de données :
   - Dans `settings.py`, configurez la base de données. Par défaut, Django utilise SQLite.
   - Si vous utilisez une autre base de données, mettez à jour les paramètres dans `DATABASES`.

6. Migrations et création de la base de données :
   - Exécutez `python manage.py makemigrations` suivi de `python manage.py migrate`.
   - Créez la base de données avec `CREATE DATABASE nom_de_la_base;` si vous n'utilisez pas SQLite.

7. Serveur de développement :
   - Lancez le serveur avec `python manage.py runserver`.
   - Accédez à l'URL indiquée dans votre navigateur pour voir votre application.
     <br>
8.Exécution des tests:
Django dispose d’un framework de test intégré que vous pouvez utiliser pour tester votre application. Pour exécuter les tests, utilisez la commande suivante :

python manage.py test bibliotheque

## Documentation supplémentaire

Pour plus de détails, consultez les tutoriels officiels de Django :
- [Écriture de votre première application Django, 2ème partie](https://docs.djangoproject.com/fr/5.0/intro/tutorial02/)
-https://www.djangoproject.com/

 Bon développement ! 🚀


