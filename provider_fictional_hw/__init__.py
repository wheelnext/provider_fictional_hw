#!/usr/bin/env python

import importlib.metadata

# from provider_fictional_hw.plugin import FictionalHWPlugin

__all__ = ["FictionalHWPlugin", "__version__"]

__version__ = importlib.metadata.version("provider_fictional_hw")
