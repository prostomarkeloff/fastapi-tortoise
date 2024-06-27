TEST_PATH=./tests
SCRIPTS_PATH=./scripts

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

dev-up:
	$(SCRIPTS_PATH)/docker-dev-up.sh

dev-down:
	$(SCRIPTS_PATH)/docker-dev-down.sh