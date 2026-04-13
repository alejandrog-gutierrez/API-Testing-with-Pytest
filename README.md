# API Testing Project – JSONPlaceholder

## 📌 Overview

The objective of this project is to validate the behavior of the post retrieval and creation endpoints.
It includes positive scenarios, boundary conditions, and negative cases, ensuring the structure and consistency of API responses.

---

## 🔗 Endpoints Tested

* `GET /posts`
* `GET /posts/{id}`
* `POST /posts`

---

## 🧪 Testing Scope

### ✔ Scenarios Covered

* Positive scenarios (valid requests)
* Negative scenarios (invalid or unexpected input)
* Boundary testing (IDs at limits and out-of-range)
* Empty and missing field cases

---

## 🔍 Validations Performed

* Status code validation
* Response structure validation
* Required field presence (`userId`, `id`, `title`, `body`)
* Data type validation
* Data consistency between request payload and response

---

## ⚠️ API Limitations

This project uses JSONPlaceholder, which is a mock API.

The API does not validate request payloads:

* POST requests always return `201 Created`
* Invalid or incomplete data is still accepted

Because of this:

* Negative tests cannot rely on expected error codes (e.g., `400` or `404`)
* Tests focus on analyzing response behavior rather than enforcing validation failures

---

## 🧠 Testing Approach

Due to the API limitations, the testing strategy is adapted to:

* Validate actual system behavior instead of ideal behavior
* Ensure consistency in API responses
* Identify behaviors that would be considered defects in a real production system

---

## 🛠️ Technologies Used

* Python
* Pytest
* Requests

---

## ▶️ How to Run

```bash
pip install pytest requests
pytest
```

---

## 📈 Future Improvements

* Add parameterized tests using Pytest
* Implement fixtures for better test structure
* Add schema validation
* Test against a real API with proper validation rules
* Integrate into a CI/CD pipeline

---

## 👤 Author

QA Automation practice project focused on API testing fundamentals and test design.
