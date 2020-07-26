
Contributing to CompilerDock
======================
### Steps for Submitting Code
When contributing code, you\'ll want to follow this checklist:

1.  Set up your `dev-setup`
2.  Run the tests (`testing`) to confirm
    they all pass on your system. If they don\'t, you\'ll need to
    investigate why they fail. If you\'re unable to diagnose this
    yourself, raise it as a bug on github issues.
3.  Write tests that demonstrate your bug or feature. Ensure that they
    fail.
4.  Make your change.
5.  Run the entire test suite again, confirming that all tests pass
    *including the ones you just added*.
6.  Send a GitHub Pull Request to the main repository\'s `master`
    branch. GitHub Pull Requests are the expected method of code
    collaboration on this project.
### Development Setup {#dev-setup}
To get your development environment setup, run:

``` {.sh}
pipenv install --dev
pre-compile install
```
### Testing

Tests are written in `pytest` and run using tox. Tests can be run very simply:

``` {.sh}
tox
```
