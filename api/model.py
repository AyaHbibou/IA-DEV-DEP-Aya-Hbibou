"""Raccord entre l'API et le modèle entraîné au TP2.

L'API n'entraîne rien et ne connaît pas scikit-learn : elle appelle la fonction
predict() du paquet sentiment_app, qui charge le modèle une seule fois.
"""
import os

from sentiment_app.predict import charger_modele
from sentiment_app.predict import predict as _predict

# Sous ce score de confiance, le modèle ne tranche pas : l'étiquette devient INDETERMINE.
SEUIL_ABSTENTION = float(os.environ.get("SEUIL_ABSTENTION", "0.60"))


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec l'interface attendue par l'API."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        charger_modele()  # échoue immédiatement si le joblib manque : on ne démarre pas sans modèle

    def predict(self, text: str) -> dict:
        """Renvoie {'label': 'POSITIVE'|'NEGATIVE'|'INDETERMINE', 'score': float, 'text': aperçu}."""
        r = _predict(text)  # lève ValueError si le texte est vide
        label = r["label"].upper()
        if r["score"] < SEUIL_ABSTENTION:
            label = "INDETERMINE"  # le score reste renvoyé tel quel
        return {"label": label, "score": r["score"], "text": text[:100]}


def load_model() -> SentimentClassifier:
    """Construit le classifier (le cache de chargement est dans sentiment_app/predict.py)."""
    return SentimentClassifier()
