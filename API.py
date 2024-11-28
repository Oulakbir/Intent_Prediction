import torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Charger le modèle et le tokenizer
model = AutoModelForSequenceClassification.from_pretrained('./saved_model')
tokenizer = AutoTokenizer.from_pretrained('./saved_model')

# Liste des intentions, chaque index correspond à une classe d'intention
classes = ['insurance', 'next_holiday', 'repeat', 'credit_limit_change', 'book_hotel', 
           'yes', 'damaged_card', 'rewards_balance', 'time', 'pto_balance', 'interest_rate', 
           'change_volume', 'taxes', 'sync_device', 'traffic', 'what_song', 'shopping_list', 
           'todo_list_update', 'order_checks', 'shopping_list_update']

# Créer l'application FastAPI
app = FastAPI()

# Modèle pour la requête
class Message(BaseModel):
    text: str

# Point d'entrée pour prédire l'intention du texte
@app.post("/predict/")
async def predict(message: Message):
    # Tokenisation de l'entrée
    inputs = tokenizer(message.text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    
    # Calcul des probabilités avec softmax
    probs = torch.nn.functional.softmax(logits, dim=-1)
    
    # Trouver la classe prédite (indice)
    predicted_class = probs.argmax().item()
    
    # Récupérer le nom de l'intention correspondant à l'indice
    predicted_intent = classes[predicted_class]
    
    # Confiance en pourcentage
    confidence = probs.max().item() * 100  
    
    return {
        "prediction": predicted_intent,  # Renvoie le label d'intention
        "confidence": confidence
    }

# Point d'entrée pour vérifier si l'API est en ligne
@app.get("/")
async def root():
    return {"message": "API is running!"}
