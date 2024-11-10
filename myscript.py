import os
# Démarrer le bisect en spécifiant le bon et le mauvais commit
os.system("git bisect start c1a4be04b972b6c17db242fc37752ad517c29402 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")

# Exécuter les tests pour chaque commit dans le bisect
os.system("git bisect run python manage.py test")

# Réinitialiser le bisect après l'exécution
#os.system("git bisect reset")
