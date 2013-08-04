# You found the docs!
(sortof) Take the next step and read them: <INSERT URL HERE>

Or, if you prefer, you can build them in many formats.

Here's how to build them [*from scratch*](http://youtu.be/7s664NsLeFM):

## Grab Requirements
For all build cases, install Sphinx, and the app dependencies for the Sphinx autodocs extension.
```sh
pip install -r docs/doc-requirements
```

## Create the .rst files
You can make these manually, but that's no fun. Keep your docstrings chock-full with helpful usage tips, and let [Autodoc](http://sphinx-doc.org/tutorial.html#autodoc) take care of you

In either case, use the reStructuredText & discover some handy Sphinx directives - here are the docs:

  * [reStructuredText Primer](http://sphinx-doc.org/rest.html)
  * [Sphinx Markup Constructs](http://sphinx-doc.org/markup/index.html)
  * [Sphinx Domains](http://sphinx-doc.org/domains.html)

All subsequent commands issue with the working directory docs/
```sh
cd docs
```

### Use Sphinx to auto-generate your .rst files
```sh
sphinx-apidoc -F -H "Project Name" -A "Author Name" -V "doc-version" -o ./ \
../src
```
(add a `-f` option to overwrite existing .rst files)
Make sure that created `index.rst`, `conf.py`, `make.bat`, `Makefile`, and a `.rst` file for each of your modules inside `src`

## Make the text
```sh
make text
```
will output generated text files to `docs/_build/text/`

## Make the html
```sh
make html
```
will output generated html files to `docs/_build/html`

## Run the inline code snippets in the docstrings
```sh
make doctest
```
will output results from the test to `docs/_build/doctest/output.txt`
