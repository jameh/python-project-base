from setuptools import setup
setup(
    name = "HelloWorld",
    version = "0.1",
    # scripts = [],
    install_requires = ['flask==0.10.1'],

    # metadata for upload to PyPI
    author = "Me",
    author_email = "me@example.com",
    description = "This is an Example Package",
    license = "PSF",
    keywords = "hello world example examples",
    url = "http://example.com/HelloWorld/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
