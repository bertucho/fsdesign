=======================
Factorial Survey Design
=======================


.. image:: https://img.shields.io/pypi/v/fsdesign.svg
        :target: https://pypi.python.org/pypi/fsdesign

.. image:: https://img.shields.io/travis/bertucho/fsdesign.svg
        :target: https://travis-ci.org/bertucho/fsdesign

.. image:: https://readthedocs.org/projects/fsdesign/badge/?version=latest
        :target: https://fsdesign.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python package for Factorial Survey Design


* Free software: MIT license
* Documentation: https://fsdesign.readthedocs.io.


Features
--------

* Vignettes factorial design generation

Installation
------------

Using pip:

.. code-block:: bash

    $ pip install fsdesign

Usage
-----

As a command line tool
""""""""""""""""""""""

.. code-block:: bash

    $ fsdesign [OPTIONS]

Options:
::

  -t, --template PATH  Path to template text file for vignettes
  -f, --factors PATH   Path to factors csv file
  -s, --size INTEGER   Number of resulting vignettes
  -o, --output PATH    Output file path
  -d, --duplicates     Flag for duplicated vignettes
  --help               Show usage and options information.

Example:

.. code-block:: bash

    $ fsdesign -t my_template.txt -f my_factors.csv -s 370 -o vignettes.csv -d

Template file example:

::

    Peter is a {{job_title}}.

    During the last year he has been using {{drug_type}} {{frequency}}.

Factors csv example:

=================== =============== ============
job_title           drug_type       frequency
=================== =============== ============
college professor   alcohol         occasionally
police officer      tobacco         often
student             cocaine         daily
salesman            marijuana
nightclub waiter    amphetamines
=================== =============== ============

The output is a csv file containing:

* Incremental unique ID
* Vignette text
* Assigned values for the factors within the vignette

Example:

=== ============================== =============== ============ ==============
ID  Text                           job_title       drug_type    frequency
=== ============================== =============== ============ ==============
1   Peter is a student [...]       student         alcohol      daily
2   Peter is a salesman [...]      salesman        tobacco      often
3   Peter is a student [...]       student         marijuana    occasionally
=== ============================== =============== ============ ==============

**Important:** It is recommended to use Google Spreadsheets for creating
the factors csv (File->Download->Comma-separated values) as well as for importing the output
csv to avoid problems with character encodings that other software
applications might cause.
