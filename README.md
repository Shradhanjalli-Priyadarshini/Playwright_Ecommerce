Playwright Ecommerce Automation Framework
Overview

This project is an Ecommerce UI automation framework developed using Playwright with Python and Pytest.

The framework follows the Page Object Model (POM) design pattern and is designed to support maintainable, reusable, and scalable automated tests.

The project covers common Ecommerce workflows such as login, product search, product selection, cart management, checkout, and order validation.

Tech Stack
Python
Playwright
Pytest
Page Object Model (POM)
HTML Reporting
Git & GitHub
GitHub Actions (CI/CD)

Project Structure
Playwright_Ecommerce/
│
├── config/
│   └── Application configuration and environment settings
│
├── data/
│   └── Test data
│
├── pages/
│   └── Page Object classes
│
├── tests/
│   └── Test cases
│
├── utils/
│   └── Reusable utility functions
│
├── conftest.py
│   └── Pytest fixtures and test configuration
│
├── pytest.ini
│   └── Pytest configuration
│
├── requirements.txt
│   └── Project dependencies
│
├── .gitignore
│   └── Files and folders excluded from Git
│
└── README.md
    └── Project documentation
Features
Playwright-based UI automation
Python + Pytest framework
Page Object Model implementation
Reusable page methods and utilities
Configurable test environments
Test data management
Pytest fixtures
Cross-browser automation support
Maintainable and reusable test structure
GitHub Actions CI/CD integration
Automated test execution on push and pull request
HTML test reporting
Test artifacts including reports, traces, screenshots and videos

Prerequisites

Make sure the following are installed:

Python 3.x
Git
VS Code or any preferred IDE
Installation

Clone the repository:

git clone https://github.com/Shradhanjalli-Priyadarshini/Playwright_Ecommerce.git

Navigate to the project directory:

cd Playwright_Ecommerce

Create and activate a virtual environment:

python -m venv venv

Windows:

venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

Install Playwright browsers:

playwright install
Running Tests

Run the complete test suite:

pytest

Run tests with verbose output:

pytest -v

Run a specific test file:

pytest tests/test_login.py

Run tests for a specific environment:

pytest --env=qa
Test Scenarios

The framework is designed to automate Ecommerce scenarios including:

User login
Product search
Product selection
Add product to cart
Cart validation
Checkout workflow
Order validation

## Reports

The framework generates HTML test execution reports using **pytest-html**.

Run tests with HTML reporting:

pytest --html=reports/report.html --self-contained-html

The HTML report can be opened in a browser to review test execution results.

### CI/CD Reporting

GitHub Actions automatically executes the test suite and generates the HTML report.

Test artifacts are uploaded after every CI run and include:

- HTML test report
- Playwright traces
- Screenshots for failed tests
- Videos when video recording is enabled

Configuration

Application and environment-specific configuration is maintained separately from test cases.

This allows the same test suite to be executed against different environments without modifying the test scripts.

Future Enhancements

Planned improvements include:

Allure reporting
Parallel test execution
Additional API automation
Improved test data management
Cross-browser execution
Docker-based test execution
Author

Shradhanjalli Priyadarshini

QA Engineer | Automation Testing

Skills: Python, Playwright, Pytest, Selenium, API Testing, SQL and AI-assisted Testing
