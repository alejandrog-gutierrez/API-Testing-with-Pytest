import requests
BASE_URL = "https://jsonplaceholder.typicode.com/"
def test_get_homepage():
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200
    print(response.status_code)

def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    first_post = data[0]
    assert "userId" in first_post
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post

def test_post_lower_limit():
    response = get_post(1)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_post_upper_limit():
    response = get_post(100)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 100

def test_post_below_lower_limit():
    response = get_post(0)
    assert response.status_code == 404
    data = response.json()
    assert data == {}

def test_post_above_upper_limit():
    response = get_post(101)
    assert response.status_code == 404
    data = response.json()
    assert data == {}

def test_post_negative_id():
    response = get_post(-1)
    assert response.status_code == 404
    data = response.json()
    assert data == {} or data is None

def create_post(payload):
    return requests.post(f"{BASE_URL}/posts", json=payload)

def payload_build(title, body, userId):
    return {"title": title, "body": body, "userId": userId}

def test_create_post():
    payload = payload_build("Test Post", "This is a test post and should be treated as such", 1)
    response = create_post(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

def test_create_post_invalid():
    payload = payload_build("","", None)
    response = create_post(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] is None
    assert "id" in data

def test_missing_field():
    payload = {
        "title": "Test",
        "userId": 1
    }
    response = create_post(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["userId"] == payload["userId"]
    assert "body" not in payload
    assert "id" in data