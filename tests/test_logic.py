from app.main import parse_and_average


def test_parse_and_average_happy():
    assert parse_and_average("1,2,3,4") == "Average: 2.5000"


def test_parse_and_average_spaces_and_commas():
    assert parse_and_average("1,  2  3,4") == "Average: 2.5000"


def test_parse_and_average_empty():
    assert parse_and_average("") == "Error: no values provided"
    assert parse_and_average(None) == "Error: no values provided"


def test_parse_and_average_non_numeric():
    assert parse_and_average("1, a, 3") == "Error: non-numeric value detected"


def test_parse_and_average_all_invalid_after_filter():
    # tokens become empty after filtering empties (unlikely but defensive)
    assert parse_and_average(", ,   ") == "Error: no values provided"


def test_parse_and_average_precision():
    # 0.1 + 0.2 + 0.3 = 0.6 / 3 = 0.2 (format to 4 decimals). A tolerance-based
    # assertion is unnecessary because we format using mean() and standard
    # rounding; this checks the string result.
    assert parse_and_average("0.1 0.2 0.3") == "Average: 0.2000"
