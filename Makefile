build:
	twine upload dist/*

build-test:
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

install-local:
	pipenv shell \
	pip install .
