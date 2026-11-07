"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D)."""
from pathlib import Path

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
pytestmark = pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")


def test_demarrage_reel_charge_le_modele():
    """D.1 (donné en exemple) : un client ouvert par « with » exécute le lifespan."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")
    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


def test_modele_absent_refuse_de_demarrer(monkeypatch, tmp_path):
    """D.2 : sans fichier modèle, le lifespan échoue : l'API ne démarre pas."""
    from fastapi.testclient import TestClient

    import predict
    from api.main import app  # importé d'abord : api/model.py ajoute src/ au chemin

    monkeypatch.setattr(predict, "MODELE", tmp_path / "absent.joblib")
    predict.charger_modele.cache_clear()  # sinon le modèle déjà en cache serait réutilisé

    with pytest.raises(FileNotFoundError):
        with TestClient(app):
            pass

    predict.charger_modele.cache_clear()  # ne laisse aucun état au test suivant


def test_modele_non_charge_repond_503(monkeypatch):
    """D.3 : API démarrée, modèle retiré de app.state : 503 partout où il sert."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        monkeypatch.delattr(app.state, "classifier")
        assert client.get("/health").status_code == 503
        assert client.post("/predict", json={"text": "Très bon produit"}).status_code == 503


@pytest.mark.parametrize("panne", [RuntimeError("modèle HS"), ValueError("bug interne")])
def test_modele_en_panne_repond_500_sans_fuite(monkeypatch, panne):
    """D.4 : toute panne de predict donne 500, sans le message interne dans la réponse."""
    from fastapi.testclient import TestClient

    from api.main import app

    def en_panne(texte):
        raise panne

    monkeypatch.setattr("api.model._predict", en_panne)

    # raise_server_exceptions=False : on veut lire la réponse 500, pas voir l'exception remonter
    with TestClient(app, raise_server_exceptions=False) as client:
        reponse = client.post("/predict", json={"text": "Très bon produit"})

    assert reponse.status_code == 500
    assert str(panne) not in reponse.text
