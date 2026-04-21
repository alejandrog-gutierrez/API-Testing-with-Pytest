# API Automation Testing Project – JSONPlaceholder (/posts)

## What is this?

This project is an automated API testing suite built with Python, Pytest, and Requests. It focuses on validating the behavior of a REST API by executing different types of tests, including functional, negative and exploratory scenarios using the mock platform JSONPlaceholder.

---

## Product / Feature Under Test

The `/posts` endpoint of the JSONPlaceholder REST API, including the following operations:

- GET (single post, all posts, posts by user) (`get_post` `get_all_posts` `get_post_by_user`)
- POST (create posts) (`payload_builder` `create_post`)
- PUT (replace posts) (`put_post`)
- PATCH (partial updates) (`patch_post`)
- DELETE (remove posts) (`delete_post`)

---

## Objective

The objective of this project is to validate API behavior under different test scenarios and build a reusable and scalable test automation framework using Python, Pytest, and Requests

---

## Scope

### Included:
- Testing of `/posts` endpoint
- Validation of `GET`, `POST`, `PUT`, `PATCH`, `DELETE` methods
- User-based filtering via `/posts?userId=`
- Positive, edge, and exploratory test cases

### Not included:
- Authentication testing (not supported by the API)
- Performance testing
- Strict data validation rules (API does not enforce constraints)
- Persistent data validation (API is mock-based)

---

## Project Structure / Artifacts

The project includes:

- Test suite built with Pytest
- API client module containing reusable request functions
- Helper functions for:
  - Payload generation
  - Request execution
  - Response validation
  - Negative and exploratory scenarios
- Organized separation between API logic and test logic

---

## Key Decisions

- Helpers were implemented to reduce code duplication and improve readability and scalability.
- Separation between API client and test files was used to avoid tight coupling and improve maintainability.
- Pytest and Requests were chosen because they are the tools used during development and learning of this project.

---

## Results

The project successfully covers the main endpoints of the API and validates different types of scenarios using both functional and exploratory testing.

A modular and scalable test structure was implemented, making it easier to maintain and extend the test suite in the future.

---

## What Could Be Improved

- Implement parametrized tests to reduce repetition
- Improve assert strictness and validation depth
- Add more structured negative test handling
- Further optimize test organization and separation of concerns
- Introduce testing against APIs with real validation rules

---

## Tools Used In This Project

![Python](https://img.shields.io/badge/Python-6A5ACD?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-1E90FF?style=for-the-badge&logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-40E0D0?style=for-the-badge&logo=python&logoColor=black)

---

## Test Design Methodologies

![API Testing](https://img.shields.io/badge/API%20Testing-4CAF50?style=for-the-badge)
![Functional Testing](https://img.shields.io/badge/Functional%20Testing-FFD700?style=for-the-badge&logoColor=black)
![Negative Testing](https://img.shields.io/badge/Negative%20Testing-FF0000?style=for-the-badge)
![Exploratory Testing](https://img.shields.io/badge/Exploratory%20Testing-FFFFFF?style=for-the-badge&logoColor=black)

---

## Notes

JSONPlaceholder is a mock API. It does not enforce strict validation rules or persist changes, so tests focus on response structure, behavior, and consistency rather than backend enforcement.

---

## How to Run Tests

### 1. Clone the repository
git clone <repo-url>

### 2. Move into the project directory
cd <project-folder>

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the test suite
pytest tests/test_posts.py