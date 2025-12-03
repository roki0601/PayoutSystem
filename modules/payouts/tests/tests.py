import pytest
from rest_framework.test import APIClient
from unittest.mock import patch
from modules.payouts.models import Payout, PayoutStatus

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_payout(api_client):
    data = {
        "amount": "150.50",
        "currency": "RUB",
        "recipient": "Иван Иванов",
        "description": "Тестовая выплата"
    }

    with patch("modules.payouts.views.process_payout_task.delay") as mock_task:
        response = api_client.post("/api/payouts/", data, format="json")
        assert response.status_code == 201

        mock_task.assert_called_once()

        payout = Payout.objects.get(id=response.data["id"])
        assert payout.amount == 150.50
        assert payout.status == PayoutStatus.NEW
        
@pytest.mark.django_db
def test_payout_list(api_client):
    for i in range(15):
        Payout.objects.create(amount=100+i, currency="RUB", recipient=f"User {i}")

    response = api_client.get("/api/payouts/")
    assert response.status_code == 200
    assert response.data["count"] == 15