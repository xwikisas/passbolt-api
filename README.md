# Passbolt API

This package provides bindings to a Passbolt server API. Each of the bindings declared in this package aim to follow the [official Passbolt API documentation](https://api-reference.passbolt.com/).

## Releasing a new version

Before releasing a new version of the package, please take some time to read a bit about Python packaging [here](https://packaging.python.org/tutorials/packaging-projects/).

Once, this is done, you will need the standard utilities to build and upload the package, namely : 

* setuptools
* wheel
* twine

### Make sure that you have a clean index

* Check that you have nothing to commit
* Check that you are on `master`
* Check that you are up to date with the remote repository

### Build the distribution archives

Simply run :

```
python3 setup.py sdist bdist_wheel
```

This will generate the package archives in `dist/`

### Upload the archives to PyPI

Make sure that you have access to one of the maintainers account credentials for the package. You can see the list of maintainers for the project [here](https://pypi.org/project/passbolt-api/).

Prepare the account username and password and then run the following to upload the archives :

```
python3 -m twine upload dist/*
```

### Tag the version

For good measure, tag the commit from which you released the packet with `git tag -s v<version> <commit>`.
