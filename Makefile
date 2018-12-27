# Record and shortcuts of available project commands

build:
	# Test, build, and deploy package to PyPI.
	make build-test
	make build-deploy


build-deploy:
	# Build package and push to PyPI
	twine upload dist/*


build-test:
	# Verify package can be pushed to PyPI.
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*


bumpversion:
	# Update semantic version per .bumpversion.cfg.
	@read -p "Bump major, minor, or patch? " semvar; \
	bumpversion $$semvar


clean:
	# Remove project artifacts
	rm -Rf .eggs              # pypi
	rm -Rf .pytest_cache      # pytest
	rm -Rf build              # pypi
	rm -Rf dist               # pypi
	rm -Rf helpers.egg-info # pypi


install-local:
	# Install package in current environment.
	pip install .
