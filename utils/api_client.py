import requests
BASE_URL = "https://jsonplaceholder.typicode.com/"
def get_all_posts():
    return requests.get(f"{BASE_URL}/posts")
def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")
def create_post(payload):
    return requests.post(f"{BASE_URL}/posts", json=payload)
def payload_builder(title, body, userId):
    return {"title": title, "body": body, "userId": userId}
def get_posts_by_user(userId):
    return requests.get(f"{BASE_URL}/posts",params={'userId':userId})
def delete_post(id):
    return requests.delete(f"{BASE_URL}/posts/{id}")
def patch_post(id, title, body, userId):
    return requests.patch(f"{BASE_URL}/posts/{id}", json={"title": title, "body": body, "userId": userId})