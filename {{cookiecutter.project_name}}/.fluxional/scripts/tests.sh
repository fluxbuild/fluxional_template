poetry run coverage run -m pytest -vv
poetry run mypy fluxional/
poetry run ruff fluxional/
poetry run coverage html
