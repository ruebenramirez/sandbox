

# Code "challenge":

https://www.hackerrank.com/contests/30daychallenge/challenges/sum-of-two-numbers-100-1


# My notes

This is a simple task of adding 2 numbers together.  I'm taking this as an opportunity to refresh my understanding of the python [click library](https://click.palletsprojects.com/en/8.1.x/).  Testing via `clic.testing.CliRunner` does seem to make life much easier.

Testing the addition logic directly was problematic when calling the decorated functions directly.  By externalizing the "business logic" from the input handler logic, we're able to improve testability.  In our case, capturing the printed sum total via the `capfd` pytest fixture.

Having the `output` and `exit_code` from the `CliRunner` runtime makes behavioral testing much quicker.


## Example run output

```
$ make run
poetry run python3 app.py 1 2
3
```

## Example test output

```
$ make test
poetry run pytest .
======================================================================================== test session starts =========================================================================================
platform linux -- Python 3.10.12, pytest-8.3.2, pluggy-1.5.0
rootdir: /home/rramirez/code/sandbox/hackerrank/sum-two-numbers
configfile: pyproject.toml
collected 3 items

test_sums.py ...                                                                                                                                                                               [100%]

========================================================================================= 3 passed in 0.04s ==========================================================================================
```
