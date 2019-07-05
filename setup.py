import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'requests_gpgauthlib>=0.1.2'
]

setuptools.setup(
    name="passbolt-api",
    version="0.0.3",
    author="XWiki SAS Development Team",
    author_email="pypi@xwiki.com",
    description="Provides API bindings for the Passbolt API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xwikisas/passbolt-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
    ],
    install_requires=requires
)
