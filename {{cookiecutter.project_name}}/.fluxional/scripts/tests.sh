poetry run coverage run -m pytest -vv
poetry run mypy .
poetry run ruff .
poetry run coverage html