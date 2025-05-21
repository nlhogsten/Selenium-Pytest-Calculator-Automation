import pytest
from pages.math_operations import add, subtract, multiply, divide, concatenate

# Positive test cases:
# (a, b, op_value, op_func, integer_only, expect_error, expected_str_or_None)
POSITIVE_CASES = [
    # ─────── Positive cases ───────
    (2.5,   1.3, "0", add,      False, False, "3.8"),
    (2.5,   1.3, "0", add,      True,  False, "3"),
    (2,     3,   "0", add,      False, False, "5"),
    (2,     3,   "0", add,      True,  False, "5"),

    (5.5,   2.2, "1", subtract, False, False, "3.3"),
    (5.5,   2.2, "1", subtract, True,  False, "3"),
    (10,    4,   "1", subtract, False, False, "6"),
    (10,    4,   "1", subtract, True,  False, "6"),

    (2.5,   1.0, "2", multiply, False, False, "2.5"),
    (2.5,   1.0, "2", multiply, True,  False, "2"),
    (6,     7,   "2", multiply, False, False, "42"),
    (6,     7,   "2", multiply, True,  False, "42"),

    (12,    3,   "3", divide,   False, False, "4"),
    (12,    3,   "3", divide,   True,  False, "4"),
    (5,     2,   "3", divide,   False, False, "2.5"),
    (5,     2,   "3", divide,   True,  False, "2"),
    
    # concatenate just returns raw Python result
    (4.5, 6.2,   "4", concatenate, False, False, "4.56.2"),
    (4,    6,    "4", concatenate, False, False, "46"),
    ("foo","bar","4", concatenate, False, False, "foobar"),
]

# Negative test cases:
# (a, b, op_value, op_func, integer_only, expect_error, expected_str_or_None)
NEGATIVE_CASES = [
    # ─────── Positive cases ───────
    (2.5,   1.3, "0", add,      False, False, "3.8"),
    (2.5,   1.3, "0", add,      True,  False, "3"),
    (2,     3,   "0", add,      False, False, "5"),
    (2,     3,   "0", add,      True,  False, "5"),

    (5.5,   2.2, "1", subtract, False, False, "3.3"),
    (5.5,   2.2, "1", subtract, True,  False, "3"),
    (10,    4,   "1", subtract, False, False, "6"),
    (10,    4,   "1", subtract, True,  False, "6"),

    (2.5,   1.0, "2", multiply, False, False, "2.5"),
    (2.5,   1.0, "2", multiply, True,  False, "2"),
    (6,     7,   "2", multiply, False, False, "42"),
    (6,     7,   "2", multiply, True,  False, "42"),

    (12,    3,   "3", divide,   False, False, "4"),
    (12,    3,   "3", divide,   True,  False, "4"),
    (5,     2,   "3", divide,   False, False, "2.5"),
    (5,     2,   "3", divide,   True,  False, "2"),
    
    # concatenate just returns raw Python result
    (4.5, 6.2,   "4", concatenate, False, False, "4.56.2"),
    (4,    6,    "4", concatenate, False, False, "46"),
    ("foo","bar","4", concatenate, False, False, "foobar"),

        # ─────── Negative cases ───────
    # non-numeric in numeric op
    ("abc", 5,   "0", add,      False, True, None),
    # decimals with integer-only
    (2.5,   1.2, "0", add,      True,  True, None),
    # division by zero
    (10,    0,   "3", divide,   False, True, None),
    # totally invalid op code
    (2,     3,   "999", add,    False, True, None),
]

# Parameter templates for entry into positive_test.py and negative_test.py
parametrize_positive = pytest.mark.parametrize(
    "a,b,op_value,op_func,integer_only,expect_error,expected",
    POSITIVE_CASES
)
parametrize_negative = pytest.mark.parametrize(
    "a,b,op_value,op_func,integer_only,expect_error,expected",
    NEGATIVE_CASES
)