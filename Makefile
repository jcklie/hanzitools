test:
	python -m unittest

black:
	black -l 120 hanzitools/
	black -l 120 tests/
	black -l 120 examples/