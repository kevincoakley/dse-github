# dse-github

![Python package](https://github.com/kevincoakley/dse-github/workflows/Python%20package/badge.svg)
[![codecov](https://codecov.io/gh/kevincoakley/dse-github/branch/master/graph/badge.svg)](https://codecov.io/gh/kevincoakley/dse-github)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Requirements

Python 3.6+

## Install

Install via pip:

    $ pip install git+https://github.com/kevincoakley/dse-github.git

Install from source:

    $ git clone https://github.com/kevincoakley/dse-github.git
    $ cd dse-github
    $ python setup.py install
    
## Uninstall

Uninstall via pip:

    $ pip uninstall dse-github -y
    
## Commands

Run with GitHub Username & Password:

    $ dse-github --username user --password pass --file ~/form.csv

Run with GitHub Access Token (if you account is using 2fa):

    $ dse-github --access-token abc123 --file ~/form.csv

## CSV Example:

    Username,Repository,Cohort
    github-username-01,github-repo-01,cohort01
    github-username-02,github-repo-02,cohort01
    github-username-03,github-repo-03,cohort01
