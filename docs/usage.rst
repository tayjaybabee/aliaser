Usage
=====

This section demonstrates common ways to declare and work with method aliases.

Declaring aliases with ``@alias``
---------------------------------

.. code-block:: python

   from aliaser import Aliases, alias

   class Greeter(Aliases):
       @alias('hi', 'sup')
       def hello(self):
           print("Hello!")

   Greeter().hi()  # prints "Hello!"

Adding aliases at runtime
-------------------------

.. code-block:: python

   Greeter.add_alias('hello', 'howdy')
   Greeter().howdy()  # also prints "Hello!"

Avoiding the built-ins side effect
----------------------------------

Importing the top-level package calls :func:`aliaser.install` which registers
``alias`` on ``builtins``. This modifies the global namespace. Call
:func:`aliaser.uninstall` to undo the side effect, or import :func:`alias` from
``aliaser.decorator`` and :class:`aliaser.mixin.AliasMixin` directly instead of
importing ``aliaser``.

