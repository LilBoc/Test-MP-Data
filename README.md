
# Projet Test MP Data

L'objectif de ce projet est de construire un modèle capable de prédire si un joueur de NBA va rester plus de 5 ans dans le championnat, et donc si il est intéressant de le sponsoriser, à partir de ses statistiques de jeu.

Pour cela nous avons à notre disposition un jeu de donnée avec les statistiques de match de certains joueurs, et si ils ont duré plus de 5 ans dans le championnat.

Le modèle retenu est un modèle XGBoost. Son seuil a été fixé à 0.25 mais cette valeur est amenée a évoluer selon les besoins du client.

## Notebook

Le notebook Notebook_Lilian.ipynb présente la partie analyse des données et construction du modèle.

## API

L'api est construite dans le dossier APILilian, elle est construite avec flask. Pour l'utiliser, suivez les instructions suivantes:

- installation de virtualenv: 
```bash
pip install virtualenv
```
- création de l'environnement virtuel: 
```bash
virtualenv api_venv
```
- activation de l'environnement: 
```bash
source api_venv/bin/activate
```
- Installation des dépendances dans l'environnement: 
```bash
pip install -r requirements.txt
```

- Lancement de l'API:
```bash
python app.py
```

Entrez ensuite l'url suivante dans votre navigateur:

http://127.0.0.1:5000

Rentrez les statistiques de votre joueur, cliquez sur "Submit" et observez les prédictions du modèle.


