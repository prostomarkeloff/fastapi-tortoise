TEST_PATH=./tests

init:
	pip install poetry
	poetry install

pre-commit:
	pre-commit install

black:
	black app/

test:
	export API_TEST=1
	python -m pytest --cov=app --verbose --color=yes $(TEST_PATH)