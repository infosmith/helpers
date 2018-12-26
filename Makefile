build:
	twine upload dist/*

build-test:
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

clean:
	rm -Rf .eggs
	rm -Rf .pytest_cache
	rm -Rf batteries.egg-info
	rm -Rf build
	rm -Rf dist

install-local:
	pipenv shell \
	pip install .
