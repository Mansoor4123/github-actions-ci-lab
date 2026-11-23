# CI Dashboard

A lightweight DevOps lab project that demonstrates the relationship between application code, automated tests, and GitHub Actions. The dashboard is a static HTML/CSS/JavaScript demo and uses clearly labeled sample data.

## Project structure

```text
github-actions-ci-lab/
├── frontend/                 # Static CI dashboard
│   ├── index.html
│   ├── style.css
│   └── script.js
├── src/                      # Python application modules
│   ├── app.py
│   └── calculator.py
├── tests/                    # Pytest test suite
│   ├── test_app.py
│   └── test_calculator.py
├── .github/workflows/        # Intentionally empty; add the workflow in a later lab step
├── requirements.txt
└── .gitignore
```

## How the pieces relate

- `src/calculator.py` provides basic mathematical operations and validation.
- `src/app.py` provides project-name validation, title processing, and test-result summaries.
- `tests/` verifies normal behavior, boundaries, invalid inputs, and exceptions.
- `frontend/` visualizes a CI pipeline and static sample execution data.
- GitHub Actions will later run `pytest` automatically on pushes and pull requests.

## Run locally

From the project directory:

```bash
cd github-actions-ci-lab
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
pytest -v
```

To view the dashboard, open `frontend/index.html` directly in a browser or serve the directory:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000/frontend/`.

## Demonstrating a failing CI run

The committed test suite is expected to pass. To demonstrate a failure safely:

1. Change an assertion in a test, for example `assert add(10, 5) == 15` to `assert add(10, 5) == 16`.
2. Run `pytest -v` and confirm that Pytest reports the failure.
3. Revert the change before committing.

In GitHub Actions, a failing Pytest command exits with a non-zero status and GitHub marks the workflow run as failed.

## GitHub Actions setup (later step)

Create `.github/workflows/ci.yml` after this lab setup. The workflow should check out the repository, set up Python, install `requirements.txt`, and run `pytest -v`. This project intentionally does not include a workflow YAML file.
