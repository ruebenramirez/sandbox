

# Code "challenge":

https://www.hackerrank.com/contests/30daychallenge/challenges/sum-of-two-numbers-100-1


# My notes

This is a simple task of adding 2 numbers together.  I'm taking this as an opportunity to refresh my understanding of the python [click library](https://click.palletsprojects.com/en/8.1.x/).  Testing via `clic.testing.CliRunner` does seem to make life much easier.

Testing the addition logic directly was problematic when calling the decorated functions directly.  By externalizing the "business logic" from the input handler logic, we're able to improve testability.  In our case, capturing the printed sum total via the `capfd` pytest fixture.

Having the `output` and `exit_code` from the `CliRunner` runtime makes behavioral testing much quicker.


