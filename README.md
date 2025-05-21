# Overview
This repository contains a UI automation testing the Basic Calculator functionality website using:

- 'Prototype' Calculator Build (https://testsheepnz.github.io/BasicCalculator.html)
- Python
- Selenium WebDriver (Chrome & Firefox both are options)
- Pytest Tests for both positive and negative scenarios

# Folder Structure
```
NateHogsten-automation-assessment/
│       
├── pytest.ini               # pytest configuration (logging)
├── requirements.txt         # Python dependencies
├── README.md                # Documentation
├── .pytest_cache            # Cache for pytest
│
├── tests/
│     ├── conftest.py          # Browser setup (Chrome/Firefox) via pytest fixture
│     ├── positive_test.py     # Positive (valid-input) test cases
│     └── negative_test.py     # Negative (invalid-input) test cases
│     └── test_utils.py        # Defines parameters for test data
│     └──pages/
│         └── calculator_page.py   # Page object for the calculator UI
│         └── math_operations.py   # Python mathematical functions: add, subtract, multiply, divide, concatenate
```

# Installation & Setup
Create & activate virtual environment:

```
python -m venv venv
```

- macOS/Linux
```
source venv/bin/activate
```
------ OR -------
- Windows (PowerShell)
```
.\venv\Scripts\Activate.ps1
```

# Install dependencies

- Ensure Chrome or Firefox is installed

```
python -m pip install -r requirements.txt
```

# Configuration
(tests/conftest.py) || Defines a --browser pytest flag and loads Selenium browser driver

(tests/test_utils.py) || Defines parameters for positive and negative test cases

(tests/pytest.ini) [Optional] || Add any markers or default command-line options here.

# Run all tests on default Chrome browser
```
python -m pytest --browser=chrome
```
# Or specify Firefox
```
python -m pytest --browser=firefox
```

# Page Objects & Operations
(tests/pages/calculator_page.py) || Encapsulates all interactions with the calculator:
- Loading the page
- Entering values
- Selecting operation & integer-only checkbox
- Clicking “Calculate”
- Waiting for and retrieving result or error

(tests/pages/math_operations.py) || Performs the mathematical tests for comparison
- add
- subtract
- multiply
- divide
- concatenate

# Tests
1. Positive Test (tests/positive_test.py)

- Loads in postiive test case parameters from test_utils
- Covers addition, subtraction, multiplication, division, concatenation.
Verifies:
- No error message
- Exact string match of the calculator’s output vs. our math_operations result (with integer rounding when “Integers only” is checked).

2. Negative Test (tests/negative_test.py)

- Same as positive test but with negative test case parameters from test_utils with cases that fail on the calculator

# Design Notes

1. Maintainability

- Clear Separation of Concerns & Page Object Model (POM)
- All locator definitions and page-specific actions live in calculator_page.py. If an element’s ID or the page URL changes, you only update that one file—not every test.
- Centralized Fixture :The driver setup/teardown lives in conftest.py. Browser configuration changes (e.g. headless flags, timeouts) happen in one place.
- Readable & self-Documenting Tests
- Each test file is small and focused, with descriptive names (e.g. positive_test.py)
- Docstrings  and comments explain intent so new contributors quickly grasp what each test covers.

2. Reusability

- All tests pull in the same shared driver fixture (tests/conftest.py).
- Can declare different browser to use with the --browser='browser_name' flag 
- Parametrization of calculate() method from (tests/pages/calculator_page.py) can be called from any test without rewriting input/submit logic.
- Single-Responsibility Tests: Each test file does one thing, mix-and-match them without tangled dependencies.
- Test data for all tests is defined in parameters in (tests/test_utils.py)

3. Scalability
- Easy to add new test cases: Simply add another tuple to a parametrized test (e.g. (9, 9, "2", "81")) or create new test files for special flows.
- Supports parallel execution of tests because tests don’t share state
