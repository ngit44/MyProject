from fastapi.testclient import TestClient
from copy import deepcopy
import pytest

from app.main import app
from app.sample_data import sites

client = TestClient(app)

#autouse=True means pytest applies this fixture automatically to every test in this file.
@pytest.fixture(autouse=True)
def restore_sites():
    original_sites = deepcopy(sites)  # Before: save sample data

    yield                            # Run the test

    sites.clear()                    # After: remove current contents
    sites.update(original_sites)     # Restore sample data


def test_get_existing_site():
    # Arrange: choose a site in our sample data
    site_id = 1783718

    # Act: send the request
    response = client.get(f"/sites/{site_id}")

    # Assert: check the result
    assert response.status_code == 200
    assert response.json()["site_id"] == site_id
    
def test_get_missing_site():
    site_id = 99999
    response = client.get(f"/sites/{site_id}")

    assert response.status_code == 404
    assert response.json() == {"detail": "Site not found"}
    
def test_get_site_invalid_id():
    response = client.get("/sites/abc")

    assert response.status_code == 422
    
def test_create_site():
    site_id = 99999
    payload = {
        "site_name": "Test Monitoring Site",
        #"municipality": "Mississauga",
        "status": "Active",
        "depth": 100.0,
    }

    response = client.post(
        f"/sites/{site_id}",
        json=payload,
    )

    # TODO 1: Check the creation status code
    assert response.status_code == 201, response.json()

    # TODO 2: Check the returned site ID
    assert response.json()["site_id"] == site_id

    # Confirm the new site can be retrieved
    get_response = client.get(f"/sites/{site_id}")
    assert get_response.status_code == 200
    assert get_response.json()["site_name"] == payload["site_name"]