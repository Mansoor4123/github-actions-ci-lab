"""Simple application logic for validation and text processing."""

from __future__ import annotations


def validate_project_name(name: str) -> str:
    """Validate and return a clean project name."""
    if not isinstance(name, str):
        raise TypeError("Project name must be a string")

    clean_name = name.strip()
    if not clean_name:
        raise ValueError("Project name cannot be empty")
    if len(clean_name) > 50:
        raise ValueError("Project name cannot exceed 50 characters")
    return clean_name


def normalize_title(title: str) -> str:
    """Normalize whitespace and capitalization in a title."""
    if not isinstance(title, str):
        raise TypeError("Title must be a string")

    words = title.strip().split()
    if not words:
        raise ValueError("Title cannot be empty")
    return " ".join(words).lower().title()


def summarize_tests(total: int, passed: int, failed: int) -> dict[str, int | str]:
    """Summarize test counts and raise an error for inconsistent values."""
    for value in (total, passed, failed):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Test counts must be integers")
        if value < 0:
            raise ValueError("Test counts cannot be negative")

    if passed + failed != total:
        raise ValueError("Passed and failed tests must add up to total tests")

    status = "success" if failed == 0 else "failure"
    return {"total": total, "passed": passed, "failed": failed, "status": status}
