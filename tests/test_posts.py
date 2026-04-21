from utils.api_client import get_post, get_all_posts, create_post, payload_builder, get_posts_by_user, delete_post, \
    put_post, patch_post

def test_get_all_posts():
    response = get_all_posts()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data,list)
    assert len(data) > 0 #This test validates that there is data in the endpoint "POSTS"

def test_post_structure():
    response = get_all_posts()
    assert response.status_code == 200
    data = response.json()
    for post in data:
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post #This test validates the structure of each entry of the dictonary

def assert_post_valid(post):
    response = get_post(post)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post
    return response #This helper evokes the function "get_post" from "api_client"
                    #and replaces the "post_id" variable with an input (post) and validates
                    #the status code of the request, which should be 200 for existing posts

#Positive tests
def test_post_in_lower_range_limit():
    assert_post_valid(1)

def test_post_in_lower_valid_range():
    assert_post_valid(2)

def test_post_in_upper_valid_range():
    assert_post_valid(99)

def test_post_in_upper_range_limit():
    assert_post_valid(100)

def assert_post_invalid(post):
    response = get_post(post)
    assert response.status_code == 404
    data = response.json()
    assert data == {} #This helper uses out of range or invalid values for "POSTS"
    return response   #and validates that the status code for the request is "404"
                      #The API returns an empty dictionary for data ({})

#Negative tests
def test_post_below_lower_limit():
    assert_post_invalid(0)

def test_post_above_upper_limit():
    assert_post_invalid(101)

def test_post_negative_id():
    assert_post_invalid(-1)

def test_post_null_id():
    assert_post_invalid(None)

def create_valid_post(title, body, userId):
    payload = payload_builder(title, body, userId) #This helper builds a body and validates
    response = create_post(payload)                #the status code for the request (Always 201 no matter the data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"] #Here I validate that the values within the keys
    assert data["body"] == payload["body"]   #on the request's body are the same as on the response
    assert data["userId"] == payload["userId"]
    assert "id" in data #The API always return a 201 code with an "id" key for the "NEW" post
    return data         #I'm validating that the key EXISTS.
#Positive test for post
def test_create_post():
    create_valid_post("Test Post", "This is a test post and should be treated as such", 1)

def test_valid_title():
    create_valid_post("Alejandro", "This is a test post and should be treated as such", 1)

def test_valid_body():
    create_valid_post("Test Post", "This is a test post and should be treated as such 123 @-.,¿$%&/( ыддлгфрюьжщл", 1)

def test_valid_userId():
    create_valid_post("Test Post", "This is a test post and should be treated as such", 2)

#Exploratory cases for title
def test_title_accepts_numbers():
    create_valid_post(12345, "This is a test post and should be treated as such", 1)

def test_title_accepts_symbols():
    create_valid_post(",.-{+´@", "This is a test post and should be treated as such", 1)

def test_title_accepts_other_language():
    create_valid_post("ыддлгфрюьжщл", "This is a test post and should be treated as such", 1)

def test_title_accepts_too_short():
    create_valid_post("A", "This is a test post and should be treated as such", 1)

def test_title_accepts_too_long():
    create_valid_post("A"*1000, "This is a test post and should be treated as such", 1)

def test_title_accepts_null():
    create_valid_post("", "This is a test post and should be treated as such", 1)

def test_title_accepts_none():
    create_valid_post(None, "This is a test post and should be treated as such", 1)

#Exploratory cases for body
def test_body_accepts_too_short():
    create_valid_post("Test","a", 1)

def test_body_accepts_too_long():
    create_valid_post("Test","A"*1000 , 1)

def test_body_accepts_null():
    create_valid_post("Test","", 1)

def test_body_accepts_none():
    create_valid_post("Test",None, 1)

#Exploratory cases for userId
def test_userID_accepts_str():
    create_valid_post("Test Post", "This is a test post and should be treated as such","A" )

def test_userID_accepts_empty():
    create_valid_post("Test Post", "This is a test post and should be treated as such","")

def test_userID_accepts_none():
    create_valid_post("Test Post", "This is a test post and should be treated as such",None)

def test_userID_accepts_symbols():
    create_valid_post("Test Post", "This is a test post and should be treated as such","@%&/()" )

def test_userID_accepts_another_language():
    create_valid_post("Test Post", "This is a test post and should be treated as such","ыддлгфрюьжщл" )

def test_userID_accepts_too_long():
    create_valid_post("Test Post", "This is a test post and should be treated as such","2"*1000 )

def test_post_accepts_empty_fields():
    create_valid_post("","", None)

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
    assert "id" in data #Although, there is no literature on field limitations, I decided to make
                        #exploratory testing in order to review the behavior of the API

def test_get_posts_by_user_id():
    response = get_posts_by_user(1)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for post in data:
        assert post["userId"] == 1 #This test validates that the user #1 has posts related to it
                                   #it validates the existence of a dictionary and validates that
                                   #every single post has the userId == 1

def test_get_post_by_invalid_user():
    response = get_posts_by_user(11)
    assert response.status_code == 200
    data = response.json()
    assert data == [] #In this test something curious happens, since the endpoint exists but
                      #there is no value associated to the search, it returns a "[]" instead
                      #of a "{}" associated to a non-existing endpoint!

def delete_a_post(post):
    response = delete_post(post)
    assert response.status_code == 200
    data = response.json()
    assert data == {}
    return response #It's worth noting that the API will always return a 200 code
                    #according to JSONPlaceholder literature, I designed the cases
                    #covering exploratory scenarios, not validating status codes in this instance!

def test_delete_valid_post():
    delete_a_post(1)

def test_delete_invalid_post():
    delete_a_post(999)

def test_delete_negative_post():
    delete_a_post(-1)

def test_delete_null_post():
    delete_a_post(None)

def test_delete_post_0():
    delete_a_post(0)

def test_put_post():
    response = put_post(1,"Alejandro","This is a test",9)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Alejandro"
    assert data["userId"] == 9
    assert data["body"] == "This is a test"
    assert data["id"] == 1 #This test validates that after a change in all fields
                           #With a PUT request, the backend returns the inputted values
                           #prior to the test

def test_patch_post_title():
    original = get_post(1).json()
    response = patch_post(1,"Alejandro")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Alejandro"
    assert data["id"] == original["id"]
    assert data["body"] == original["body"]      #This test validates that ONLY one of the keys (title) change
    assert data["userId"] == original["userId"]  #after making a PATCH request by comparing the original
                                                #value (get.post(1)) to the response (id, body, userId)

