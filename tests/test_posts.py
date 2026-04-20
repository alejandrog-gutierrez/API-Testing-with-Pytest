from utils.api_client import get_post, get_all_posts, create_post, payload_builder, get_posts_by_user, delete_post, \
    patch_post

def test_get_all_posts():
    response = get_all_posts()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data,list)
    assert len(data) > 0

def test_post_structure():
    response = get_all_posts()
    assert response.status_code == 200
    data = response.json()
    for post in data:
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post

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
    assert data == {} or data is None

def test_post_above_upper_limit():
    response = get_post(101)
    assert response.status_code == 404
    data = response.json()
    assert data == {} or data is None

def test_post_negative_id():
    response = get_post(-1)
    assert response.status_code == 404
    data = response.json()
    assert data == {} or data is None

def test_create_post():
    payload = payload_builder("Test Post", "This is a test post and should be treated as such", 1)
    response = create_post(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

def test_invalid_title():
    payload = payload_builder(1, "This is a test post and should be treated as such", 1)
    response = create_post(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

def test_invalid_body():
    payload = payload_builder("Test",1, 1)
    response = create_post(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

def test_invalid_userId():
    payload = payload_builder("Test Post", "This is a test post and should be treated as such","A" )
    response = create_post(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

def test_create_post_invalid():
    payload = payload_builder("","", None)
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

def test_get_posts_by_user_id():
    response = get_posts_by_user(1)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for post in data:
        assert post["userId"] == 1

def test_get_post_by_invalid_user():
    response = get_posts_by_user(11)
    assert response.status_code == 200
    data = response.json()
    assert data == []

def test_delete_post():
    response = delete_post(1)
    assert response.status_code == 200
    data = response.json()
    assert data == {}

def test_patch_post():
    response = patch_post(1,"Alejandro","This is a test",1)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Alejandro"
    assert data["userId"] == 1
    assert data["body"] == "This is a test"
    assert data["id"] == 1
