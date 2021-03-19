test:
	poetry run python -m pytest --hypothesis-show-statistics

lint:
	python -m flake8 .

format:
	python -m isort .
