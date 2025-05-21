import time
import logging
from pages.calculator_page import CalculatorPage
from tests.test_utils import parametrize_positive

# enable pytest to show INFO logs to console
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

PAUSE_BETWEEN = 1.0  # seconds

# Load in paramters and run claculator test
@parametrize_positive
def test_calculator(a, b, op_value, op_func, integer_only, expect_error, expected, driver):
    """
    Drives the calculator UI for both positive and negative cases:
        - expect_error=False → answer must exactly match `expected`, error must be None
        - expect_error=True  → answer must be empty (or None), error must be non-empty
    """
    page = CalculatorPage(driver)
    page.load()

    logger.info(f"\n---\nCase: a={a!r}, b={b!r}, op={op_value}, integer_only={integer_only}")

    rv = page.calculate(a, b, op_value, integer_only)
    answer, error = rv["answer"], rv["error"]
    logger.info(f"Browser returned → answer={answer!r}, error={error!r}")

    if expect_error:
        # Negative: no numeric answer, but an error message must appear
        assert not answer, f"Expected no numeric result, but got {answer!r}"
        assert error,       f"Expected an error message for inputs {a!r}, {b!r}"
    else:
        # Positive: exact match, and no error
        assert error is None, f"Unexpected error for valid inputs: {error!r}"
        assert answer == expected, \
            f"Expected answer {expected!r}, but got {answer!r}"

    # brief pause so each iteration is visible on screen
    time.sleep(PAUSE_BETWEEN)






