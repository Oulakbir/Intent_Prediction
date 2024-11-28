# Banking Chatbot Assistant

## Prérequis

Avant de commencer, vous devez installer les éléments suivants sur votre machine :

- **Python 3.7+**
- **FastAPI** (pour l'API de prédiction)
- **Streamlit** (pour l'interface utilisateur)
- **Uvicorn** (pour lancer FastAPI)
- **Requests** (pour effectuer des requêtes HTTP)
- 
##  Run the Notebook

First of all you have to run the notebook some the folder "saved_model" will be created in your current directory and which will be used to run your application. 
If the folder is generated you can proceed with the remaining steps to lounch the application.

## Étapes pour démarrer l'application

1. **Installer les dépendances** : 

   Clonez le dépôt ou assurez-vous que vous avez le fichier `requirements.txt` contenant les dépendances nécessaires.

   ```bash
   pip install -r requirements.txt
   ```

2. **Lancer le serveur FastAPI avec Uvicorn** : 

   Ouvrez un terminal et exécutez la commande suivante pour démarrer le serveur FastAPI :

   ```bash
   uvicorn API:app --reload
   ```

   Le serveur sera accessible à l'URL suivante :
   ```
   http://127.0.0.1:8000
   ```

3. **Lancer l'application Streamlit** : 

   Ensuite, dans un autre terminal, exécutez l'application Streamlit avec la commande suivante :

   ```bash
   streamlit run chatbot.py
   ```

   L'application sera accessible à l'URL suivante :
   ```
   http://localhost:8501
   ```

   Here is How the applicatio looks like:
   
   ![Screenshot 2024-11-28 192442](https://github.com/user-attachments/assets/71f0eff8-0a36-4fe8-af07-311f3098cc5a)

