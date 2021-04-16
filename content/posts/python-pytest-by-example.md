---
title: "Pytest by Example"
date: "2020-04-21"
summary: "Examples of usage and configuration for pytest"
tags: [
    "python",
]
---

`pytest` is a popular python test framework. below are a collection of snippets and examples for usage.

<!-- TOC -->

- [Configuration files](#configuration-files)
    - [pytest.ini](#pytestini)
    - [conftest.py](#conftestpy)
- [Markers](#markers)
    - [Document markers in pytest.ini](#document-markers-in-pytestini)
    - [Run tests against markers](#run-tests-against-markers)
- [Fixtures](#fixtures)

<!-- /TOC -->

## Configuration files

`pytest` is based on 2 files that you host at the root of your testing suites.

### pytest.ini

example:

```ini
[pytest]
python_files test_*
python_classes = *Tests
python_functions test_*

markers =
    smoke: collection of smokes tests to be run on every build
    slow: slow collection of tests
    logic: all logic tests
```

### conftest.py

example:

```python
from pytest import fixture

@fixture
def global_example():
    print("called global_exaple")
```

## Markers

Allow you to collect tests together via adding a construct against each function or class.

``` python
from pytest import mark

@mark.my_class
class my_classTests:
    
    @mark.smoke
    @mark.input
    def test_input_value():
        assert true
    @mark.output
    def test_output_value():
        assert true
```

The above will mark:

- `test_input_value` with `my_class, smoke, input`
- `test_output_value` with `my_class, output`

### Document markers in pytest.ini

You can add documentation to markers via updating the `pytest.ini` file with:

``` ini
markers =
    smoke: collection of smokes tests to be run on every build
    math: all math logic tests
    logic: all logic tests
```

You can return the markers information via:

``` bash
pytest --markers
```

### Run tests against markers

To run tests against markers you have some basic `sql` like syntax

```bash
pytest -m smoke
pytest -m "input or output"
pytest -m "smoke and input"
pytest -m "not slow"
```

## Fixtures

Allow for reusable snippets of code.

Add the `fixture` to `conftest.py`

```python
from pytest import fixture

@fixture
def global_example():
    print("called global_exaple")
```

Use the fixture in test:

```python
def test_global_example(global_example):
    """
    calls the global_example fixture
    """
    assert true
```

## Parameterize

```python
def test_is_palindrome_empty_string():
    assert is_palindrome("")

def test_is_palindrome_single_character():
    assert is_palindrome("a")

def test_is_palindrome_mixed_casing():
    assert is_palindrome("Bob")

def test_is_palindrome_with_spaces():
    assert is_palindrome("Never odd or even")

def test_is_palindrome_with_punctuation():
    assert is_palindrome("Do geese see God?")

def test_is_palindrome_not_palindrome():
    assert not is_palindrome("abc")

def test_is_palindrome_not_quite():
    assert not is_palindrome("abab")
```


into 

``` python
@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God?",
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abab",
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)
```