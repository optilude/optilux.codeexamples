====================
optilux.codeexamples
====================

This package contains various doctests with example code outlining Zope
development concepts. They are all set up in ``tests.py``. See the various
``.txt`` files and follow along with the examples there to learn about
different aspects of Zope programming. Feel free to make changes to the
example code or to write new tests if it helps your understanding.

To create a test environment, run the following from the package root::

    $ python2.6 bootstrap.py
    $ bin/buildout

Then run the tests are normal, with::

    $ ./bin/test
