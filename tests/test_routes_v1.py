from fastapi.testclient import TestClient
from psyncly.app import app

client = TestClient(app)


def test_user_create():
    response = client.post(
        "/v1/users",
        json={"username": "testuser1", "email": "testuser1@example.com"},
    )

    assert response.status_code == 201


def test_user_list():
    response = client.get("/v1/users")

    data_list = response.json()

    assert len(data_list) == 1

    data = data_list[0]

    assert data["id"] == 1
    assert data["username"] == "testuser1"
    assert data["email"] == "testuser1@example.com"


def test_user_get():
    response = client.get("/v1/users/1")

    data = response.json()

    assert data["id"] == 1
    assert data["username"] == "testuser1"
    assert data["email"] == "testuser1@example.com"


def test_user_delete():
    response = client.delete("/v1/users/1")

    assert response.status_code == 204


def test_track_create():
    response = client.post(
        "/v1/tracks",
        json={"title": "testtitle1", "artist": "testartist1", "isrc": "testisrc1"},
    )

    assert response.status_code == 201


def test_track_list():
    response = client.get("/v1/tracks")

    data_list = response.json()

    assert len(data_list) == 1

    data = data_list[0]

    assert data["id"] == 1
    assert data["title"] == "testtitle1"
    assert data["artist"] == "testartist1"
    assert data["isrc"] == "testisrc1"


def test_track_get():
    response = client.get("/v1/tracks/1")

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "testtitle1"
    assert data["artist"] == "testartist1"
    assert data["isrc"] == "testisrc1"


def test_track_delete():
    response = client.delete("/v1/tracks/1")

    assert response.status_code == 204
