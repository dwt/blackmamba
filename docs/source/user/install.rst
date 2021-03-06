.. _install:

############
Installation
############


Install
-------

.. code-block:: python

    import requests as r; exec(r.get('http://bit.ly/get-blackmamba').text)

Copy the above line, paste it into Pythonista interactive prompt and execute it.
Black Mamba will be installed under the ``site-packages-3`` folder.


Update
------

Black Mamba checks for updates automatically. You can disable check for
updates entirely or you can configure time interval.
See :ref:`configuration` section.

Updates are **not** installed automatically. Black Mamba just informs you
about available update. Copy & paste the installation line into Pythonista
interactive prompt and execute it. Latest version will be downloaded and
installed.


PIP
---

Black Mamba no longer supports installation via ``pip``. Latest available
release is 1.0.2.

.. _install-startup:

Startup
-------

Black Mamba requires from you to put following lines to the
``~/Documents/site-packages-3/pythonista_startup.py`` file:

.. code-block:: python

    #!python3
    import blackmamba

    blackmamba.main()


This is bare minimum. Continue to :ref:`configuration` section to learn how to
tweak Black Mamba.
