test:
	poetry run python -m pytest --cov=. --hypothesis-show-statistics

# flags required by black (https://bit.ly/2Qovtjm)
lint:
	python -m flake8 --max-line-length=88 --extend-ignore=E203,W503 .

format:
	poetry run isort .
	poetry run black .
