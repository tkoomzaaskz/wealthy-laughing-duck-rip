The Wealthy Laughing Duck Project
---------------------------------

This repository is a [duck component](https://github.com/wealthy-laughing-duck).
Visit [Wealthy Laughing Duck Project](http://wealthy-laughing-duck.github.io/) for more information.

Python/Django API
=================

This duck component is a RESTful API consumed by other duck components,
suck as the [duck interface](https://github.com/wealthy-laughing-duck/duck-interface),
which provides a RIA (browser application) based on this API.

Dependencies
------------

 * [django framework](https://www.djangoproject.com/)
 * [django tastypie API generator](django-tastypie.readthedocs.org)
 * [bootstrap](http://twitter.github.com/bootstrap/)

For more technical details, see the [documentation](doc/README.md).

Database
--------

Each duck component relies on the
[duck-commons](https://github.com/wealthy-laughing-duck/duck-commons) repository
So does the duck API - it needs the MySQL database for django. If you haven't
done it before, simply fetch duck-commons repository and execute SQL scripts
from that repo. Duck API is already configured to connect the database with
appropriate credentials.
