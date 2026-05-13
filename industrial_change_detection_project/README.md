# Industrial Visual Change Detection

Prototype Python pour comparer deux images d'une même zone industrielle prises à deux instants différents, détecter des écarts visuels et produire une table de zones à vérifier.

Le notebook utilise une scène synthétique afin de rester reproductible et d'éviter l'usage de données industrielles sensibles. La sortie principale est un fichier CSV contenant des régions candidates pour une revue manuelle.

## Fichiers

- `industrial_visual_change_detection.ipynb` : notebook principal.
- `requirements.txt` : dépendances nécessaires au notebook.
- `outputs/detected_visual_changes.csv` : export créé lors de l'exécution du notebook.

## Installation

### 1. Cloner le repository

```bash
git clone <URL_DU_REPOSITORY>
cd industrial-visual-change-detection
```

### 2. Créer un environnement virtuel

Sous macOS / Linux :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Sous Windows PowerShell :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Lancer Jupyter Notebook

```bash
jupyter notebook
```

Ou avec JupyterLab si disponible :

```bash
jupyter lab
```

Ouvrir ensuite `industrial_visual_change_detection.ipynb`.

### 5. Désactiver l'environnement virtuel

```bash
deactivate
```

## Adapter à des images réelles

Placer deux images dans un dossier local, par exemple :

```text
data/before.jpg
data/after.jpg
```

Puis remplacer la génération synthétique par un chargement d'images avec OpenCV. Les images doivent représenter la même zone avec un cadrage aussi proche que possible.

## Limites

La méthode est sensible à l'éclairage, au cadrage et aux changements de perspective. Des faux positifs sont possibles. Une évaluation fiable nécessite un jeu de données annoté et représentatif du cas d'usage.
