#!/usr/bin/env python
"""
Check for required dependencies for the workshop.
Usage::

  python check_env.py

"""
from distutils.version import LooseVersion

# NOTE: Update minversion values as needed.
# This should match environment.yml file.
PACKAGES = {
    'asdf': None,
    'asdf-astropy': None,
    'asdf-standard': None,
    'astropy': '4.2',
    'gwcs': '0.16',
    'jupyter': None,
    'notebook': '6.0',
    'IPython': '7.2',
    'matplotlib': '3.2',
    'numpy': '1.16',
    'pandas': '1.0',
    'scipy': '1.5',
}


def check_package(package_name: str, minimum_version: str = None, verbose: bool = True) -> bool:
    success = True
    try:
        package = __import__(package_name)
    except ImportError as err:
        print(f'Error: Failed import: {err}')
        success = False
    else:
        if package_name in ('jupyter', 'keyring'):
            installed_version = ''
        elif package_name == 'xlwt':
            installed_version = package.__VERSION__
        else:
            installed_version = package.__version__
        if (minimum_version is not None and
                LooseVersion(installed_version) <
                LooseVersion(str(minimum_version))):
            print(
                f'Error: "{package_name}" version "{minimum_version}" or later is required; you have version "{installed_version}"')
            success = False
        if success and verbose:
            print(f'Found "{package_name} {installed_version}"')
    return success


def run_checks():
    errors = []
    for package_name, min_version in PACKAGES.items():
        if not check_package(package_name, minimum_version=min_version):
            errors.append(package_name)
    if any(errors):
        print(
            '\n'
            'There are errors that you must resolve before running the tutorials.'
        )
    else:
        print(
            '\n'
            'Your Python environment is good to go!'
        )


if __name__ == '__main__':
    run_checks()
