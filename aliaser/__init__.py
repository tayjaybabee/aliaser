"""Initialize the package and inject the ``alias`` decorator into ``builtins``.

This module exposes the :func:`aliaser.decorator.alias` decorator and the
:class:`aliaser.mixin.AliasMixin` class.  It also registers ``alias`` on the
``builtins`` module if it does not already exist so it can be used without an
explicit import.
"""
import builtins as _bt
from .decorator import alias
from .mixin import AliasMixin as Aliases


# Avoid clobbering existing names
if not hasattr(_bt, "alias"):
    _bt.alias = alias


__all__ = ['Aliases']
