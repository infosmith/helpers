"""Package setup script."""

from setuptools import setup, find_packages

# Python packaging constants
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]
LICENSES = {
    'MIT license':
        'License :: OSI Approved :: MIT License',
    'BSD license':
        'License :: OSI Approved :: BSD License',
    'Apache Software License 2.0':
        'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3':
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
}
REQUIREMENTS = {
    'install': [],
    'setup': ['pytest-runner'],
    'tests': ['pytest']
}

# Project constants
EMAIL = 'infosmith@prontonmail.com'
FULL_NAME = "David S."
GITHUB_ACCOUNT = 'infosmith'
LICENSE = 'MIT license'
PROJECT_SLUG = 'helpers'
PROJECT_SHORT_DESCRIPTION = 'Improved developer experience, accumulated.'
VERSION = '0.2.0'

# Project conditional configuration
if 'MIT license' in LICENSES.keys():
    CLASSIFIERS.append(LICENSES['MIT license'])

# Configure project
setup(
    author=FULL_NAME,
    author_email=EMAIL,
    classifiers=CLASSIFIERS,
    description=PROJECT_SHORT_DESCRIPTION,
    include_package_data=True,
    install_requires=REQUIREMENTS['install'],
    keywords=PROJECT_SLUG,
    license=LICENSE,
    name=PROJECT_SLUG,
    packages=find_packages(include=[PROJECT_SLUG]),
    setup_requires=REQUIREMENTS['setup'],
    test_suite='tests',
    tests_require=REQUIREMENTS['tests'],
    url="https://github.com/{}/{}".format(GITHUB_ACCOUNT, PROJECT_SLUG),
    version=VERSION,
    zip_safe=False,
)
