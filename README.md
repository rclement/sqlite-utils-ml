# sqlite-utils-ml

> An sqlite-utils plugin to perform machine-learning workloads

[![PyPI](https://img.shields.io/pypi/v/sqlite-utils-ml.svg)](https://pypi.org/project/sqlite-utils-ml/)
[![CI/CD](https://github.com/rclement/sqlite-utils-ml/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/rclement/sqlite-utils-ml/actions/workflows/ci-cd.yml)
[![Coverage Status](https://img.shields.io/codecov/c/github/rclement/sqlite-utils-ml)](https://codecov.io/gh/rclement/sqlite-utils-ml)
[![License](https://img.shields.io/github/license/rclement/sqlite-utils-ml)](https://github.com/rclement/sqlite-utils-ml/blob/master/LICENSE)

This [`sqlite-utils`](https://sqlite-utils.datasette.io) plugin allows to perform
machine-learning related workloads, using an MLOps philosophy.
All the underlying features are provided by [`sqlite-ml`][sqlite-ml].

## Installation

This plugin can be installed using `sqlite-utils`:
```bash
sqlite-utils install sqlite-utils-ml
```

Or you can install it as a standard Python package:
```bash
pip install sqlite-utils-ml
```

## Usage

All `sqlite-ml` SQL functions are now available through `sqlite-utils`.

For instance to load the famous "Iris Dataset":
```bash
sqlite-utils memory "select sqml_load_dataset('iris')"
```

Please refer to [`sqlite-ml`][sqlite-ml] for further instructions.

## License

Licensed under Apache License, Version 2.0

Copyright (c) 2023 - present Romain Clement


[sqlite-ml]: https://github.com/rclement/sqlite-ml