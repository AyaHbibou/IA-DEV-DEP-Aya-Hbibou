
"""Tests aux limites du contrat d'entrée (TP4, étape B)."""

import json
from pathlib import Path

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"

pytestmark = pytest.mark.skipif(
    not MODELE.exists(),
    reason="modèle non produit : python src/train.py",
)


@pytest.fixture(scope="module")
def client():
    """Démarre l'API une seule fois pour ce fichier."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as c:
        yield c


def en_json(valeur: object) -> bytes:
    """Convertit une valeur en JSON encodé en octets."""
    return json.dumps(valeur).encode("utf-8")


# Étape B.1 : huit cas limites au minimum
CAS = [
    pytest.param(en_json({"text": ""}), 422, id="texte-vide"),
    pytest.param(en_json({"text": "   "}), 422, id="espaces-seuls"),
    pytest.param(en_json({"text": "a"}), 200, id="un-caractere"),
    pytest.param(en_json({"text": "a" * 2000}), 200, id="2000-caracteres"),
    pytest.param(en_json({"text": "a" * 2001}), 422, id="2001-caracteres"),
    pytest.param(en_json({}), 422, id="champ-absent"),
    pytest.param(en_json({"text": 42}), 422, id="type-entier"),
    pytest.param(b"pas du json", 422, id="json-invalide"),
]


# Étape B.2 : vérification des frontières et de la forme des erreurs
@pytest.mark.parametrize("corps, code_attendu", CAS)
def test_frontieres_du_contrat(client, corps, code_attendu):
    reponse = client.post(
        "/predict",
        content=corps,
        headers={"Content-Type": "application/json"},
    )

    assert reponse.status_code == code_attendu

    if code_attendu == 422:
        donnees = reponse.json()

        assert "detail" in donnees
        assert isinstance(donnees["detail"], list)
        assert len(donnees["detail"]) > 0

        for erreur in donnees["detail"]:
            assert isinstance(erreur, dict)
            assert "loc" in erreur
            assert "msg" in erreur
            assert "type" in erreur


# Étape B.5.1 : propriété des textes valides
ALPHABET_TEXTE = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789 .,!?éà"
)


@settings(deadline=None, max_examples=30)
@given(
    texte=st.text(
        alphabet=ALPHABET_TEXTE,
        min_size=1,
        max_size=2000,
    ).filter(lambda t: any(not c.isspace() for c in t))
)
def test_propriete_texte_valide(client, texte):
    reponse = client.post(
        "/predict",
        content=en_json({"text": texte}),
        headers={"Content-Type": "application/json"},
    )

    assert reponse.status_code == 200

    donnees = reponse.json()
    assert "label" in donnees
    assert "score" in donnees
    assert isinstance(donnees["score"], (int, float))
    assert 0 <= donnees["score"] <= 1


# Étape B.5.2 : propriété des textes composés uniquement de blancs
@settings(deadline=None, max_examples=30)
@given(
    texte=st.text(
        alphabet=" \t\n\r",
        min_size=1,
        max_size=2000,
    )
)
def test_propriete_texte_blanc(client, texte):
    reponse = client.post(
        "/predict",
        content=en_json({"text": texte}),
        headers={"Content-Type": "application/json"},
    )

    assert reponse.status_code == 422

    donnees = reponse.json()
    assert "detail" in donnees
    assert isinstance(donnees["detail"], list)
    assert len(donnees["detail"]) > 0

    for erreur in donnees["detail"]:
        assert isinstance(erreur, dict)
        assert "loc" in erreur
        assert "msg" in erreur
        assert "type" in erreur
