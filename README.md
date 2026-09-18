# Playwright Ecommerce Automation Framework

## Overview

This project is an **Ecommerce automation framework developed using Playwright with Python and Pytest**.

The framework follows the **Page Object Model (POM)** design pattern and is designed to support maintainable, reusable, and scalable automated testing.

The framework covers both **UI and API automation**, including ecommerce workflows such as login, product search, product selection, cart management, checkout, order validation, and API validation.

---

## Tech Stack

* Python
* Playwright
* Pytest
* Page Object Model (POM)
* Playwright APIRequestContext
* Pytest HTML Reporting
* Allure Reporting
* Git & GitHub
* GitHub Actions (CI/CD)
* Python-dotenv

---

## Project Structure

```text
Playwright_Ecommerce/
│
├── config/
│   └── Application configuration and environment settings
│
├── data/
│   └── Test data and API payloads
│
├── pages/
│   └── Page Object classes
│
├── tests/
│   ├── api/
│   │   └── API test cases
│   │
│   └── UI test cases
│
├── utils/
│   └── Reusable utility functions
│
├── conftest.py
│   └── Pytest fixtures and test configuration
│
├── pytest.ini
│   └── Pytest configuration and markers
│
├── requirements.txt
│   └── Project dependencies
│
├── .env
│   └── Local environment variables (not committed to Git)
│
├── .gitignore
│   └── Files and folders excluded from Git
│
└── README.md
    └── Project documentation
```

---

## Features

### UI Automation

* Playwright-based UI automation
* Python + Pytest framework
* Page Object Model implementation
* Reusable page methods and utilities
* Configurable test environments
* Test data management
* Pytest fixtures
* Cross-browser execution support
* Login automation
* Product search and selection
* Cart validation
* Checkout workflow
* Order validation

### API Automation

* API automation using Playwright `APIRequestContext`
* GET, POST, PUT and DELETE requests
* Positive and negative API scenarios
* Query parameter validation
* Response header validation
* Response body validation
* Response status code validation
* Response time validation
* Parameterized API testing
* API chaining
* Authentication header handling
* Reusable API fixtures

### Reporting & Debugging

* Pytest HTML reporting
* Allure reporting
* Playwright traces
* Screenshots for failed tests
* Optional video recording
* Test artifacts uploaded through GitHub Actions

### CI/CD

* GitHub Actions integration
* Automated test execution on push and pull request
* Automatic dependency installation
* Playwright browser installation
* Environment variable configuration
* Automated HTML report generation
* Test artifact collection

---

## Prerequisites

Make sure the following are installed:

* Python 3.x
* Git
* VS Code or any preferred IDE

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Shradhanjalli-Priyadarshini/Playwright_Ecommerce.git
```

### Navigate to the project directory

```bash
cd Playwright_Ecommerce
```

### Create a virtual environment

```bash
python -m venv test_env
```

### Activate the virtual environment

**Windows:**

```bash
test_env\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright browsers

```bash
playwright install
```

---

## Environment Configuration

API configuration is maintained using environment variables.

Create a `.env` file in the project root:

```text
API_BASE_URL=https://jsonplaceholder.typicode.com
API_TOKEN=demo-token
```

The `.env` file is excluded from Git using `.gitignore`.

For GitHub Actions, the required API environment variables are configured directly in the workflow.

---

## Running Tests

### Run the complete test suite

```bash
pytest
```

### Run tests with verbose output

```bash
pytest -v
```

### Run only API tests

```bash
pytest -m api
```

### Run a specific test file

```bash
pytest tests/api/test_api.py
```

### Run tests for a specific environment

```bash
pytest --env=qa
```

### Run tests with HTML reporting

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Test Coverage

The framework currently contains **26 automated tests** covering UI and API scenarios.

### UI Test Scenarios

* User login
* Product search
* Product selection
* Add product to cart
* Cart validation
* Checkout workflow
* Order validation

### API Test Scenarios

* GET request validation
* POST request validation
* PUT request validation
* DELETE request validation
* Invalid resource validation
* Query parameter validation
* Response header validation
* Response time validation
* Parameterized API testing
* API chaining
* Authentication header handling

---

## Reports

### HTML Reporting

The framework generates HTML test execution reports using **pytest-html**.

Run:

```bash
pytest --html=reports/report.html --self-contained-html
```

The generated report can be opened in a browser to review test execution results.

### Allure Reporting

Allure results can be generated using:

```bash
pytest --alluredir=reports/allure-results
```

To open the Allure report:

```bash
allure serve reports/allure-results
```

---

## CI/CD Reporting

GitHub Actions automatically executes the complete test suite on **push and pull request** events.

The CI pipeline:

1. Checks out the repository
2. Sets up Python
3. Installs project dependencies
4. Installs Playwright browsers
5. Configures required environment variables
6. Executes the Pytest suite
7. Generates the HTML test report
8. Uploads test artifacts

Artifacts include:

* HTML test report
* Playwright traces
* Screenshots for failed tests
* Videos when video recording is enabled

The current CI pipeline successfully executes **26 automated tests**.

---

## Configuration

Application and environment-specific configuration is maintained separately from the test cases.

This allows the same test suite to be executed against different environments without modifying the test scripts.

Pytest markers are configured in `pytest.ini`, including:

```text
smoke
regression
login
cart
checkout
api
```

---

## Future Enhancements

Planned improvements include:

* Parallel test execution
* Additional API coverage
* Improved test data management
* Docker-based test execution
* Expanded cross-browser execution
* Advanced CI/CD pipeline configuration

---

## Author

**Shradhanjalli Priyadarshini**

QA Engineer | Automation Testing

**Skills:** Python, Playwright, Pytest, Selenium, API Testing, SQL, Mabl and AI-assisted Testing
