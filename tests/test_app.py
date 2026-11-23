import pytest

from src.app import normalize_title, summarize_tests, validate_project_name


def test_validate_project_name():
    assert validate_project_name("  CI Dashboard  ") == "CI Dashboard"


def test_validate_project_name_allows_boundary_length():
    name = "A" * 50
    assert validate_project_name(name) == name


@pytest.mark.parametrize("name", ["", "   ", "A" * 51])
def test_validate_project_name_rejects_empty_or_too_long(name):
    with pytest.raises(ValueError):
        validate_project_name(name)


def test_validate_project_name_rejects_non_string():
    with pytest.raises(TypeError):
        validate_project_name(123)


def test_normalize_title():
    assert normalize_title("  ci    dashboard  ") == "Ci Dashboard"


def test_normalize_title_rejects_empty_title():
    with pytest.raises(ValueError):
        normalize_title(" ")


def test_summarize_successful_tests():
    result = summarize_tests(12, 12, 0)
    assert result["status"] == "success"


def test_summarize_failed_tests():
    result = summarize_tests(12, 10, 2)
    assert result["status"] == "failure"


def test_summarize_rejects_inconsistent_counts():
    with pytest.raises(ValueError, match="Passed and failed"):
        summarize_tests(12, 10, 1)


def test_summarize_rejects_negative_counts():
    with pytest.raises(ValueError, match="cannot be negative"):
        summarize_tests(-1, 0, 0)
