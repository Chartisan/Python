all:
	$(MAKE) build

build:
	poetry build

publish:
	poetry publish