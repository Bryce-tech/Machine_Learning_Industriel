# Energy Performance Dashboard

Suivi simple de performance énergétique pour un réseau de chaleur, avec un volet qualité des données.

## Objectif

Ce projet propose un exemple de suivi de performance énergétique sur un réseau de chaleur à partir de données journalières simulées.

Le but est de montrer une démarche claire : intégrer des données techniques, contrôler leur qualité, calculer des indicateurs utiles et construire quelques visualisations lisibles pour l'aide à la décision.

## Contexte métier

Le jeu de données représente plusieurs sites clients raccordés à un réseau de chaleur. Chaque ligne correspond à une journée pour un site.

Les données suivent notamment l'énergie produite, l'énergie livrée, les pertes réseau, le rendement, la température extérieure et les anomalies de qualité.

## Contenu du dépôt

```text
energy-performance-dashboard/
│
├── README.md
├── requirements.txt
├── data/
│   └── reseau_chaleur_sample.csv
└── notebooks/
    └── energy_performance_dashboard.ipynb
```

Le notebook contient tout le projet : chargement ou création des données, contrôles qualité, nettoyage, indicateurs et graphiques.

## Indicateurs suivis

- Énergie produite totale
- Énergie livrée totale
- Pertes réseau
- Rendement moyen
- Nombre d'anomalies détectées
- Taux de données fiables
- Site le plus performant
- Site avec le plus d'anomalies

## Comment lancer le projet

Depuis un terminal :

```bash
cd energy-performance-dashboard
python -m venv .venv
```

Sous Windows :

```bash
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/energy_performance_dashboard.ipynb
```

Sous macOS ou Linux :

```bash
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/energy_performance_dashboard.ipynb
```

Le fichier CSV est déjà fourni. Si le fichier est supprimé, le notebook peut recréer un jeu de données fictif automatiquement.

## Compétences montrées

- Manipulation de données avec `pandas`
- Génération et chargement de données CSV en UTF-8
- Contrôle qualité simple et explicable
- Nettoyage de valeurs manquantes ou incohérentes
- Calcul de KPI métier
- Visualisation avec `plotly`
- Documentation claire d'un projet data

## Améliorations possibles

- Connecter le notebook à une vraie base de données
- Automatiser les contrôles qualité
- Suivre les anomalies au quotidien
- Ajouter des prévisions de consommation
- Créer des alertes sur les rendements anormaux
