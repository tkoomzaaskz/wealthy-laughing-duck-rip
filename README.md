duck-api-rip
============

This repository holds a python/django code that deploys a RESTful API within
the *wealthy laughing duck* project. See the repository of the
[duck-interface project](https://github.com/tkoomzaaskz/duck-interface)
which provides a RIA (browser application) based on this API.

For more technical details, see the [documentation](doc/index.md).

Database
--------

Each duck component relies on the
[duck-commons](https://github.com/wealthy-laughing-duck/duck-commons) repository
So does the duck API - it needs the MySQL database for django. If you haven't
done it before, simply fetch duck-commons repository and execute SQL scripts
from that repo. Duck API is already configured to connect the database with
appropriate credentials.
