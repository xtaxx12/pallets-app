import pytest
from rest_framework.test import APIClient
from pallets.models import Pallet
from django.urls import reverse

client = APIClient()

@pytest.mark.django_db
def test_crear_pallet():
    payload = {
        "id": "P12345",
        "fecha": "2025-05-17",
        "tipo": "INGRESO",
        "estado": "POR_RECIBIR",
        "origen": "SALMUERA",
        "desde_empresa": "Empresa A",
        "hacia_empresa": "Empresa B"
    }

    response = client.post("/api/pallets/", data=payload, format="json")

    assert response.status_code == 201
    assert Pallet.objects.count() == 1
    assert Pallet.objects.get(id="P12345").estado == "POR_RECIBIR"

@pytest.mark.django_db
def test_actualizar_estado():
    pallet = Pallet.objects.create(
        id="P67890",
        fecha="2025-05-17",
        tipo="INGRESO",
        estado="POR_RECIBIR",
        origen="MASTERIZADO",
        desde_empresa="Empresa A",
        hacia_empresa="Empresa B"
    )

    response = client.patch(f"/api/pallets/{pallet.id}/cambiar_estado/")

    assert response.status_code == 200
    pallet.refresh_from_db()
    assert pallet.estado == "RECIBIDO"
