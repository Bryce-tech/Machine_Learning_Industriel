# CNN

Petit projet Python pour experimenter autour des reseaux de neurones.

## Creer l'environnement virtuel

Depuis ce dossier, ouvre PowerShell puis lance :

```powershell
python -m venv .venv
```

Active ensuite l'environnement virtuel :

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloque l'activation avec une erreur de politique d'execution, lance :

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Puis reessaie :

```powershell
.\.venv\Scripts\Activate.ps1
```

Quand l'environnement est actif, le prompt commence generalement par `(.venv)`.

## Installer les dependances

Installe les dependances du projet avec :

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Pour le moment, le projet n'utilise aucune bibliotheque externe. Le fichier `requirements.txt` est donc vide, et cette commande ne devrait rien installer.

## Lancer le script

```powershell
python perceptron_and.py
```

## Desactiver l'environnement virtuel

Quand tu as fini :

```powershell
deactivate
```

## Sur macOS ou Linux

Les commandes sont presque identiques :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python perceptron_and.py
```
