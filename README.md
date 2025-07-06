# aliaser

`aliaser` provides a small metaclass and mixin that let you declare call-perfect
aliases for methods. Apply the `@alias` decorator to a method to expose it under
multiple names, or use `AliasMixin.add_alias` at runtime to add new aliases.
Importing the package automatically registers the `alias` decorator under
`builtins` so it is always available.

## Installation

Install from PyPI with `pip`:

```bash
pip install aliaser
```

Or add it to a Poetry project:

```bash
poetry add aliaser
```

## Usage

### Declaring aliases with `@alias`

```python
from aliaser import Aliases, alias

class Greeter(Aliases):
    @alias('hi', 'sup')
    def hello(self):
        print("Hello!")

Greeter().hi()  # prints "Hello!"
```

### Adding aliases at runtime

```python
Greeter.add_alias('hello', 'howdy')
Greeter().howdy()  # also prints "Hello!"
```

Importing `aliaser` adds the `alias` decorator to `builtins`, so it can be used
without an explicit import once the package is imported.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on
GitHub to discuss changes.

## Supported Python versions

This package requires Python 3.12 or newer.

## License

`aliaser` is distributed under the terms of the MIT License.

