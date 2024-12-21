### **Contexte et Objectifs**  
En tant qu'ingénieur(e) cloud, ma mission est de migrer l’application de **Intent Prediction** vers le cloud AWS. Cette migration vise à :  
- Moderniser l’infrastructure.  
- Garantir une haute disponibilité et scalabilité.  
- Optimiser les performances et les coûts.  
- Automatiser les déploiements via des pratiques DevOps.  

L’objectif est d’héberger une application **ML (Intent Prediction)** qui comprend :  
- Une **API REST** pour traiter les requêtes et retourner les intentions prédictes.  
- Un modèle pré-entraîné (comme BERT), fine-tuné localement et exporté.  
- Une interface simple pour tester les prédictions d'intentions.  

---

### **Analyse et Conception de l’Architecture**  

#### **Analyse de l’application :**  
1. **Dépendances nécessaires** :  
   - Modèle pré-entraîné (`.h5` ou `.pt`),  
   - Bibliothèques Python (Transformers, PyTorch ou TensorFlow, Flask ou FastAPI),  
   - Environnement runtime Python 3.8 ou supérieur.  

2. **Ressources nécessaires** :  
   - **CPU et RAM** : 2 vCPU et 4 GB RAM suffisent pour la version actuelle.  
   - **Stockage** : 5-10 Go pour le modèle ML et les fichiers d’artefacts.  
   - **Base de données** : Une base relationnelle ou NoSQL (si besoin de logs ou stockage).  

#### **Architecture Cloud sur AWS :**  
L'architecture intègre :  
- **EC2** pour exécuter l’API et le modèle.  
- **S3** pour héberger les fichiers du modèle.  
- **DynamoDB** pour le stockage des logs et analyses (optionnel).  
- **IAM Roles** pour sécuriser les accès aux ressources.  
- **Load Balancer (ELB)** et **Auto Scaling Group** pour la haute disponibilité et scalabilité.  

---

### **Implémentation Technique sur AWS**  

#### **Choix technique : PaaS ou IaaS ?**  
J'ai choisi une approche **IaaS (EC2)** pour plus de flexibilité dans la gestion du modèle ML et des configurations spécifiques.  

#### **Étapes détaillées :**  
1. **Configuration des services AWS :**  
   - Création d’un **S3 bucket** pour stocker le modèle et d'autres artefacts.  
   - Lancement d’une instance EC2 (t2.medium) pour héberger l’API.  

2. **Déploiement de l’API :**  
   - Transfert des fichiers nécessaires via **SCP** ou AWS CLI.  
   - Installation des dépendances Python et configuration du modèle ML.  
   - Lancement du serveur Flask ou FastAPI avec un outil comme **Gunicorn**.  

3. **Sécurité et Réseau :**  
   - Configuration d’un **Security Group** pour autoriser les ports nécessaires (HTTP/HTTPS).  
   - Ajout d’un **Elastic Load Balancer (ELB)** pour répartir les requêtes.  

4. **Automatisation et Monitoring :**  
   - Mise en place de **CloudWatch** pour le monitoring.  
   - Option : Utilisation d’**AWS CodePipeline** pour la CI/CD.  

---

### **Livrables**  

1. **Rapport** :  
   - **Introduction** : Résumé du contexte, objectifs et enjeux.  
   - **Description de l’application** : Front-end (facultatif), back-end (API), modèle ML, etc.  
   - **Architecture proposée** : Diagramme précis et description détaillée.  
   - **Justification des choix** : Pourquoi EC2 ? Pourquoi S3 ? Coût optimisé ?  
   - **Implémentation** : Étapes détaillées et captures d’écran.  
   - **Conclusion** : Résultats, défis rencontrés, et recommandations.  

2. **Présentation PPT** :  
   - Introduction au projet.  
   - Description de l’application et des composants.  
   - L’architecture proposée.  
   - Justification des choix techniques.  
   - Démonstration (captures d'écran).  
   - Conclusion (apports, défis, perspectives).  

3. **Vidéo (20 min max)** :  
   - Présentation orale (objectifs et contexte).  
   - Explication de l’architecture.  
   - Démonstration de l’application déployée via une URL publique.  
   - Résumé des défis et des solutions apportées.  
