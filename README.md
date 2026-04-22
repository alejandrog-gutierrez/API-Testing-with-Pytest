# API Automation Testing Project – JSONPlaceholder (/posts)

## What is this?

This project is an automated API testing suite for validating RESTful behavior of the mock API JSONPlaceholder /posts endpoint using Python, Pytest, and Requests.

---

## Product / Feature Under Test

The `/posts` endpoint of the JSONPlaceholder REST API, including the following operations:

![GET](https://img.shields.io/badge/GET-Fetch%20Posts%20Data-brightgreen)
![POST](https://img.shields.io/badge/POST-Create%20New%20Post-00bcd4)
![PUT](https://img.shields.io/badge/PUT-Full%20Update%20Post-ffeb3b)
![PATCH](https://img.shields.io/badge/PATCH-Partial%20Update%20Post-orange)
![DELETE](https://img.shields.io/badge/DELETE-Delete%20Post-red)

---

## Objective

The objective of this project was to validate the behavior of the `/posts` endpoint by testing its CRUD operations under different input scenarios in a mock REST API.

The goal was to detect issues that could lead to production problems such as inconsistent responses, incorrect handling of data, or unreliable API behavior, which in real systems could result in data corruption, poor user experience, or operational failures.

---

## Scope

### Included:
- Testing of the `/posts` endpoint, focusing on CRUD operations (GET, POST, PUT, PATCH, DELETE).
- Validation of response behavior, status codes, and data consistency across requests.
- User filtering via `/posts?userId=`.
- Positive, negative, boundary, and exploratory scenarios based on available API behavior.

### Not included:
- Authentication testing, since JSONPlaceholder does not implement auth or security layers.
- Performance or load testing, as the scope was focused on functional validation only.
- Strict data validation rules, since the API does not enforce backend constraints or persistence.
- Database or persistence validation, because responses are simulated and not stored permanently.

---

## Project Structure / Artifacts

The test framework is organized in a modular way, with a clear separation of responsibilities to keep things maintainable and easy to scale over time.

 - Test Layer (Pytest): This is where all the test cases live. It covers the /posts resource and checks different scenarios like positive flows, negative cases, boundaries, and exploratory testing.
 - API Client Layer: This layer handles all the HTTP requests using the Requests library. Instead of calling the API directly inside the tests, I wrapped the requests into reusable methods (GET, POST, PUT, PATCH, DELETE).
 - Helper Layer: This includes small utilities like payload generation, response checks, and test data handling. The idea here was to avoid repeating code and keep the tests cleaner.

Overall, the idea was to keep test logic focused on behavior, while everything related to API calls and supporting logic stays separated and reusable.

---

## Key Decisions

 - Helpers were implemented to reduce code duplication, improve readability, and support scalability, while keeping test cases focused on behavior rather than implementation details.
 - A clear separation between the API client and test files was applied to avoid tight coupling and improve maintainability. Helper functions were created for each type of request, making them easily reusable and called within test cases.
 - Pytest and Requests were selected as the main tools for this project due to their suitability for API testing, flexibility, and ease of integration in automated test frameworks.

---

## Results

 - The test suite was built and executed against the /posts endpoint, covering around 20–30 test cases across GET, POST, PUT, PATCH, and DELETE operations. The focus was on checking response behavior, status codes, and consistency between request payloads and API responses.

 - During testing, I validated positive flows, invalid inputs, boundary conditions, and exploratory scenarios. Since JSONPlaceholder is a mock API, most responses are simulated rather than truly validated or persisted, which meant that some negative scenarios behaved more like exploratory checks instead of strict failures.

 - Even with those limitations, the suite helped me observe how the API responds under different conditions, and gave me a clearer understanding of CRUD behavior, response consistency, and test coverage strategy.

The structure also made it easier to run and extend tests, since API calls and test logic were separated from reusable helpers.

---

## What Could Be Improved

 - Add more parametrized tests to reduce repetition, especially for similar CRUD scenarios.
 - Improve helper flexibility, since a few tests still required raw or “manual” requests outside the utility functions.
 - Better separation of helpers from the start (they were created as needed during development, which led to some structure decisions being reactive rather than planned).
 - Expand test coverage beyond JSONPlaceholder to a real API with proper validation rules and data persistence.
 - Introduce more structured negative testing, since the mock nature of the API limited strict validation behavior.

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
git clone <https://github.com/alejandrog-gutierrez/API-Testing-with-Pytest>

### 2. Move into the project directory
cd API-Testing-with-Pytest

### 3. Install dependencies
pip install requests

### 4. Run the test suite
pytest tests/test_posts.py

---

## Contact me!
You liked my work? Let´s talk about working together!

[![Email](https://img.shields.io/badge/Email-aggdl2428%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:aggdl2428@gmail.com)
[![Phone](https://img.shields.io/badge/Phone-%2B507%2067848724-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](tel:+50767848724)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Alejandro%20Guti%C3%A9rrez-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alejandro-gutierrez-deleon-qa)
