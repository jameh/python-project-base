python-project-base
===================

Just add water.

This project is in the Public Domain; see LICENSE

[![Build Status][2.1]][2.2]

## Directions

  * Code your python in / (flat is better than nested)
  * Keep good docstrings - see docs/README.md for links
    * host the docs on [readthedocs][0]
    * include well-formatted doctests
  * Keep track of your python's dependencies in requirements.txt
    * [virtualenv][1]
    * `pip freeze >> requirements.txt`
  * Write nose tests in `test.py`
    * test with `nosetests --with-doctest --with-coverage`
  * Integrate testing with [Travis CI][1] Github hook & markdown badge
  * Protect your code with a LICENSE, and refer to it in your source files
    * Go here for the know-how: [opensource.org/licences][5]
  * Replace this README with your own
  * Package it with Pip

## readthedocs directions

Follow directions at [`docs/README.md`](/docs/README.md) up till **Use Sphinx to auto-generate your .rst files**, push to your git remote, then:

  * [Sign up][0.1] / [Log in][0.2] to [readthedocs][0]
  * Create a project
    * Go to your [dashboard][0.3]
    * Click [Import][0.4]
    * Fill the forms
      * Give it the same name as on your git repository
      * Python configuration file: `docs/conf.py`
      * Use virtualenv
      * Requirements file: [`docs/doc-requirements.txt`](/docs/doc-requirements.txt)

## Github-specific directions

#### readthedocs hook
Follow the **readthedocs directions** first
  * Go to project settings on Github
  * Choose "Service Hooks" > "ReadTheDocs"
  * Check "Active", Click "Update Settings"

#### Travis CI hook
  * Customize `.travis.yml`, validate with the [ruby gem][2.3] or the [web app][2.4]
  * Go to [Travis CI][3]
  * Sign in with Github
  * Turn "ON" the repository
  * click the little wrench next to the "ON" toggle (links to Github)
  * Activate the service hook
  * include the [![Build Status][2.1]][2.2] badge in your README.md
  * push or pull and wait a couple minutes.

### GitHub Pages
  * Go to your Github project settings
  * Click on "Automatic Page Generator"
  * Edit the content in markdown (could just load README.md)
  * Continue to Layouts & choose a layout
  * Publish


## Pip directions
Use the current setup.py as a template, remove junk you don't need.

Refer to [the docs][4]

### Important kwargs
  * `name`, `version`, `description`
  * `author`, `author_email`
  * `license`
  * `url` - point it to github code, github page or readthedocs page
  * `install_requires`
  * `scripts` - point it to installable command-line scripts

then make sure it installs:
```
python setup.py install
```

then distribute to [PyPI][3]:

if it is your first time:
```
setup.py register
```

if it is your next time:
```
setup.py sdist upload
```

### Versioning:
Make sure you push your version tags to git, and that they're consistent with your setup.py `version` kwarg. If you're distributing a package with an `__init__.py`, make sure to update the version in there as well.

[0]: https://readthedocs.org
  [0.1]: https://readthedocs.org/accounts/register/
  [0.2]: https://readthedocs.org/accounts/login/
  [0.3]: https://readthedocs.org/dashboard/
  [0.4]: https://readthedocs.org/dashboard/import/
[1]: https://github.com/pypa/virtualenv
[2]: https://travis-ci.org
  [2.1]: https://travis-ci.org/jameh/python-project-base.png
  [2.2]: https://travis-ci.org/jameh/python-project-base
  [2.3]: http://about.travis-ci.org/docs/user/travis-lint/
  [2.4]: http://lint.travis-ci.org/
[3]: https://pypi.python.org/pypi
[4]: http://pythonhosted.org/distribute/
[5]: http://opensource.org/licenses/

