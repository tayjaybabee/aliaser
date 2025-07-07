# aliaser

aliaser provides a tiny metaclass and mixin that let you expose call-perfect
method aliases without writing boilerplate forwarders.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Declaring aliases with `@alias`](#declaring-aliases-with-alias)
  - [Adding aliases at runtime](#adding-aliases-at-runtime)
  - [Avoiding the built-ins side effect](#avoiding-the-built-ins-side-effect)
- [Development](#development)
- [Supported Python versions](#supported-python-versions)
- [License](#license)

## Features

- `@alias` decorator to expose a method or property under multiple names.
- `Aliases` mixin for runtime helpers, backed by the `AliasMeta` metaclass.
- Property and method aliases share the original descriptor – no wrappers.
- Automatically registers `alias` on `builtins` when importing the package for
  drop-in usage.

## Installation

Install from PyPI:

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

### Avoiding the built-ins side effect

Importing the top-level package registers `alias` on `builtins` so it can be
used without an explicit import. This modifies the global namespace. To avoid
that side effect, import `alias` from `aliaser.decorator` and `Aliases` from
`aliaser.mixin` directly instead of importing `aliaser`.

## Development

Clone the repository and install dependencies with Poetry:

```bash
poetry install
```

After making changes you can build the wheel with `poetry build`. Feel free to
open issues or pull requests on GitHub to discuss improvements.

## Supported Python versions

This project requires Python 3.12 or newer.

## License

`aliaser` is distributed under the MIT License.
