python-project-base
===================

Just add water.

This project is in the Public Domain, see LICENSE

## Directions

  * Code your python in src/
  * Keep good docstrings - see docs/README.md for links
    * host the docs on https://readthedocs.org
  * Keep track of your python's dependencies in requirements.txt
    * [virtualenv](https://github.com/pypa/virtualenv)
    * `pip freeze >> requirements.txt`
  * Protect your code with a LICENSE, and refer to it in your source files
    * Go here for the know-how: http://opensource.org/licenses/
  * Replace this README with your own
  * Package it with Pip

## readthedocs directions

Follow directions at `docs/README.md` up till **Use Sphinx to auto-generate your .rst files**, push to your git remote, then:

  * [Sign up](https://readthedocs.org/accounts/register/) / [Log in](https://readthedocs.org/accounts/login/)
  * Create a project
    * Go to your [dashboard](https://readthedocs.org/dashboard/)
    * Click [Import](https://readthedocs.org/dashboard/import/)
    * Fill the forms
      * Give it the same name as on your git repository
      * Python configuration file: `docs/conf.py`
      * Use virtualenv
      * Requirements file: `docs/doc-requirements.txt`

## Github-specific directions
### readthedocs hook
Follow the **readthedocs directions** first
  * Go to your Github project settings
  * Click on "Service Hooks" on the left
  * Choose "ReadTheDocs"
  * Check "Active", Click "Update Settings"

### GitHub Pages
  * Go to your Github project settings
  * Click on "Automatic Page Generator"
  * Edit the content in markdown (could just load REAMDE.md)
  * Continue to Layouts & choose a layout
  * Publish


## Pip directions
http://pythonhosted.org/distribute/