from fastapi.testclient import TestClient
from main import app
client= TestClient(app)

def test_read_sheep():
    response= client.get("/sheep/1")
    assert response.status_code ==200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed":"Gotland",
        "sex": "ewe"
    }
def test_add_sheep():
    # TODO: Prepare the new sheep data in a dictionary format.
    new_sheep = {
        "id": 7,
        "name": "cat",
        "breed": "shaun ",
        "sex": "uhhhhh"
    }

    # TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
    # Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=new_sheep)

    # TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep

    # TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    # include an assert statement to see if the new sheep data can be retrieved.
    get_response = client.get(f"/sheep/{new_sheep['id']}")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep    

def test_delete_sheep_success():
    # Send a DELETE request to remove an existing sheep (e.g., ID 1)
    response = client.delete("/sheep/1")
    
    # Assert that the response status code is 204 (No Content)
    assert response.status_code == 204

  


def test_delete_sheep_not_found():
    # Try to delete a sheep ID that doesn't exist (e.g., ID 999)
    response = client.delete("/sheep/999")
    
    # Assert that it returns a 404 Not Found error
    assert response.status_code == 404
    
def test_update_sheep():
    # 1. First, make sure the sheep exists in the database
    initial_sheep = {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }
    client.post("/sheep", json=initial_sheep)

    # 2. Prepare the updated data
    updated_sheep_data = {
        "id": 1,
        "name": "Spice Updated",
        "breed": "Gotland",
        "sex": "ewe"
    }

    # 3. Send a PUT request to update the sheep
    response = client.put("/sheep/1", json=updated_sheep_data)
    
    # 4. Assert that the response data matches the updated data
    assert response.json() == updated_sheep_data

    # 5. Verify via GET that the database was actually updated
    get_response = client.get("/sheep/1")
    assert get_response.json() == updated_sheep_data