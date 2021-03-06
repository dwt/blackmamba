#!python3
"""
I strongly suggests to check
`config.py:_DEFAULTS <https://github.com/zrzka/blackmamba/blob/master/blackmamba/config.py>`_
from time to time. Just to check if this documentation isn't outdated.

Sections
========

.. _configuration-general:

General
-------

Defaults:

.. code-block:: python

    'general': {
        'jedi': False,
        'register_key_commands': True,
        'page_line_count': 40
    }


``jedi: bool`` - `JEDI <http://jedi.readthedocs.io/en/latest/>`_ is used as a backend for Find usages,
Jump to definition and Show documentation :ref:`scripts`. But because JEDI is also used by the Pythonista,
JEDI is not thread safe and I don't know when and how it is used, it's disabled by default. You have to
set it to ``True`` to enable mentioned scripts.

``register_key_commands: bool`` - set to ``False`` to disable default :ref:`shortcuts`.

``page_line_count: int`` - number of lines to scroll up / down for page up / down.


.. _configuration-updates:

Updates
-------

Defaults:

.. code-block:: python

    'update': {
        'enabled': True,
        'interval': 3600
    }

``enabled: bool`` - set to ``False`` to disable check for updates.

``interval: int`` - check for updates time interval (in seconds).


.. _configuration-file_picker:

File picker
-----------

Defaults:

.. code-block:: python

    'file_picker': {
        'ignore_folders': {
            '': ['.git'],
            '.': ['.Trash', 'Examples',
                  'site-packages', 'site-packages-2', 'site-packages-3']
        }
    }

``ignore_folders: dict`` - key is a parent directory (not full path, just name) and value is a list of
folders to ignore. You can use two special values as keys:


* ``''`` - any parent directory,
* ``'.'`` - parent directory is ``~/Documents``.

Default value says that ``.git`` folder inside any folder is ignored. ``.Trash``,
``Examples``, ... folders inside ``~/Documents`` folder are ignored as well.

Affects Open quickly and Run quickly scripts, see :ref:`scripts`.

.. _configuration-analyzer:

Analyzer
--------

Defaults (since 1.1.0):

* ``ignore_codes`` option is removed /ignored
* ``max_line_length`` option is removed / ignored

.. code-block:: python

    'analyzer': {
        'hud_alert_delay': 1.0,
        'remove_whitespaces': True,
        'flake8': [
            # 1st pass
            ['--select=E901,E999,F821,F822,F823'],
            # 2nd pass
            ['--max-complexity=10', '--max-line-length=127']
        ]
    }

If ``flake8`` is provided, ``ignore_codes`` and ``max_line_length`` options are ignored. ``flake8``
must contain list of passes and every pass contains list of ``flake8`` arguments. You can run ``flake8``
several times with different options in this way.

Defaults (pre 1.1.0):

.. code-block:: python

    'analyzer': {
        'hud_alert_delay': 1.0,
        'ignore_codes': None,
        'max_line_length': 127,
        'remove_whitespaces': True
    }

Affects Analyze script, see :ref:`scripts`.

.. _configuration-tester:

Tester
------

Defaults:

.. code-block:: python

    'tester': {
        'hud_alert_delay': 1.0,
        'hide_console': True
    }

Affects Run unit tests script, see :ref:`scripts`.

.. _configuration-drag_and_drop:

Drag and Drop
-------------

Defaults:

.. code-block:: python

    'drag_and_drop': {
        'ignore_folders': {
            '': ['.git'],
            '.': ['.Trash', 'Examples',
                  'site-packages', 'site-packages-2', 'site-packages-3', 'stash_extensions']
        }
    }

Affects Drag & Drop script, see :ref:`scripts`.

.. _configuration-documentation:

Documentation
-------------

Defaults:

.. code-block:: python

    'documentation': {
        'reuse': True,
        'frame': (630, 110, 730, 350)
    }

``reuse: bool`` - same overlay view is reused for consequent show documentation calls if
set to ``True``. Otherwise multiple overlays appear in consequent show documentation calls,
but if a symbol's fully qualified name matches existing overlay, this particular overlay is
expanded and activated.

``frame: tuple(float, float, float, float)`` - initial overlay frame in the key window coordinates.

Affects Show documentation script, see :ref:`scripts`.

Sample
======

See `pythonista_startup.py <https://github.com/zrzka/blackmamba/blob/master/pythonista_startup.py>`_
for more examples.
"""

from collections import Mapping
from copy import deepcopy

__all__ = ['get_config_value']

_DEFAULTS = {
    'general': {
        'jedi': False,
        'register_key_commands': True,
        'page_line_count': 40
    },
    'update': {
        'enabled': True,
        'interval': 3600
    },
    'file_picker': {
        'ignore_folders': {
            '': ['.git'],
            '.': ['.Trash', 'Examples',
                  'site-packages', 'site-packages-2', 'site-packages-3']
        }
    },
    'analyzer': {
        'hud_alert_delay': 1.0,
        'remove_whitespaces': True,
        'flake8': [
            # 1st pass
            ['--select=E901,E999,F821,F822,F823'],
            # 2nd pass
            ['--max-complexity=10', '--max-line-length=127']
        ]
    },
    'tester': {
        'hud_alert_delay': 1.0,
        'hide_console': True
    },
    'drag_and_drop': {
        'ignore_folders': {
            '': ['.git'],
            '.': ['.Trash', 'Examples',
                  'site-packages', 'site-packages-2', 'site-packages-3', 'stash_extensions']
        }
    },
    'documentation': {
        'reuse': True,
        'frame': (630, 110, 730, 350)
    }
}

_config = dict(_DEFAULTS)


def get_config_value(key_path, default=None):
    v = _config
    try:
        for k in key_path.split('.'):
            v = v[k]
        return v
    except TypeError:
        return default
    except KeyError:
        return default


def _update(d, u):
    for k, v in u.items():
        if isinstance(d, Mapping):
            if isinstance(v, Mapping):
                d[k] = _update(d.get(k, {}), v)
            else:
                d[k] = v
        else:
            d = {k: v}
    return d


def update_config_with_dict(d):
    global _config
    _config = _update(deepcopy(_config), d)
