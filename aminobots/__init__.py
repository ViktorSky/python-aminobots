"""
Amino API Wrapper
-----------------

A basic async wrapper for the Amino API.

:copyright: (c) 2023-present ViktorSky
:license: MIT, see LICENSE for more details.

"""

__title__ = 'python-aminobots'
__description__ = 'A basic async wrapper for the Amino API.'
__url__ = 'https://github.com/ViktorSky/python-aminobots'
__version__ = '0.0.1'
__author__ = 'ViktorSky'
__author_email__ = 'viktorbotsprojects@gmail.com'
__license__ = 'MIT LICENSE'
__copyright__ = 'Copyright (c) 2023 ViktorSky'


import pkgutil
import logging
from typing import Any, NamedTuple, Literal, Coroutine

from .acm import *
from .amino import *
from .bot import *
from .http import *
from .rtc import *
from .ws import *
from . import (
    abc as abc,
    enums as enums,
    errors as errors,
    models as models,
    objects as objects,
    models as models,
    utils as utils
)

__path__ = pkgutil.extend_path(__path__, __name__)

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=0, minor=0, micro=1, releaselevel='alpha', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())


def run(main: Coroutine[Any, Any, Any], *, debug=False) -> None:
    import asyncio
    try:
        asyncio.run(main, debug=debug)
    except KeyboardInterrupt:
        pass

del logging, Any, NamedTuple, Literal, Coroutine, VersionInfo, pkgutil
