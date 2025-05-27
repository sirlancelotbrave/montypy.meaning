|Icon| |title|_
===============

.. |title| replace:: montypy.meaning
.. _title: https://kot-roundtable.github.io/montypy.meaning

.. |Icon| image:: https://avatars.githubusercontent.com/kot-roundtable
        :target: https://kot-roundtable.github.io/montypy.meaning
        :height: 100px

|PyPI| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/kot-roundtable/montypy.meaning/actions/workflows/matrix-and-codecov-on-merge-to-main.yml/badge.svg
        :target: https://github.com/kot-roundtable/montypy.meaning/actions/workflows/matrix-and-codecov-on-merge-to-main.yml

.. |Codecov| image:: https://codecov.io/gh/kot-roundtable/montypy.meaning/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/kot-roundtable/montypy.meaning

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/montypy.meaning
        :target: https://anaconda.org/conda-forge/montypy.meaning

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPI| image:: https://img.shields.io/pypi/v/montypy.meaning
        :target: https://pypi.org/project/montypy.meaning/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/montypy.meaning
        :target: https://pypi.org/project/montypy.meaning/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/kot-roundtable/montypy.meaning/issues

A Python package for the the Knights of the Round Table.

* LONGER DESCRIPTION HERE

For more information about the montypy.meaning library, please consult our `online documentation <https://kot-roundtable.github.io/montypy.meaning>`_.

Citation
--------

If you use montypy.meaning in a scientific publication, we would like you to cite this package as

        montypy.meaning Package, https://github.com/kot-roundtable/montypy.meaning

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``montypy.meaning_env`` ::

        conda create -n montypy.meaning_env montypy.meaning
        conda activate montypy.meaning_env

To confirm that the installation was successful, type ::

        python -c "import montypy.meaning; print(montypy.meaning.__version__)"

The output should print the latest version displayed on the badges above.

If the above does not work, you can use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``montypy.meaning_env`` environment, type ::

        pip install montypy.meaning

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/kot-roundtable/montypy.meaning/>`_. Once installed, ``cd`` into your ``montypy.meaning`` directory
and run the following ::

        pip install .

Getting Started
---------------

You may consult our `online documentation <https://kot-roundtable.github.io/montypy.meaning>`_ for tutorials and API references.

Support and Contribute
----------------------

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/kot-roundtable/montypy.meaning/issues>`_ and/or `submit a fix as a PR <https://github.com/kot-roundtable/montypy.meaning/pulls>`_.

Feel free to fork the project and contribute. To install montypy.meaning
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contributing, please read our `Code of Conduct <https://github.com/kot-roundtable/montypy.meaning/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact
-------

For more information on montypy.meaning please visit the project `web-page <https://kot-roundtable.github.io/>`_ or email Sir Lancelot at sirlancelotbrave@montypy.com.

Acknowledgements
----------------

``montypy.meaning`` is built and maintained with `scikit-package <https://scikit-package.github.io/scikit-package/>`_.
